# ============================================
#   empresarios.py — CRUD de Empresarios
# ============================================

empresarios = []
proximo_id_empresario = 1


def _linha():
    print("-" * 45)


def _encontrar_empresario(id_empresario):
    """Devolve o empresario com esse id, ou None."""
    for e in empresarios:
        if e["id"] == id_empresario:
            return e
    return None


# ──────────────────────────────────────────
#  CREATE
# ──────────────────────────────────────────

def adicionar_empresario():
    global proximo_id_empresario

    print("\n  --- ADICIONAR EMPRESARIO ---")
    nome    = input("  Nome          : ")
    licenca = input("  Nr. de licenca: ")
    email   = input("  Email         : ")
    telefone = input("  Telefone      : ")

    empresario = {
        "id"       : proximo_id_empresario,
        "nome"     : nome,
        "licenca"  : licenca,
        "email"    : email,
        "telefone" : telefone
    }

    empresarios.append(empresario)
    proximo_id_empresario += 1
    print(f"  Empresario '{nome}' adicionado! (ID: {empresario['id']})")


# ──────────────────────────────────────────
#  READ
# ──────────────────────────────────────────

def listar_empresarios():
    print("\n  --- LISTA DE EMPRESARIOS ---")

    if len(empresarios) == 0:
        print("  Nao ha empresarios registados.")
        return

    print(f"  {'ID':<5} {'Nome':<20} {'Licenca':<14} {'Email':<22} {'Telefone'}")
    _linha()
    for e in empresarios:
        print(f"  {e['id']:<5} {e['nome']:<20} {e['licenca']:<14} {e['email']:<22} {e['telefone']}")


def listar_empresarios_resumo():
    """Versao curta para usar noutros ficheiros."""
    if len(empresarios) == 0:
        print("  (Sem empresarios registados)")
        return
    for e in empresarios:
        print(f"    [{e['id']}] {e['nome']}  |  Licenca: {e['licenca']}")


def obter_empresario(id_empresario):
    """Devolve o dicionario do empresario ou None."""
    return _encontrar_empresario(id_empresario)


# ──────────────────────────────────────────
#  UPDATE
# ──────────────────────────────────────────

def editar_empresario():
    print("\n  --- EDITAR EMPRESARIO ---")
    listar_empresarios_resumo()

    try:
        id_emp = int(input("\n  ID do empresario a editar: "))
    except ValueError:
        print("  ID invalido.")
        return

    emp = _encontrar_empresario(id_emp)
    if emp is None:
        print("  Empresario nao encontrado.")
        return

    print(f"  A editar: {emp['nome']}  (deixa em branco para nao alterar)")

    nome     = input(f"  Nome     [{emp['nome']}]: ")
    licenca  = input(f"  Licenca  [{emp['licenca']}]: ")
    email    = input(f"  Email    [{emp['email']}]: ")
    telefone = input(f"  Telefone [{emp['telefone']}]: ")

    if nome     != "": emp["nome"]     = nome
    if licenca  != "": emp["licenca"]  = licenca
    if email    != "": emp["email"]    = email
    if telefone != "": emp["telefone"] = telefone

    print("  Empresario atualizado!")


# ──────────────────────────────────────────
#  DELETE
# ──────────────────────────────────────────

def eliminar_empresario():
    print("\n  --- ELIMINAR EMPRESARIO ---")
    listar_empresarios_resumo()

    try:
        id_emp = int(input("\n  ID do empresario a eliminar: "))
    except ValueError:
        print("  ID invalido.")
        return

    emp = _encontrar_empresario(id_emp)
    if emp is None:
        print("  Empresario nao encontrado.")
        return

    confirmacao = input(f"  Eliminar '{emp['nome']}'? (s/n): ")
    if confirmacao.lower() == "s":
        empresarios.remove(emp)
        print("  Empresario eliminado!")
    else:
        print("  Operacao cancelada.")


# ──────────────────────────────────────────
#  MENU
# ──────────────────────────────────────────

def menu_empresarios():
    while True:
        print("\n=============================")
        print("     MENU — EMPRESARIOS      ")
        print("=============================")
        print("  1. Adicionar empresario")
        print("  2. Listar empresarios")
        print("  3. Editar empresario")
        print("  4. Eliminar empresario")
        print("  0. Voltar")
        _linha()
        opcao = input("  Opcao: ")

        if   opcao == "1": adicionar_empresario()
        elif opcao == "2": listar_empresarios()
        elif opcao == "3": editar_empresario()
        elif opcao == "4": eliminar_empresario()
        elif opcao == "0": break
        else: print("  Opcao invalida!")
