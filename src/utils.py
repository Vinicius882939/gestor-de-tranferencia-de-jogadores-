# ============================================
#   utils.py — Utilitarios partilhados
# ============================================


def ok(dados=None, mensagem="OK"):
    """Resposta de sucesso sem criacao (200)."""
    return (200, mensagem, dados)


def criado(dados=None, mensagem="Criado com sucesso."):
    """Resposta de criacao bem-sucedida (201)."""
    return (201, mensagem, dados)


def nao_encontrado(mensagem="Nao encontrado."):
    """Entidade nao existe (404)."""
    return (404, mensagem, None)


def erro(mensagem="Erro interno."):
    """Erro generico (500)."""
    return (500, mensagem, None)


def encontrar_por_id(lista, id_):
    """Devolve o primeiro elemento da lista cujo campo 'id' == id_, ou None."""
    id_ = int(id_)
    for item in lista:
        if item["id"] == id_:
            return item
    return None


def validar_id(valor):
    """
    Tenta converter valor para int.
    Devolve (int, None) em caso de sucesso ou (None, mensagem_erro) se falhar.
    """
    try:
        return int(valor), None
    except (ValueError, TypeError):
        return None, "ID invalido."


def separador(largura=50):
    """Imprime uma linha separadora."""
    print("-" * largura)