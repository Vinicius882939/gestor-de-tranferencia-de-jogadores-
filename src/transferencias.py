from utils import ok, criado, nao_encontrado, erro, encontrar_por_id, validar_id, carregar_dados, guardar_dados

FICHEIRO = "dados/transferencias.json"
_transferencias, _proximo_id = carregar_dados(FICHEIRO)

ESTADOS_VALIDOS = {"pendente", "concluida", "cancelada"}

def _guardar():
    guardar_dados(FICHEIRO, _transferencias, _proximo_id)


def criar_transferencia(jogador_id, clube_origem_id, clube_destino_id, empresario_id, valor, data):
    global _proximo_id
    jid, msg = validar_id(jogador_id)
    if jid is None:
        return erro(msg)
    did, msg = validar_id(clube_destino_id)
    if did is None:
        return erro(msg)
    try:
        valor = float(valor)
    except (ValueError, TypeError):
        return erro("Valor da transferencia invalido.")
    oid = None
    if clube_origem_id not in (None, ""):
        oid, msg = validar_id(clube_origem_id)
        if oid is None:
            return erro(msg)
    eid = None
    if empresario_id not in (None, ""):
        eid, msg = validar_id(empresario_id)
        if eid is None:
            return erro(msg)
    transferencia = {"id": _proximo_id, "jogador_id": jid, "clube_origem_id": oid,
                     "clube_destino_id": did, "empresario_id": eid,
                     "valor": valor, "data": data or "", "estado": "pendente"}
    _transferencias.append(transferencia)
    _proximo_id += 1
    _guardar()
    return criado(transferencia, "Transferencia criada com sucesso.")


def listar_transferencias():
    return ok(list(_transferencias)) if _transferencias else ok([], "Nao ha transferencias registadas.")


def consultar_transferencia(id_t):
    id_, msg = validar_id(id_t)
    if id_ is None:
        return erro(msg)
    t = encontrar_por_id(_transferencias, id_)
    return ok(t) if t else nao_encontrado(f"Transferencia com ID {id_} nao encontrada.")


def atualizar_transferencia(id_t, valor=None, data=None, estado=None):
    id_, msg = validar_id(id_t)
    if id_ is None:
        return erro(msg)
    t = encontrar_por_id(_transferencias, id_)
    if t is None:
        return nao_encontrado(f"Transferencia com ID {id_} nao encontrada.")
    if valor is not None:
        try:
            t["valor"] = float(valor)
        except (ValueError, TypeError):
            return erro("Valor invalido.")
    if data   is not None: t["data"]   = data
    if estado is not None:
        if estado not in ESTADOS_VALIDOS:
            return erro(f"Estado invalido. Valores aceites: {', '.join(ESTADOS_VALIDOS)}.")
        t["estado"] = estado
    _guardar()
    return ok(t, "Transferencia atualizada com sucesso.")


def remover_transferencia(id_t):
    id_, msg = validar_id(id_t)
    if id_ is None:
        return erro(msg)
    t = encontrar_por_id(_transferencias, id_)
    if t is None:
        return nao_encontrado(f"Transferencia com ID {id_} nao encontrada.")
    if t["estado"] == "pendente":
        return erro("Nao e possivel remover uma transferencia pendente. Cancela-a primeiro.")
    _transferencias.remove(t)
    _guardar()
    return ok(None, f"Transferencia {id_} removida com sucesso.")
