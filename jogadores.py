# ==============================
# jogadores.py
# CRUD de Jogadores
# ==============================

jogadores = []
proximo_id = 1


def _encontrar_jogador(id_jogador):
    for j in jogadores:
        if j["id"] == id_jogador:
            return j
    return None


# CREATE
def criar_jogador(nome, posicao, valor, nacionalidade, data_nasc, clube_id=None):
    global proximo_id

    if not nome or not posicao:
        return (400, "Nome e posicao sao obrigatorios.")

    try:
        valor = float(valor)
    except (ValueError, TypeError):
        return (400, "Valor de mercado invalido.")

    jogador = {
        "id"           : proximo_id,
        "nome"         : nome,
        "posicao"      : posicao,
        "valor"        : valor,
        "nacionalidade": nacionalidade,
        "data_nasc"    : data_nasc,
        "clube_id"     : int(clube_id) if clube_id else None
    }
    jogadores.append(jogador)
    proximo_id += 1
    return (201, "Jogador criado com sucesso.", jogador)


# READ - listar todos
def listar_jogadores():
    if len(jogadores) == 0:
        return (200, "Sem jogadores registados.", [])
    return (200, "OK", jogadores)


# READ - consultar um
def consultar_jogador(id_jogador):
    try:
        id_jogador = int(id_jogador)
    except (ValueError, TypeError):
        return (400, "ID invalido.")

    j = _encontrar_jogador(id_jogador)
    if j is None:
        return (404, "Jogador nao encontrado.")
    return (200, "OK", j)


# UPDATE
def atualizar_jogador(id_jogador, nome=None, posicao=None, valor=None,
                      nacionalidade=None, data_nasc=None, clube_id=None):
    try:
        id_jogador = int(id_jogador)
    except (ValueError, TypeError):
        return (400, "ID invalido.")

    j = _encontrar_jogador(id_jogador)
    if j is None:
        return (404, "Jogador nao encontrado.")

    if nome:          j["nome"]          = nome
    if posicao:       j["posicao"]       = posicao
    if nacionalidade: j["nacionalidade"] = nacionalidade
    if data_nasc:     j["data_nasc"]     = data_nasc
    if valor:
        try:
            j["valor"] = float(valor)
        except ValueError:
            return (400, "Valor invalido.")
    if clube_id is not None:
        j["clube_id"] = int(clube_id) if clube_id != "" else None

    return (200, "Jogador atualizado com sucesso.", j)


# DELETE
def remover_jogador(id_jogador):
    try:
        id_jogador = int(id_jogador)
    except (ValueError, TypeError):
        return (400, "ID invalido.")

    j = _encontrar_jogador(id_jogador)
    if j is None:
        return (404, "Jogador nao encontrado.")

    jogadores.remove(j)
    return (200, f"Jogador '{j['nome']}' removido com sucesso.")
