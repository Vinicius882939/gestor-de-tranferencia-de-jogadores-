# ============================================
#   jogadores.py — CRUD de Jogadores
# ============================================

from utils import ok, criado, nao_encontrado, erro, encontrar_por_id, validar_id

_jogadores = []
_proximo_id = 1


# ──────────────────────────────────────────
#  CREATE
# ──────────────────────────────────────────

def criar_jogador(nome, posicao, valor, nacionalidade=None,
                  data_nasc=None, clube_id=None):
    global _proximo_id

    if not nome or not posicao:
        return erro("Nome e posicao sao obrigatorios.")

    try:
        valor = float(valor)
    except (ValueError, TypeError):
        return erro("Valor de mercado invalido.")

    jogador = {
        "id"           : _proximo_id,
        "nome"         : nome,
        "posicao"      : posicao,
        "valor"        : valor,
        "nacionalidade": nacionalidade or "",
        "data_nasc"    : data_nasc or "",
        "clube_id"     : int(clube_id) if clube_id is not None else None,
    }
    _jogadores.append(jogador)
    _proximo_id += 1
    return criado(jogador, f"Jogador '{nome}' criado com sucesso.")


# ──────────────────────────────────────────
#  READ
# ──────────────────────────────────────────

def listar_jogadores():
    if not _jogadores:
        return ok([], "Nao ha jogadores registados.")
    return ok(list(_jogadores))


def consultar_jogador(id_jogador):
    id_, msg = validar_id(id_jogador)
    if id_ is None:
        return erro(msg)

    jogador = encontrar_por_id(_jogadores, id_)
    if jogador is None:
        return nao_encontrado(f"Jogador com ID {id_} nao encontrado.")
    return ok(jogador)


# ──────────────────────────────────────────
#  UPDATE
# ──────────────────────────────────────────

def atualizar_jogador(id_jogador, nome=None, posicao=None, valor=None,
                      nacionalidade=None, data_nasc=None, clube_id=None):
    id_, msg = validar_id(id_jogador)
    if id_ is None:
        return erro(msg)

    jogador = encontrar_por_id(_jogadores, id_)
    if jogador is None:
        return nao_encontrado(f"Jogador com ID {id_} nao encontrado.")

    if nome          is not None: jogador["nome"]          = nome
    if posicao       is not None: jogador["posicao"]       = posicao
    if nacionalidade is not None: jogador["nacionalidade"] = nacionalidade
    if data_nasc     is not None: jogador["data_nasc"]     = data_nasc
    if valor is not None:
        try:
            jogador["valor"] = float(valor)
        except (ValueError, TypeError):
            return erro("Valor de mercado invalido.")
    if clube_id is not None:
        jogador["clube_id"] = int(clube_id) if clube_id != "" else None

    return ok(jogador, "Jogador atualizado com sucesso.")


# ──────────────────────────────────────────
#  DELETE
# ──────────────────────────────────────────

def remover_jogador(id_jogador):
    id_, msg = validar_id(id_jogador)
    if id_ is None:
        return erro(msg)

    jogador = encontrar_por_id(_jogadores, id_)
    if jogador is None:
        return nao_encontrado(f"Jogador com ID {id_} nao encontrado.")

    _jogadores.remove(jogador)
    return ok(None, f"Jogador '{jogador['nome']}' removido com sucesso.")