# ============================================
#   jogadores.py — CRUD de Jogadores
# ============================================

jogadores = []
proximo_id_jogador = 1


def _linha():
    print("-" * 45)


def _encontrar_jogador(id_jogador):
    """Devolve o jogador com esse id, ou None."""
    for j in jogadores:
        if j["id"] == id_jogador:
            return j
    return None


# ──────────────────────────────────────────
#  CREATE
# ──────────────────────────────────────────

def adicionar_jogador(clubes, empresarios):
    """
    Recebe as listas de clubes e empresarios
    para o utilizador poder escolher.
    """
    global proximo_id_jogador

    print("\n  --- ADICIONAR JOGADOR ---")

    nome          = input("  Nome          : ")
    nacionalidade = input("  Nacionalidade : ")
    posicao       = input("  Posicao       : ")

    try:
        valor = float(input("  Valor mercado (M euros): "))
    except ValueError:
        print("  Valor invalido. A usar 0.")
        valor = 0.0

    # Escolher clube
    clube_id = None
    if len(clubes) > 0:
        print("\n  Clubes disponiveis:")
        for c in clubes:
            print(f"    [{c['id']}] {c['nome']}")
        entrada = input("  ID do clube (ENTER = sem clube): ")
        if entrada != "":
            try:
                cid = int(entrada)
                for c in clubes:
                    if c["id"] == cid:
                        clube_id = cid
                        break
                if clube_id is None:
                    print("  Clube nao encontrado. Jogador ficara sem clube.")
            except ValueError:
                pass
    else:
        print("  (Sem clubes registados)")

    # Escolher empresario
    empresario_id = None
    if len(empresarios) > 0:
        print("\n  Empresarios disponiveis:")
        for e in empresarios:
            print(f"    [{e['id']}] {e['nome']}")
        entrada = input("  ID do empresario (ENTER = sem empresario): ")
        if entrada != "":
            try:
                eid = int(entrada)
                for e in empresarios:
                    if e["id"] == eid:
                        empresario_id = eid
                        break
                if empresario_id is None:
                    print("  Empresario nao encontrado.")
            except ValueError:
                pass
    else:
        print("  (Sem empresarios registados)")

    jogador = {
        "id"            : proximo_id_jogador,
        "nome"          : nome,
        "nacionalidade" : nacionalidade,
        "posicao"       : posicao,
        "valor"         : valor,
        "clube_id"      : clube_id,
        "empresario_id" : empresario_id
    }

    jogadores.append(jogador)
    proximo_id_jogador += 1
    print(f"  Jogador '{nome}' adicionado! (ID: {jogador['id']})")


# ──────────────────────────────────────────
#  READ
# ──────────────────────────────────────────

def listar_jogadores(clubes, empresarios):
    print("\n  --- LISTA DE JOGADORES ---")

    if len(jogadores) == 0:
        print("  Nao ha jogadores registados.")
        return

    print(f"  {'ID':<5} {'Nome':<18} {'Pos':<5} {'Valor':>7}  {'Clube':<18} {'Empresario'}")
    _linha()
    for j in jogadores:
        # Procura nome do clube
        nome_clube = "Sem clube"
        for c in clubes:
            if c["id"] == j["clube_id"]:
                nome_clube = c["nome"]
                break

        # Procura nome do empresario
        nome_emp = "Sem empresario"
        for e in empresarios:
            if e["id"] == j["empresario_id"]:
                nome_emp = e["nome"]
                break

        print(f"  {j['id']:<5} {j['nome']:<18} {j['posicao']:<5} {j['valor']:>5.1f}M  {nome_clube:<18} {nome_emp}")


def ver_jogador(clubes, empresarios):
    print("\n  --- DETALHES DO JOGADOR ---")
    listar_jogadores_resumo()

    try:
        id_j = int(input("\n  ID do jogador: "))
    except ValueError:
        print("  ID invalido.")
        return

    j = _encontrar_jogador(id_j)
    if j is None:
        print("  Jogador nao encontrado.")
        return

    nome_clube = "Sem clube"
    for c in clubes:
        if c["id"] == j["clube_id"]:
            nome_clube = c["nome"]
            break

    nome_emp = "Sem empresario"
    for e in empresarios:
        if e["id"] == j["empresario_id"]:
            nome_emp = e["nome"]
            break

    print()
    _linha()
    print(f"  ID            : {j['id']}")
    print(f"  Nome          : {j['nome']}")
    print(f"  Nacionalidade : {j['nacionalidade']}")
    print(f"  Posicao       : {j['posicao']}")
    print(f"  Valor mercado : {j['valor']}M euros")
    print(f"  Clube         : {nome_clube}")
    print(f"  Empresario    : {nome_emp}")
    _linha()


def listar_jogadores_resumo():
    """Versao curta para usar noutros ficheiros."""
    if len(jogadores) == 0:
        print("  (Sem jogadores registados)")
        return
    for j in jogadores:
        print(f"    [{j['id']}] {j['nome']} ({j['posicao']})")


def obter_jogador(id_jogador):
    """Devolve o dicionario do jogador ou None."""
    return _encontrar_jogador(id_jogador)


# ──────────────────────────────────────────
#  UPDATE
# ──────────────────────────────────────────

def editar_jogador():
    print("\n  --- EDITAR JOGADOR ---")
    listar_jogadores_resumo()

    try:
        id_j = int(input("\n  ID do jogador a editar: "))
    except ValueError:
        print("  ID invalido.")
        return

    j = _encontrar_jogador(id_j)
    if j is None:
        print("  Jogador nao encontrado.")
        return

    print(f"  A editar: {j['nome']}  (deixa em branco para nao alterar)")

    nome          = input(f"  Nome          [{j['nome']}]: ")
    nacionalidade = input(f"  Nacionalidade [{j['nacionalidade']}]: ")
    posicao       = input(f"  Posicao       [{j['posicao']}]: ")
    valor_str     = input(f"  Valor         [{j['valor']}]: ")

    if nome          != "": j["nome"]          = nome
    if nacionalidade != "": j["nacionalidade"] = nacionalidade
    if posicao       != "": j["posicao"]       = posicao
    if valor_str     != "":
        try:
            j["valor"] = float(valor_str)
        except ValueError:
            print("  Valor invalido, nao foi alterado.")

    print("  Jogador atualizado!")


# ──────────────────────────────────────────
#  DELETE
# ──────────────────────────────────────────

def eliminar_jogador(transferencias):
    """Recebe a lista de transferencias para verificar dependencias."""
    print("\n  --- ELIMINAR JOGADOR ---")
    listar_jogadores_resumo()

    try:
        id_j = int(input("\n  ID do jogador a eliminar: "))
    except ValueError:
        print("  ID invalido.")
        return

    j = _encontrar_jogador(id_j)
    if j is None:
        print("  Jogador nao encontrado.")
        return

    # Nao deixa eliminar se tiver transferencias pendentes
    for t in transferencias:
        if t["jogador_id"] == id_j and t["estado"] == "pendente":
            print("  Erro: jogador tem transferencias pendentes. Cancela primeiro.")
            return

    confirmacao = input(f"  Eliminar '{j['nome']}'? (s/n): ")
    if confirmacao.lower() == "s":
        jogadores.remove(j)
        print("  Jogador eliminado!")
    else:
        print("  Operacao cancelada.")


# ──────────────────────────────────────────
#  MENU
# ──────────────────────────────────────────

def menu_jogadores(clubes, empresarios, transferencias):
    while True:
        print("\n=============================")
        print("      MENU — JOGADORES       ")
        print("=============================")
        print("  1. Adicionar jogador")
        print("  2. Listar jogadores")
        print("  3. Ver detalhes")
        print("  4. Editar jogador")
        print("  5. Eliminar jogador")
        print("  0. Voltar")
        _linha()
        opcao = input("  Opcao: ")

        if   opcao == "1": adicionar_jogador(clubes, empresarios)
        elif opcao == "2": listar_jogadores(clubes, empresarios)
        elif opcao == "3": ver_jogador(clubes, empresarios)
        elif opcao == "4": editar_jogador()
        elif opcao == "5": eliminar_jogador(transferencias)
        elif opcao == "0": break
        else: print("  Opcao invalida!")
