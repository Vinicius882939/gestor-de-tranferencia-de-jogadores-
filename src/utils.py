import json
import os


def ok(dados=None, mensagem="OK"):
    return (200, mensagem, dados)

def criado(dados=None, mensagem="Criado com sucesso."):
    return (201, mensagem, dados)

def nao_encontrado(mensagem="Nao encontrado."):
    return (404, mensagem, None)

def erro(mensagem="Erro interno."):
    return (500, mensagem, None)

def encontrar_por_id(lista, id_):
    for item in lista:
        if item["id"] == int(id_):
            return item
    return None

def validar_id(valor):
    try:
        return int(valor), None
    except (ValueError, TypeError):
        return None, "ID invalido."

def separador(largura=50):
    print("-" * largura)

def carregar_dados(ficheiro):
    if not os.path.exists(ficheiro):
        return [], 1
    try:
        with open(ficheiro, "r", encoding="utf-8") as f:
            c = json.load(f)
        return c.get("dados", []), c.get("_meta", {}).get("proximo_id", 1)
    except (json.JSONDecodeError, OSError):
        return [], 1

def guardar_dados(ficheiro, lista, proximo_id):
    os.makedirs(os.path.dirname(ficheiro) or ".", exist_ok=True)
    with open(ficheiro, "w", encoding="utf-8") as f:
        json.dump({"_meta": {"proximo_id": proximo_id}, "dados": lista}, f, ensure_ascii=False, indent=2)
