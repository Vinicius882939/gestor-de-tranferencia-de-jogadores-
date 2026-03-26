# ============================================
#   clubes.py — CRUD de Clubes
# ============================================

clubes = []
proximo_id_clube = 1


def _linha():
    print("-" * 45)


def _encontrar_clube(id_clube):
    """Devolve o clube com esse id, ou None."""
    for c in clubes:
        if c["id"] == id_clube:
            return c
    return None


# ──────────────────────────────────────────
#  CREATE
# ──────────────────────────────────────────

def adicionar_clube():
    global proximo_id_clube

    print("\n  --- ADICIONAR CLUBE ---")
    nome  = input("  Nome do clube : ")
    pais  = input("  Pais          : ")
    liga  = input("  Liga          : ")

    clube = {
        "id"   : proximo_id_clube,
        "nome" : nome,
        "pais" : pais,
        "liga" : liga
    }

    clubes.append(clube)
    proximo_id_clube += 1
    print(f"  Clube '{nome}' adicionado! (ID: {clube['id']})")


# ──────────────────────────────────────────
#  READ
# ──────────────────────────────────────────

def listar_clubes():
    print("\n  --- LISTA DE CLUBES ---")

    if len(clubes) == 0:
        print("  Nao ha clubes registados.")
        return

    print(f"  {'ID':<5} {'Nome':<20} {'Pais':<15} {'Liga'}")
    _linha()
    for c in clubes:
        print(f"  {c['id']:<5} {c['nome']:<20} {c['pais']:<15} {c['liga']}")


def listar_clubes_resumo():
    """Versao curta para usar noutros ficheiros."""
    if len(clubes) == 0:
        print("  (Sem clubes registados)")
        return
    for c in clubes:
        print(f"    [{c['id']}] {c['nome']} ({c['pais']})")


def obter_clube(id_clube):
    """Devolve o dicionario do clube ou None."""
    return _encontrar_clube(id_clube)


# ──────────────────────────────────────────
#  UPDATE
# ──────────────────────────────────────────

def editar_clube():
    print("\n  --- EDITAR CLUBE ---")
    listar_clubes_resumo()

    try:
        id_clube = int(input("\n  ID do clube a editar: "))
    except ValueError:
        print("  ID invalido.")
        return

    clube = _encontrar_clube(id_clube)
    if clube is None:
        print("  Clube nao encontrado.")
        return

    print(f"  A editar: {clube['nome']}  (deixa em branco para nao alterar)")

    nome = input(f"  Nome [{clube['nome']}]: ")
    pais = input(f"  Pais [{clube['pais']}]: ")
    liga = input(f"  Liga [{clube['liga']}]: ")

    if nome != "": clube["nome"] = nome
    if pais != "": clube["pais"] = pais
    if liga != "": clube["liga"] = liga

    print("  Clube atualizado!")


# ──────────────────────────────────────────
#  DELETE
# ──────────────────────────────────────────

def eliminar_clube(jogadores):
    """Recebe a lista de jogadores para verificar dependencias."""
    print("\n  --- ELIMINAR CLUBE ---")
    listar_clubes_resumo()

    try:
        id_clube = int(input("\n  ID do clube a eliminar: "))
    except ValueError:
        print("  ID invalido.")
        return

    clube = _encontrar_clube(id_clube)
    if clube is None:
        print("  Clube nao encontrado.")
        return

    # Nao deixa eliminar se tiver jogadores
    for j in jogadores:
        if j["clube_id"] == id_clube:
            print(f"  Erro: o jogador '{j['nome']}' ainda pertence a este clube.")
            return

    confirmacao = input(f"  Eliminar '{clube['nome']}'? (s/n): ")
    if confirmacao.lower() == "s":
        clubes.remove(clube)
        print("  Clube eliminado!")
    else:
        print("  Operacao cancelada.")


# ──────────────────────────────────────────
#  MENU
# ──────────────────────────────────────────

def menu_clubes(jogadores):
    while True:
        print("\n=============================")
        print("       MENU — CLUBES         ")
        print("=============================")
        print("  1. Adicionar clube")
        print("  2. Listar clubes")
        print("  3. Editar clube")
        print("  4. Eliminar clube")
        print("  0. Voltar")
        _linha()
        opcao = input("  Opcao: ")

        if   opcao == "1": adicionar_clube()
        elif opcao == "2": listar_clubes()
        elif opcao == "3": editar_clube()
        elif opcao == "4": eliminar_clube(jogadores)
        elif opcao == "0": break
        else: print("  Opcao invalida!")
