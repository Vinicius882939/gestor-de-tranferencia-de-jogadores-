# ============================================
#   main.py — Menu terminal
# ============================================

from clubes        import criar_clube, listar_clubes, consultar_clube, atualizar_clube, remover_clube
from jogadores     import criar_jogador, listar_jogadores, consultar_jogador, atualizar_jogador, remover_jogador
from empresarios   import criar_empresario, listar_empresarios, consultar_empresario, atualizar_empresario, remover_empresario
from transferencias import criar_transferencia, listar_transferencias, consultar_transferencia, atualizar_transferencia, remover_transferencia


# ══════════════════════════════════════════
#  AUXILIARES DE APRESENTACAO
# ══════════════════════════════════════════

def _mostrar_clubes():
    rc = listar_clubes()
    if rc[0] == 200 and rc[2]:
        print("\n  Clubes disponiveis:")
        for c in rc[2]:
            print(f"    [{c['id']}] {c['nome']} ({c['pais']})")
    else:
        print("  (Sem clubes registados)")


def _mostrar_jogadores():
    rc = listar_jogadores()
    if rc[0] == 200 and rc[2]:
        print("\n  Jogadores disponiveis:")
        for j in rc[2]:
            print(f"    [{j['id']}] {j['nome']} ({j['posicao']})")
    else:
        print("  (Sem jogadores registados)")


def _mostrar_empresarios():
    rc = listar_empresarios()
    if rc[0] == 200 and rc[2]:
        print("\n  Empresarios disponiveis:")
        for e in rc[2]:
            print(f"    [{e['id']}] {e['nome']} | Licenca: {e['licenca']}")
    else:
        print("  (Sem empresarios registados)")


def _nome_clube(id_clube):
    if id_clube is None:
        return "Livre"
    rc = consultar_clube(id_clube)
    return rc[2]["nome"] if rc[0] == 200 else "-"


def _nome_jogador(id_jogador):
    rc = consultar_jogador(id_jogador)
    return rc[2]["nome"] if rc[0] == 200 else "-"


def _nome_empresario(id_empresario):
    if id_empresario is None:
        return "Sem empresario"
    rc = consultar_empresario(id_empresario)
    return rc[2]["nome"] if rc[0] == 200 else "-"


def _imprimir_rc(rc):
    """Imprime a mensagem de retorno independentemente do codigo."""
    print(rc[1])


# ══════════════════════════════════════════
#  CLUBES
# ══════════════════════════════════════════

def gerir_clubes():
    while True:
        print("\n===== MENU CLUBES =====")
        print("1 - Criar clube")
        print("2 - Listar clubes")
        print("3 - Consultar clube")
        print("4 - Atualizar clube")
        print("5 - Remover clube")
        print("0 - Voltar")
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            print("\n--- Criar Clube ---")
            nome     = input("Nome: ")
            pais     = input("Pais: ")
            liga     = input("Liga: ")
            estadio  = input("Estadio (enter para ignorar): ")
            fundacao = input("Ano de fundacao (enter para ignorar): ")
            rc = criar_clube(nome, pais, liga, estadio or None, fundacao or None)
            _imprimir_rc(rc)

        elif opcao == "2":
            print("\n--- Listar Clubes ---")
            rc = listar_clubes()
            if rc[0] == 200 and rc[2]:
                print(f"\n{'ID':<5} {'Nome':<20} {'Pais':<15} {'Liga':<18} {'Estadio':<18} {'Fundacao'}")
                print("-" * 85)
                for c in rc[2]:
                    print(f"{c['id']:<5} {c['nome']:<20} {c['pais']:<15} {c['liga']:<18} "
                          f"{c.get('estadio','-'):<18} {c.get('fundacao','-')}")
            else:
                _imprimir_rc(rc)

        elif opcao == "3":
            print("\n--- Consultar Clube ---")
            _mostrar_clubes()
            id_clube = input("ID do clube: ")
            rc = consultar_clube(id_clube)
            if rc[0] == 200:
                c = rc[2]
                print(f"\n  ID       : {c['id']}")
                print(f"  Nome     : {c['nome']}")
                print(f"  Pais     : {c['pais']}")
                print(f"  Liga     : {c['liga']}")
                print(f"  Estadio  : {c.get('estadio', '-')}")
                print(f"  Fundacao : {c.get('fundacao', '-')}")
            else:
                _imprimir_rc(rc)

        elif opcao == "4":
            print("\n--- Atualizar Clube ---")
            _mostrar_clubes()
            id_clube = input("ID do clube a atualizar: ")
            nome     = input("Novo nome (enter para manter): ")
            pais     = input("Novo pais (enter para manter): ")
            liga     = input("Nova liga (enter para manter): ")
            estadio  = input("Novo estadio (enter para manter): ")
            fundacao = input("Nova fundacao (enter para manter): ")
            rc = atualizar_clube(
                id_clube,
                nome     or None,
                pais     or None,
                liga     or None,
                estadio  or None,
                fundacao or None,
            )
            _imprimir_rc(rc)

        elif opcao == "5":
            print("\n--- Remover Clube ---")
            _mostrar_clubes()
            id_clube = input("ID do clube a remover: ")
            rc_j = listar_jogadores()
            lista_j = rc_j[2] if rc_j[0] == 200 else []
            rc = remover_clube(id_clube, lista_j)
            _imprimir_rc(rc)

        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


# ══════════════════════════════════════════
#  JOGADORES
# ══════════════════════════════════════════

def gerir_jogadores():
    while True:
        print("\n===== MENU JOGADORES =====")
        print("1 - Criar jogador")
        print("2 - Listar jogadores")
        print("3 - Consultar jogador")
        print("4 - Atualizar jogador")
        print("5 - Remover jogador")
        print("0 - Voltar")
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            print("\n--- Criar Jogador ---")
            nome          = input("Nome: ")
            posicao       = input("Posicao (ex: GK, ST, MF): ")
            valor         = input("Valor de mercado (M euros): ")
            nacionalidade = input("Nacionalidade (enter para ignorar): ")
            data_nasc     = input("Data de nascimento YYYY-MM-DD (enter para ignorar): ")
            _mostrar_clubes()
            clube_id_str  = input("ID do clube (enter para sem clube): ")
            clube_id      = int(clube_id_str) if clube_id_str else None
            rc = criar_jogador(nome, posicao, valor, nacionalidade or None,
                               data_nasc or None, clube_id)
            _imprimir_rc(rc)

        elif opcao == "2":
            print("\n--- Listar Jogadores ---")
            rc = listar_jogadores()
            if rc[0] == 200 and rc[2]:
                rc_c = listar_clubes()
                mapa = {c["id"]: c["nome"] for c in rc_c[2]} if rc_c[0] == 200 else {}
                print(f"\n{'ID':<5} {'Nome':<20} {'Pos':<6} {'Valor':>7}  {'Nac.':<14} {'Data Nasc.':<12} {'Clube'}")
                print("-" * 80)
                for j in rc[2]:
                    print(f"{j['id']:<5} {j['nome']:<20} {j['posicao']:<6} {j['valor']:>5.1f}M  "
                          f"{j.get('nacionalidade','-'):<14} {j.get('data_nasc','-'):<12} "
                          f"{mapa.get(j['clube_id'], 'Sem clube')}")
            else:
                _imprimir_rc(rc)

        elif opcao == "3":
            print("\n--- Consultar Jogador ---")
            _mostrar_jogadores()
            id_jogador = input("ID do jogador: ")
            rc = consultar_jogador(id_jogador)
            if rc[0] == 200:
                j = rc[2]
                rc_c = listar_clubes()
                mapa = {c["id"]: c["nome"] for c in rc_c[2]} if rc_c[0] == 200 else {}
                print(f"\n  ID            : {j['id']}")
                print(f"  Nome          : {j['nome']}")
                print(f"  Posicao       : {j['posicao']}")
                print(f"  Valor         : {j['valor']}M euros")
                print(f"  Nacionalidade : {j.get('nacionalidade', '-')}")
                print(f"  Data Nasc.    : {j.get('data_nasc', '-')}")
                print(f"  Clube         : {mapa.get(j['clube_id'], 'Sem clube')}")
            else:
                _imprimir_rc(rc)

        elif opcao == "4":
            print("\n--- Atualizar Jogador ---")
            _mostrar_jogadores()
            id_jogador    = input("ID do jogador a atualizar: ")
            nome          = input("Novo nome (enter para manter): ")
            posicao       = input("Nova posicao (enter para manter): ")
            valor         = input("Novo valor (enter para manter): ")
            nacionalidade = input("Nova nacionalidade (enter para manter): ")
            data_nasc     = input("Nova data nasc. YYYY-MM-DD (enter para manter): ")
            _mostrar_clubes()
            clube_id_str  = input("Novo clube - ID (enter para manter): ")
            clube_id      = int(clube_id_str) if clube_id_str else None
            rc = atualizar_jogador(
                id_jogador,
                nome          or None,
                posicao       or None,
                valor         or None,
                nacionalidade or None,
                data_nasc     or None,
                clube_id,
            )
            _imprimir_rc(rc)

        elif opcao == "5":
            print("\n--- Remover Jogador ---")
            _mostrar_jogadores()
            id_jogador = input("ID do jogador a remover: ")
            rc = remover_jogador(id_jogador)
            _imprimir_rc(rc)

        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


# ══════════════════════════════════════════
#  EMPRESARIOS
# ══════════════════════════════════════════

def gerir_empresarios():
    while True:
        print("\n===== MENU EMPRESARIOS =====")
        print("1 - Criar empresario")
        print("2 - Listar empresarios")
        print("3 - Consultar empresario")
        print("4 - Atualizar empresario")
        print("5 - Remover empresario")
        print("0 - Voltar")
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            print("\n--- Criar Empresario ---")
            nome     = input("Nome: ")
            licenca  = input("Numero de licenca: ")
            email    = input("Email (enter para ignorar): ")
            telefone = input("Telefone (enter para ignorar): ")
            rc = criar_empresario(nome, licenca, email or None, telefone or None)
            _imprimir_rc(rc)

        elif opcao == "2":
            print("\n--- Listar Empresarios ---")
            rc = listar_empresarios()
            if rc[0] == 200 and rc[2]:
                print(f"\n{'ID':<5} {'Nome':<20} {'Licenca':<15} {'Email':<25} {'Telefone'}")
                print("-" * 75)
                for e in rc[2]:
                    print(f"{e['id']:<5} {e['nome']:<20} {e['licenca']:<15} "
                          f"{e.get('email','-'):<25} {e.get('telefone','-')}")
            else:
                _imprimir_rc(rc)

        elif opcao == "3":
            print("\n--- Consultar Empresario ---")
            _mostrar_empresarios()
            id_emp = input("ID do empresario: ")
            rc = consultar_empresario(id_emp)
            if rc[0] == 200:
                e = rc[2]
                print(f"\n  ID       : {e['id']}")
                print(f"  Nome     : {e['nome']}")
                print(f"  Licenca  : {e['licenca']}")
                print(f"  Email    : {e.get('email', '-')}")
                print(f"  Telefone : {e.get('telefone', '-')}")
            else:
                _imprimir_rc(rc)

        elif opcao == "4":
            print("\n--- Atualizar Empresario ---")
            _mostrar_empresarios()
            id_emp   = input("ID do empresario a atualizar: ")
            nome     = input("Novo nome (enter para manter): ")
            licenca  = input("Nova licenca (enter para manter): ")
            email    = input("Novo email (enter para manter): ")
            telefone = input("Novo telefone (enter para manter): ")
            rc = atualizar_empresario(
                id_emp,
                nome     or None,
                licenca  or None,
                email    or None,
                telefone or None,
            )
            _imprimir_rc(rc)

        elif opcao == "5":
            print("\n--- Remover Empresario ---")
            _mostrar_empresarios()
            id_emp = input("ID do empresario a remover: ")
            rc = remover_empresario(id_emp)
            _imprimir_rc(rc)

        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


# ══════════════════════════════════════════
#  TRANSFERENCIAS
# ══════════════════════════════════════════

def gerir_transferencias():
    while True:
        print("\n===== MENU TRANSFERENCIAS =====")
        print("1 - Criar transferencia")
        print("2 - Listar transferencias")
        print("3 - Consultar transferencia")
        print("4 - Atualizar transferencia")
        print("5 - Remover transferencia")
        print("0 - Voltar")
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            print("\n--- Criar Transferencia ---")
            _mostrar_jogadores()
            jogador_id = input("ID do jogador: ")
            _mostrar_clubes()
            clube_origem_str  = input("ID do clube de origem (enter se jogador livre): ")
            clube_destino_str = input("ID do clube de destino: ")
            _mostrar_empresarios()
            empresario_str = input("ID do empresario (enter para nenhum): ")
            valor = input("Valor da transferencia (M euros): ")
            data  = input("Data da transferencia YYYY-MM-DD: ")
            rc = criar_transferencia(
                jogador_id,
                clube_origem_str  or None,
                clube_destino_str,
                empresario_str    or None,
                valor,
                data,
            )
            _imprimir_rc(rc)

        elif opcao == "2":
            print("\n--- Listar Transferencias ---")
            rc = listar_transferencias()
            if rc[0] == 200 and rc[2]:
                print(f"\n{'ID':<5} {'Jogador':<18} {'Origem':<14} {'Destino':<14} {'Valor':>7}  {'Data':<12} {'Estado'}")
                print("-" * 85)
                for t in rc[2]:
                    print(f"{t['id']:<5} {_nome_jogador(t['jogador_id']):<18} "
                          f"{_nome_clube(t['clube_origem_id']):<14} "
                          f"{_nome_clube(t['clube_destino_id']):<14} "
                          f"{t['valor']:>5.1f}M  {t.get('data','-'):<12} {t['estado']}")
            else:
                _imprimir_rc(rc)

        elif opcao == "3":
            print("\n--- Consultar Transferencia ---")
            rc_lista = listar_transferencias()
            if rc_lista[0] == 200 and rc_lista[2]:
                print("\n  Transferencias disponiveis:")
                for t in rc_lista[2]:
                    print(f"    [{t['id']}] {_nome_jogador(t['jogador_id'])} -> "
                          f"{_nome_clube(t['clube_destino_id'])} | {t['estado']}")
            id_t = input("ID da transferencia: ")
            rc = consultar_transferencia(id_t)
            if rc[0] == 200:
                t = rc[2]
                print(f"\n  ID            : {t['id']}")
                print(f"  Jogador       : {_nome_jogador(t['jogador_id'])}")
                print(f"  Clube origem  : {_nome_clube(t['clube_origem_id'])}")
                print(f"  Clube destino : {_nome_clube(t['clube_destino_id'])}")
                print(f"  Empresario    : {_nome_empresario(t['empresario_id'])}")
                print(f"  Valor         : {t['valor']}M euros")
                print(f"  Data          : {t.get('data', '-')}")
                print(f"  Estado        : {t['estado']}")
            else:
                _imprimir_rc(rc)

        elif opcao == "4":
            print("\n--- Atualizar Transferencia ---")
            rc_lista = listar_transferencias()
            if rc_lista[0] == 200 and rc_lista[2]:
                print("\n  Transferencias disponiveis:")
                for t in rc_lista[2]:
                    print(f"    [{t['id']}] {_nome_jogador(t['jogador_id'])} -> "
                          f"{_nome_clube(t['clube_destino_id'])} | {t['estado']}")
            id_t   = input("ID da transferencia a atualizar: ")
            valor  = input("Novo valor (enter para manter): ")
            data   = input("Nova data YYYY-MM-DD (enter para manter): ")
            print("  Estados validos: pendente / concluida / cancelada")
            estado = input("Novo estado (enter para manter): ")
            rc = atualizar_transferencia(
                id_t,
                valor  or None,
                data   or None,
                estado or None,
            )
            _imprimir_rc(rc)

        elif opcao == "5":
            print("\n--- Remover Transferencia ---")
            rc_lista = listar_transferencias()
            if rc_lista[0] == 200 and rc_lista[2]:
                print("\n  Transferencias disponiveis:")
                for t in rc_lista[2]:
                    print(f"    [{t['id']}] {_nome_jogador(t['jogador_id'])} -> "
                          f"{_nome_clube(t['clube_destino_id'])} | {t['estado']}")
            id_t = input("ID da transferencia a remover: ")
            rc = remover_transferencia(id_t)
            _imprimir_rc(rc)

        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


# ══════════════════════════════════════════
#  PROGRAMA PRINCIPAL
# ══════════════════════════════════════════

def main():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Gerir Clubes")
        print("2 - Gerir Jogadores")
        print("3 - Gerir Empresarios")
        print("4 - Gerir Transferencias")
        print("0 - Sair")
        opcao = input("Escolha uma opcao: ")

        if   opcao == "1": gerir_clubes()
        elif opcao == "2": gerir_jogadores()
        elif opcao == "3": gerir_empresarios()
        elif opcao == "4": gerir_transferencias()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()