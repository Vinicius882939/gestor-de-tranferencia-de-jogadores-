# ============================================
#   clubes.py — CRUD de Clubes
# ============================================

from utils import ok, criado, nao_encontrado, erro, encontrar_por_id, validar_id

_clubes = []
_proximo_id = 1


# ──────────────────────────────────────────
#  CREATE
# ──────────────────────────────────────────

def criar_clube(nome, pais, liga, estadio=None, fundacao=None):
    global _proximo_id

    if not nome or not pais or not liga:
        return erro("Nome, pais e liga sao obrigatorios.")

    clube = {
        "id"       : _proximo_id,
        "nome"     : nome,
        "pais"     : pais,
        "liga"     : liga,
        "estadio"  : estadio or "",
        "fundacao" : fundacao or "",
    }
    _clubes.append(clube)
    _proximo_id += 1
    return criado(clube, f"Clube '{nome}' criado com sucesso.")


# ──────────────────────────────────────────
#  READ
# ──────────────────────────────────────────

def listar_clubes():
    if not _clubes:
        return ok([], "Nao ha clubes registados.")
    return ok(list(_clubes))


def consultar_clube(id_clube):
    id_, msg = validar_id(id_clube)
    if id_ is None:
        return erro(msg)

    clube = encontrar_por_id(_clubes, id_)
    if clube is None:
        return nao_encontrado(f"Clube com ID {id_} nao encontrado.")
    return ok(clube)


# ──────────────────────────────────────────
#  UPDATE
# ──────────────────────────────────────────

def atualizar_clube(id_clube, nome=None, pais=None, liga=None,
                    estadio=None, fundacao=None):
    id_, msg = validar_id(id_clube)
    if id_ is None:
        return erro(msg)

    clube = encontrar_por_id(_clubes, id_)
    if clube is None:
        return nao_encontrado(f"Clube com ID {id_} nao encontrado.")

    if nome     is not None: clube["nome"]     = nome
    if pais     is not None: clube["pais"]     = pais
    if liga     is not None: clube["liga"]     = liga
    if estadio  is not None: clube["estadio"]  = estadio
    if fundacao is not None: clube["fundacao"] = fundacao

    return ok(clube, "Clube atualizado com sucesso.")


# ──────────────────────────────────────────
#  DELETE
# ──────────────────────────────────────────

def remover_clube(id_clube, lista_jogadores):
    """
    lista_jogadores — lista atual de jogadores (para verificar dependencias).
    """
    id_, msg = validar_id(id_clube)
    if id_ is None:
        return erro(msg)

    clube = encontrar_por_id(_clubes, id_)
    if clube is None:
        return nao_encontrado(f"Clube com ID {id_} nao encontrado.")

    for j in lista_jogadores:
        if j.get("clube_id") == id_:
            return erro(
                f"Nao e possivel remover: o jogador '{j['nome']}' pertence a este clube."
            )

    _clubes.remove(clube)
    return ok(None, f"Clube '{clube['nome']}' removido com sucesso.")