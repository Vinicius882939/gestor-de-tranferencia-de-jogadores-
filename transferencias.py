# ==============================
# transferencias.py
# CRUD de Transferencias
# ==============================

transferencias = []
proximo_id = 1


def _encontrar_transferencia(id_transferencia):
    for t in transferencias:
        if t["id"] == id_transferencia:
            return t
    return None


# CREATE
def criar_transferencia(jogador_id, clube_origem_id, clube_destino_id,
                        empresario_id, valor, data):
    global proximo_id

    if not jogador_id or not clube_destino_id:
        return (400, "Jogador e clube de destino sao obrigatorios.")

    if clube_origem_id and clube_origem_id == clube_destino_id:
        return (400, "Clube de origem e destino nao podem ser iguais.")

    try:
        valor = float(valor)
    except (ValueError, TypeError):
        return (400, "Valor invalido.")

    transferencia = {
        "id"               : proximo_id,
        "jogador_id"       : int(jogador_id),
        "clube_origem_id"  : int(clube_origem_id) if clube_origem_id else None,
        "clube_destino_id" : int(clube_destino_id),
        "empresario_id"    : int(empresario_id) if empresario_id else None,
        "valor"            : valor,
        "data"             : data,
        "estado"           : "pendente"
    }
    transferencias.append(transferencia)
    proximo_id += 1
    return (201, "Transferencia criada com sucesso.", transferencia)


# READ - listar todas
def listar_transferencias():
    if len(transferencias) == 0:
        return (200, "Sem transferencias registadas.", [])
    return (200, "OK", transferencias)


# READ - consultar uma
def consultar_transferencia(id_transferencia):
    try:
        id_transferencia = int(id_transferencia)
    except (ValueError, TypeError):
        return (400, "ID invalido.")

    t = _encontrar_transferencia(id_transferencia)
    if t is None:
        return (404, "Transferencia nao encontrada.")
    return (200, "OK", t)


# UPDATE
def atualizar_transferencia(id_transferencia, valor=None, data=None, estado=None):
    try:
        id_transferencia = int(id_transferencia)
    except (ValueError, TypeError):
        return (400, "ID invalido.")

    t = _encontrar_transferencia(id_transferencia)
    if t is None:
        return (404, "Transferencia nao encontrada.")

    if t["estado"] != "pendente":
        return (400, f"Nao e possivel editar uma transferencia '{t['estado']}'.")

    if valor:
        try:
            t["valor"] = float(valor)
        except ValueError:
            return (400, "Valor invalido.")
    if data:  t["data"]  = data
    if estado:
        if estado not in ("pendente", "concluida", "cancelada"):
            return (400, "Estado invalido. Use: pendente, concluida ou cancelada.")
        t["estado"] = estado

    return (200, "Transferencia atualizada com sucesso.", t)


# DELETE
def remover_transferencia(id_transferencia):
    try:
        id_transferencia = int(id_transferencia)
    except (ValueError, TypeError):
        return (400, "ID invalido.")

    t = _encontrar_transferencia(id_transferencia)
    if t is None:
        return (404, "Transferencia nao encontrada.")

    if t["estado"] == "pendente":
        return (400, "Nao e possivel remover uma transferencia pendente. Cancela primeiro.")

    transferencias.remove(t)
    return (200, f"Transferencia #{t['id']} removida com sucesso.")
