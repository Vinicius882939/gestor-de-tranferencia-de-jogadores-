# ==============================
# empresarios.py
# CRUD de Empresarios
# ==============================

import json

FICHEIRO = "empresarios.json"

empresarios = []
proximo_id = 1


def _encontrar_empresario(id_empresario):
    for e in empresarios:
        if e["id"] == id_empresario:
            return e
    return None


# GUARDAR
def guardar_ficheiro():
    with open(FICHEIRO, "w") as f:
        json.dump(empresarios, f, indent=4)
    return (200, "Empresarios guardados com sucesso.")


# CARREGAR
def carregar_ficheiro():
    global empresarios, proximo_id
    try:
        with open(FICHEIRO, "r") as f:
            empresarios = json.load(f)
        if len(empresarios) > 0:
            proximo_id = max(e["id"] for e in empresarios) + 1
        return (200, "Empresarios carregados com sucesso.")
    except FileNotFoundError:
        return (404, "Ficheiro nao encontrado. A comecar com lista vazia.")


# CREATE
def criar_empresario(nome, licenca, email, telefone):
    global proximo_id

    if not nome or not licenca:
        return (400, "Nome e licenca sao obrigatorios.")

    empresario = {
        "id"      : proximo_id,
        "nome"    : nome,
        "licenca" : licenca,
        "email"   : email,
        "telefone": telefone
    }
    empresarios.append(empresario)
    proximo_id += 1
    return (201, "Empresario criado com sucesso.", empresario)


# READ - listar todos
def listar_empresarios():
    if len(empresarios) == 0:
        return (200, "Sem empresarios registados.", [])
    return (200, "OK", empresarios)


# READ - consultar um
def consultar_empresario(id_empresario):
    try:
        id_empresario = int(id_empresario)
    except (ValueError, TypeError):
        return (400, "ID invalido.")

    e = _encontrar_empresario(id_empresario)
    if e is None:
        return (404, "Empresario nao encontrado.")
    return (200, "OK", e)


# UPDATE
def atualizar_empresario(id_empresario, nome=None, licenca=None, email=None, telefone=None):
    try:
        id_empresario = int(id_empresario)
    except (ValueError, TypeError):
        return (400, "ID invalido.")

    e = _encontrar_empresario(id_empresario)
    if e is None:
        return (404, "Empresario nao encontrado.")

    if nome:     e["nome"]     = nome
    if licenca:  e["licenca"]  = licenca
    if email:    e["email"]    = email
    if telefone: e["telefone"] = telefone

    return (200, "Empresario atualizado com sucesso.", e)


# DELETE
def remover_empresario(id_empresario):
    try:
        id_empresario = int(id_empresario)
    except (ValueError, TypeError):
        return (400, "ID invalido.")

    e = _encontrar_empresario(id_empresario)
    if e is None:
        return (404, "Empresario nao encontrado.")

    empresarios.remove(e)
    return (200, f"Empresario '{e['nome']}' removido com sucesso.")
