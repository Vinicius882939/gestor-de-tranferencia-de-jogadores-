# ============================================
#   transferencias.py — CRUD de Transferencias
# ============================================

transferencias = []
proximo_id_transferencia = 1


def _linha():
    print("-" * 45)


def _encontrar_transferencia(id_t):
    """Devolve a transferencia com esse id, ou None."""
    for t in transferencias:
        if t["id"] == id_t:
            return t
    return None


def _nome_clube(clubes, id_clube):
    """Devolve o nome do clube pelo id."""
    for c in clubes:
        if c["id"] == id_clube:
            return c["nome"]
    return "Livre"


def _nome_empresario(empresarios, id_emp):
    """Devolve o nome do empresario pelo id."""
    for e in empresarios:
        if e["id"] == id_emp:
            return e["nome"]
    return "Sem empresario"


# ──────────────────────────────────────────
#  CREATE
# ──────────────────────────────────────────

def adicionar_transferencia(jogadores, clubes, empresarios):
    global proximo_id_transferencia

    print("\n  --- REGISTAR TRANSFERENCIA ---")

    if len(jogadores) == 0:
        print("  Nao ha jogadores registados.")
        return
    if len(clubes) == 0:
        print("  Nao ha clubes registados.")
        return

    # Escolher jogador
    print("\n  Jogadores disponiveis:")
    for j in jogadores:
        nome_clube = _nome_clube(clubes, j["clube_id"])
        print(f"    [{j['id']}] {j['nome']} ({j['posicao']}) — {nome_clube}")

    try:
        id_jogador = int(input("\n  ID do jogador: "))
    except ValueError:
        print("  ID invalido.")
        return

    jogador = None
    for j in jogadores:
        if j["id"] == id_jogador:
            jogador = j
            break

    if jogador is None:
        print("  Jogador nao encontrado.")
        return

    # Clube de destino
    print("\n  Clubes disponiveis:")
    for c in clubes:
        print(f"    [{c['id']}] {c['nome']} ({c['pais']})")

    try:
        id_destino = int(input("\n  ID do clube de destino: "))
    except ValueError:
        print("  ID invalido.")
        return

    clube_destino = None
    for c in clubes:
        if c["id"] == id_destino:
            clube_destino = c
            break

    if clube_destino is None:
        print("  Clube nao encontrado.")
        return

    if jogador["clube_id"] == id_destino:
        print("  O jogador ja pertence a esse clube.")
        return

    # Empresario (opcional)
    empresario_id = None
    if len(empresarios) > 0:
        print("\n  Empresarios disponiveis:")
        for e in empresarios:
            print(f"    [{e['id']}] {e['nome']}")
        entrada = input("  ID do empresario (ENTER = nenhum): ")
        if entrada != "":
            try:
                eid = int(entrada)
                for e in empresarios:
                    if e["id"] == eid:
                        empresario_id = eid
                        break
            except ValueError:
                pass

    # Valor e data
    try:
        valor = float(input("  Valor da transferencia (M euros): "))
    except ValueError:
        print("  Valor invalido. A usar 0.")
        valor = 0.0

    data = input("  Data (DD/MM/AAAA): ")

    transferencia = {
        "id"               : proximo_id_transferencia,
        "jogador_id"       : id_jogador,
        "clube_origem_id"  : jogador["clube_id"],   # guarda de onde vem
        "clube_destino_id" : id_destino,
        "empresario_id"    : empresario_id,
        "valor"            : valor,
        "data"             : data,
        "estado"           : "pendente"
    }

    transferencias.append(transferencia)
    proximo_id_transferencia += 1
    print(f"  Transferencia registada com sucesso! (ID: {transferencia['id']})")


# ──────────────────────────────────────────
#  READ
# ──────────────────────────────────────────

def listar_transferencias(jogadores, clubes, empresarios):
    print("\n  --- LISTA DE TRANSFERENCIAS ---")

    if len(transferencias) == 0:
        print("  Nao ha transferencias registadas.")
        return

    print(f"  {'ID':<5} {'Jogador':<16} {'Origem':<14} {'Destino':<14} {'Valor':>7}  {'Data':<12} {'Estado'}")
    _linha()
    for t in transferencias:
        # Encontra nomes
        nome_j = "?"
        for j in jogadores:
            if j["id"] == t["jogador_id"]:
                nome_j = j["nome"]
                break

        nome_o = _nome_clube(clubes, t["clube_origem_id"])
        nome_d = _nome_clube(clubes, t["clube_destino_id"])

        print(f"  {t['id']:<5} {nome_j:<16} {nome_o:<14} {nome_d:<14} "
              f"{t['valor']:>5.1f}M  {t['data']:<12} {t['estado']}")


def ver_transferencia(jogadores, clubes, empresarios):
    print("\n  --- DETALHES DA TRANSFERENCIA ---")
    _listar_resumo()

    try:
        id_t = int(input("\n  ID da transferencia: "))
    except ValueError:
        print("  ID invalido.")
        return

    t = _encontrar_transferencia(id_t)
    if t is None:
        print("  Transferencia nao encontrada.")
        return

    nome_j = "?"
    for j in jogadores:
        if j["id"] == t["jogador_id"]:
            nome_j = j["nome"]
            break

    nome_emp = _nome_empresario(empresarios, t["empresario_id"])

    print()
    _linha()
    print(f"  ID            : {t['id']}")
    print(f"  Jogador       : {nome_j}")
    print(f"  Clube origem  : {_nome_clube(clubes, t['clube_origem_id'])}")
    print(f"  Clube destino : {_nome_clube(clubes, t['clube_destino_id'])}")
    print(f"  Empresario    : {nome_emp}")
    print(f"  Valor         : {t['valor']}M euros")
    print(f"  Data          : {t['data']}")
    print(f"  Estado        : {t['estado']}")
    _linha()


def _listar_resumo():
    """Versao curta para usar dentro do ficheiro."""
    if len(transferencias) == 0:
        print("  (Sem transferencias registadas)")
        return
    for t in transferencias:
        print(f"    [{t['id']}] Jogador ID {t['jogador_id']} -> Clube ID {t['clube_destino_id']} | {t['valor']}M | {t['estado']}")


# ──────────────────────────────────────────
#  UPDATE
# ──────────────────────────────────────────

def editar_transferencia():
    """Permite editar valor e data de uma transferencia pendente."""
    print("\n  --- EDITAR TRANSFERENCIA ---")
    _listar_resumo()

    try:
        id_t = int(input("\n  ID da transferencia a editar: "))
    except ValueError:
        print("  ID invalido.")
        return

    t = _encontrar_transferencia(id_t)
    if t is None:
        print("  Transferencia nao encontrada.")
        return

    if t["estado"] != "pendente":
        print(f"  So e possivel editar transferencias pendentes (estado atual: {t['estado']}).")
        return

    print("  (Deixa em branco para nao alterar)")
    valor_str = input(f"  Valor [{t['valor']}]: ")
    data      = input(f"  Data  [{t['data']}]: ")

    if valor_str != "":
        try:
            t["valor"] = float(valor_str)
        except ValueError:
            print("  Valor invalido, nao foi alterado.")
    if data != "":
        t["data"] = data

    print("  Transferencia atualizada!")


def concluir_transferencia(jogadores):
    """Conclui a transferencia e move o jogador para o clube destino."""
    print("\n  --- CONCLUIR TRANSFERENCIA ---")

    pendentes = [t for t in transferencias if t["estado"] == "pendente"]
    if len(pendentes) == 0:
        print("  Nao ha transferencias pendentes.")
        return

    for t in pendentes:
        print(f"    [{t['id']}] Jogador ID {t['jogador_id']} -> Clube ID {t['clube_destino_id']} | {t['valor']}M")

    try:
        id_t = int(input("\n  ID da transferencia a concluir: "))
    except ValueError:
        print("  ID invalido.")
        return

    t = _encontrar_transferencia(id_t)
    if t is None or t["estado"] != "pendente":
        print("  Transferencia nao encontrada ou nao esta pendente.")
        return

    # Move o jogador para o clube destino
    for j in jogadores:
        if j["id"] == t["jogador_id"]:
            j["clube_id"] = t["clube_destino_id"]
            break

    t["estado"] = "concluida"
    print(f"  Transferencia {id_t} concluida! Jogador movido para o clube destino.")


def cancelar_transferencia():
    print("\n  --- CANCELAR TRANSFERENCIA ---")

    pendentes = [t for t in transferencias if t["estado"] == "pendente"]
    if len(pendentes) == 0:
        print("  Nao ha transferencias pendentes.")
        return

    for t in pendentes:
        print(f"    [{t['id']}] Jogador ID {t['jogador_id']} -> Clube ID {t['clube_destino_id']} | {t['valor']}M")

    try:
        id_t = int(input("\n  ID da transferencia a cancelar: "))
    except ValueError:
        print("  ID invalido.")
        return

    t = _encontrar_transferencia(id_t)
    if t is None or t["estado"] != "pendente":
        print("  Transferencia nao encontrada ou nao esta pendente.")
        return

    t["estado"] = "cancelada"
    print("  Transferencia cancelada!")


# ──────────────────────────────────────────
#  DELETE
# ──────────────────────────────────────────

def eliminar_transferencia():
    print("\n  --- ELIMINAR TRANSFERENCIA ---")
    _listar_resumo()

    try:
        id_t = int(input("\n  ID da transferencia a eliminar: "))
    except ValueError:
        print("  ID invalido.")
        return

    t = _encontrar_transferencia(id_t)
    if t is None:
        print("  Transferencia nao encontrada.")
        return

    if t["estado"] == "pendente":
        print("  Nao podes eliminar uma transferencia pendente. Cancela primeiro.")
        return

    confirmacao = input(f"  Eliminar transferencia {id_t}? (s/n): ")
    if confirmacao.lower() == "s":
        transferencias.remove(t)
        print("  Transferencia eliminada!")
    else:
        print("  Operacao cancelada.")


# ──────────────────────────────────────────
#  MENU
# ──────────────────────────────────────────

def menu_transferencias(jogadores, clubes, empresarios):
    while True:
        print("\n=============================")
        print("   MENU — TRANSFERENCIAS     ")
        print("=============================")
        print("  1. Registar transferencia")
        print("  2. Listar transferencias")
        print("  3. Ver detalhes")
        print("  4. Editar transferencia")
        print("  5. Concluir transferencia")
        print("  6. Cancelar transferencia")
        print("  7. Eliminar transferencia")
        print("  0. Voltar")
        _linha()
        opcao = input("  Opcao: ")

        if   opcao == "1": adicionar_transferencia(jogadores, clubes, empresarios)
        elif opcao == "2": listar_transferencias(jogadores, clubes, empresarios)
        elif opcao == "3": ver_transferencia(jogadores, clubes, empresarios)
        elif opcao == "4": editar_transferencia()
        elif opcao == "5": concluir_transferencia(jogadores)
        elif opcao == "6": cancelar_transferencia()
        elif opcao == "7": eliminar_transferencia()
        elif opcao == "0": break
        else: print("  Opcao invalida!")
