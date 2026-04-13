# ==============================
# clubes.py
# CRUD de Clubes
# ==============================

clubes = []
proximo_id = 1


def _encontrar_clube(id_clube):
    for c in clubes:
        if c["id"] == id_clube:
            return c
    return None


# CREATE
def criar_clube(nome, pais, liga, estadio, fundacao):
    global proximo_id

    if not nome or not pais or not liga:
        return (400, "Nome, pais e liga sao obrigatorios.")

    clube = {
        "id"      : proximo_id,
        "nome"    : nome,
        "pais"    : pais,
        "liga"    : liga,
        "estadio" : estadio,
        "fundacao": fundacao
    }
    clubes.append(clube)
    proximo_id += 1
    return (201, "Clube criado com sucesso.", clube)


# READ - listar todos
def listar_clubes():
    if len(clubes) == 0:
        return (200, "Sem clubes registados.", [])
    return (200, "OK", clubes)


# READ - consultar um
def consultar_clube(id_clube):
    try:
        id_clube = int(id_clube)
    except (ValueError, TypeError):
        return (400, "ID invalido.")

    c = _encontrar_clube(id_clube)
    if c is None:
        return (404, "Clube nao encontrado.")
    return (200, "OK", c)


# UPDATE
def atualizar_clube(id_clube, nome=None, pais=None, liga=None, estadio=None, fundacao=None):
    try:
        id_clube = int(id_clube)
    except (ValueError, TypeError):
        return (400, "ID invalido.")

    c = _encontrar_clube(id_clube)
    if c is None:
        return (404, "Clube nao encontrado.")

    if nome:     c["nome"]     = nome
    if pais:     c["pais"]     = pais
    if liga:     c["liga"]     = liga
    if estadio:  c["estadio"]  = estadio
    if fundacao: c["fundacao"] = fundacao

    return (200, "Clube atualizado com sucesso.", c)


# DELETE
def remover_clube(id_clube, jogadores):
    try:
        id_clube = int(id_clube)
    except (ValueError, TypeError):
        return (400, "ID invalido.")

    c = _encontrar_clube(id_clube)
    if c is None:
        return (404, "Clube nao encontrado.")

    for j in jogadores:
        if j["clube_id"] == id_clube:
            return (400, f"Nao e possivel remover: o jogador '{j['nome']}' ainda pertence a este clube.")

    clubes.remove(c)
    return (200, f"Clube '{c['nome']}' removido com sucesso.")
