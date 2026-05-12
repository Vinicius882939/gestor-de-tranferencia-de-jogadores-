# ============================================
#   empresarios.py — CRUD de Empresarios
# ============================================

from utils import ok, criado, nao_encontrado, erro, encontrar_por_id, validar_id

_empresarios = []
_proximo_id = 1


# ──────────────────────────────────────────
#  CREATE
# ──────────────────────────────────────────

def criar_empresario(nome, licenca, email=None, telefone=None):
    global _proximo_id

    if not nome or not licenca:
        return erro("Nome e numero de licenca sao obrigatorios.")

    empresario = {
        "id"       : _proximo_id,
        "nome"     : nome,
        "licenca"  : licenca,
        "email"    : email or "",
        "telefone" : telefone or "",
    }
    _empresarios.append(empresario)
    _proximo_id += 1
    return criado(empresario, f"Empresario '{nome}' criado com sucesso.")


# ──────────────────────────────────────────
#  READ
# ──────────────────────────────────────────

def listar_empresarios():
    if not _empresarios:
        return ok([], "Nao ha empresarios registados.")
    return ok(list(_empresarios))


def consultar_empresario(id_empresario):
    id_, msg = validar_id(id_empresario)
    if id_ is None:
        return erro(msg)

    emp = encontrar_por_id(_empresarios, id_)
    if emp is None:
        return nao_encontrado(f"Empresario com ID {id_} nao encontrado.")
    return ok(emp)


# ──────────────────────────────────────────
#  UPDATE
# ──────────────────────────────────────────

def atualizar_empresario(id_empresario, nome=None, licenca=None,
                         email=None, telefone=None):
    id_, msg = validar_id(id_empresario)
    if id_ is None:
        return erro(msg)

    emp = encontrar_por_id(_empresarios, id_)
    if emp is None:
        return nao_encontrado(f"Empresario com ID {id_} nao encontrado.")

    if nome     is not None: emp["nome"]     = nome
    if licenca  is not None: emp["licenca"]  = licenca
    if email    is not None: emp["email"]    = email
    if telefone is not None: emp["telefone"] = telefone

    return ok(emp, "Empresario atualizado com sucesso.")


# ──────────────────────────────────────────
#  DELETE
# ──────────────────────────────────────────

def remover_empresario(id_empresario):
    id_, msg = validar_id(id_empresario)
    if id_ is None:
        return erro(msg)

    emp = encontrar_por_id(_empresarios, id_)
    if emp is None:
        return nao_encontrado(f"Empresario com ID {id_} nao encontrado.")

    _empresarios.remove(emp)
    return ok(None, f"Empresario '{emp['nome']}' removido com sucesso.")