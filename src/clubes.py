from utils import ok, criado, nao_encontrado, erro, encontrar_por_id, validar_id, carregar_dados, guardar_dados

FICHEIRO = "dados/clubes.json"
_clubes, _proximo_id = carregar_dados(FICHEIRO)

def _guardar():
    guardar_dados(FICHEIRO, _clubes, _proximo_id)


def criar_clube(nome, pais, liga, estadio=None, fundacao=None):
    global _proximo_id
    if not nome or not pais or not liga:
        return erro("Nome, pais e liga sao obrigatorios.")
    clube = {"id": _proximo_id, "nome": nome, "pais": pais, "liga": liga,
             "estadio": estadio or "", "fundacao": fundacao or ""}
    _clubes.append(clube)
    _proximo_id += 1
    _guardar()
    return criado(clube, f"Clube '{nome}' criado com sucesso.")


def listar_clubes():
    return ok(list(_clubes)) if _clubes else ok([], "Nao ha clubes registados.")


def consultar_clube(id_clube):
    id_, msg = validar_id(id_clube)
    if id_ is None:
        return erro(msg)
    clube = encontrar_por_id(_clubes, id_)
    return ok(clube) if clube else nao_encontrado(f"Clube com ID {id_} nao encontrado.")


def atualizar_clube(id_clube, nome=None, pais=None, liga=None, estadio=None, fundacao=None):
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
    _guardar()
    return ok(clube, "Clube atualizado com sucesso.")


def remover_clube(id_clube, lista_jogadores):
    id_, msg = validar_id(id_clube)
    if id_ is None:
        return erro(msg)
    clube = encontrar_por_id(_clubes, id_)
    if clube is None:
        return nao_encontrado(f"Clube com ID {id_} nao encontrado.")
    for j in lista_jogadores:
        if j.get("clube_id") == id_:
            return erro(f"Nao e possivel remover: o jogador '{j['nome']}' pertence a este clube.")
    _clubes.remove(clube)
    _guardar()
    return ok(None, f"Clube '{clube['nome']}' removido com sucesso.")
