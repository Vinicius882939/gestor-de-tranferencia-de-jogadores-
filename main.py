# ==============================
# main.py
# menu terminal para testar CRUD
# ==============================

from clubes import (
    criar_clube,
    listar_clubes,
    consultar_clube,
    atualizar_clube,
    remover_clube
)
from jogadores import (
    criar_jogador,
    listar_jogadores,
    consultar_jogador,
    atualizar_jogador,
    remover_jogador
)


# ==============================
# MENUS
# ==============================

def menu_principal():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Gerir Clubes")
    print("2 - Gerir Jogadores")
    print("0 - Sair")


def menu_clubes():
    print("\n===== MENU CLUBES =====")
    print("1 - Criar clube")
    print("2 - Listar clubes")
    print("3 - Consultar clube")
    print("4 - Atualizar clube")
    print("5 - Remover clube")
    print("0 - Voltar")


def menu_jogadores():
    print("\n===== MENU JOGADORES =====")
    print("1 - Criar jogador")
    print("2 - Listar jogadores")
    print("3 - Consultar jogador")
    print("4 - Atualizar jogador")
    print("5 - Remover jogador")
    print("0 - Voltar")


# ==============================
# AUXILIAR — mostrar lista de clubes
# ==============================

def _mostrar_clubes():
    return_code = listar_clubes()
    if return_code[0] == 200 and len(return_code[2]) > 0:
        print("\n  Clubes disponiveis:")
        for c in return_code[2]:
            print(f"    [{c['id']}] {c['nome']} ({c['pais']})")
    else:
        print("  (Sem clubes registados)")


# ==============================
# LOGICA DE CLUBES
# ==============================

def gerir_clubes():
    while True:
        menu_clubes()
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            print("\n--- Criar Clube ---")
            nome     = input("Nome: ")
            pais     = input("Pais: ")
            liga     = input("Liga: ")
            estadio  = input("Estadio (enter para ignorar): ")
            fundacao = input("Ano de fundacao (enter para ignorar): ")

            return_code = criar_clube(nome, pais, liga, estadio, fundacao)
            if return_code[0] == 201:
                print("Clube criado com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "2":
            print("\n--- Listar Clubes ---")
            return_code = listar_clubes()
            if return_code[0] == 200:
                if len(return_code[2]) == 0:
                    print(return_code[1])
                else:
                    print(f"{'ID':<5} {'Nome':<20} {'Pais':<15} {'Liga':<18} {'Estadio':<18} {'Fundacao'}")
                    print("-" * 85)
                    for c in return_code[2]:
                        print(f"{c['id']:<5} {c['nome']:<20} {c['pais']:<15} {c['liga']:<18} {c.get('estadio','-'):<18} {c.get('fundacao','-')}")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "3":
            print("\n--- Consultar Clube ---")
            _mostrar_clubes()
            id_clube = input("ID do clube: ")

            return_code = consultar_clube(id_clube)
            if return_code[0] == 200:
                c = return_code[2]
                print("\n  Detalhes do clube:")
                print(f"    ID       : {c['id']}")
                print(f"    Nome     : {c['nome']}")
                print(f"    Pais     : {c['pais']}")
                print(f"    Liga     : {c['liga']}")
                print(f"    Estadio  : {c.get('estadio', '-')}")
                print(f"    Fundacao : {c.get('fundacao', '-')}")
            elif return_code[0] == 404:
                print("Clube nao encontrado.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "4":
            print("\n--- Atualizar Clube ---")
            _mostrar_clubes()
            id_clube = input("ID do clube a atualizar: ")
            nome     = input("Novo nome (enter para manter): ")
            pais     = input("Novo pais (enter para manter): ")
            liga     = input("Nova liga (enter para manter): ")
            estadio  = input("Novo estadio (enter para manter): ")
            fundacao = input("Nova fundacao (enter para manter): ")

            return_code = atualizar_clube(
                id_clube,
                nome     if nome     else None,
                pais     if pais     else None,
                liga     if liga     else None,
                estadio  if estadio  else None,
                fundacao if fundacao else None
            )
            if return_code[0] == 200:
                print("Clube atualizado com sucesso.")
            elif return_code[0] == 404:
                print("Clube nao encontrado.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "5":
            print("\n--- Remover Clube ---")
            _mostrar_clubes()
            id_clube = input("ID do clube a remover: ")

            rc_j = listar_jogadores()
            lista_jogadores = rc_j[2] if rc_j[0] == 200 else []

            return_code = remover_clube(id_clube, lista_jogadores)
            if return_code[0] == 200:
                print("Clube removido com sucesso.")
            elif return_code[0] == 404:
                print("Clube nao encontrado.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "0":
            break

        else:
            print("Opcao invalida.")


# ==============================
# LOGICA DE JOGADORES
# ==============================

def gerir_jogadores():
    while True:
        menu_jogadores()
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            print("\n--- Criar Jogador ---")
            nome          = input("Nome: ")
            posicao       = input("Posicao (ex: GK, ST, MF): ")
            valor         = input("Valor de mercado (M euros): ")
            nacionalidade = input("Nacionalidade (enter para ignorar): ")
            data_nasc     = input("Data de nascimento YYYY-MM-DD (enter para ignorar): ")

            _mostrar_clubes()
            clube_id_str = input("ID do clube (enter para sem clube): ")
            clube_id = int(clube_id_str) if clube_id_str else None

            return_code = criar_jogador(nome, posicao, valor, nacionalidade, data_nasc, clube_id)
            if return_code[0] == 201:
                print("Jogador criado com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "2":
            print("\n--- Listar Jogadores ---")
            return_code = listar_jogadores()
            if return_code[0] == 200:
                if len(return_code[2]) == 0:
                    print(return_code[1])
                else:
                    # Mapa id -> nome do clube
                    rc_c = listar_clubes()
                    mapa = {}
                    if rc_c[0] == 200:
                        for c in rc_c[2]:
                            mapa[c["id"]] = c["nome"]

                    print(f"{'ID':<5} {'Nome':<20} {'Posicao':<8} {'Valor':>7}  {'Nac.':<14} {'Data Nasc.':<12} {'Clube'}")
                    print("-" * 85)
                    for j in return_code[2]:
                        nome_clube = mapa.get(j["clube_id"], "Sem clube")
                        print(f"{j['id']:<5} {j['nome']:<20} {j['posicao']:<8} {j['valor']:>5.1f}M  {j.get('nacionalidade','-'):<14} {j.get('data_nasc','-'):<12} {nome_clube}")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "3":
            print("\n--- Consultar Jogador ---")
            return_code_lista = listar_jogadores()
            if return_code_lista[0] == 200 and len(return_code_lista[2]) > 0:
                print("\n  Jogadores disponiveis:")
                for j in return_code_lista[2]:
                    print(f"    [{j['id']}] {j['nome']} ({j['posicao']})")
            id_jogador = input("ID do jogador: ")

            return_code = consultar_jogador(id_jogador)
            if return_code[0] == 200:
                j = return_code[2]
                rc_c = listar_clubes()
                mapa = {}
                if rc_c[0] == 200:
                    for c in rc_c[2]:
                        mapa[c["id"]] = c["nome"]
                print("\n  Detalhes do jogador:")
                print(f"    ID            : {j['id']}")
                print(f"    Nome          : {j['nome']}")
                print(f"    Posicao       : {j['posicao']}")
                print(f"    Valor         : {j['valor']}M euros")
                print(f"    Nacionalidade : {j.get('nacionalidade', '-')}")
                print(f"    Data Nasc.    : {j.get('data_nasc', '-')}")
                print(f"    Clube         : {mapa.get(j['clube_id'], 'Sem clube')}")
            elif return_code[0] == 404:
                print("Jogador nao encontrado.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "4":
            print("\n--- Atualizar Jogador ---")
            return_code_lista = listar_jogadores()
            if return_code_lista[0] == 200 and len(return_code_lista[2]) > 0:
                print("\n  Jogadores disponiveis:")
                for j in return_code_lista[2]:
                    print(f"    [{j['id']}] {j['nome']} ({j['posicao']})")
            id_jogador    = input("ID do jogador a atualizar: ")
            nome          = input("Novo nome (enter para manter): ")
            posicao       = input("Nova posicao (enter para manter): ")
            valor         = input("Novo valor (enter para manter): ")
            nacionalidade = input("Nova nacionalidade (enter para manter): ")
            data_nasc     = input("Nova data nasc. YYYY-MM-DD (enter para manter): ")

            _mostrar_clubes()
            clube_id_str = input("Novo clube - ID (enter para manter): ")
            clube_id = int(clube_id_str) if clube_id_str else None

            return_code = atualizar_jogador(
                id_jogador,
                nome          if nome          else None,
                posicao       if posicao       else None,
                valor         if valor         else None,
                nacionalidade if nacionalidade else None,
                data_nasc     if data_nasc     else None,
                clube_id
            )
            if return_code[0] == 200:
                print("Jogador atualizado com sucesso.")
            elif return_code[0] == 404:
                print("Jogador nao encontrado.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "5":
            print("\n--- Remover Jogador ---")
            return_code_lista = listar_jogadores()
            if return_code_lista[0] == 200 and len(return_code_lista[2]) > 0:
                print("\n  Jogadores disponiveis:")
                for j in return_code_lista[2]:
                    print(f"    [{j['id']}] {j['nome']} ({j['posicao']})")
            id_jogador = input("ID do jogador a remover: ")

            return_code = remover_jogador(id_jogador)
            if return_code[0] == 200:
                print("Jogador removido com sucesso.")
            elif return_code[0] == 404:
                print("Jogador nao encontrado.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "0":
            break

        else:
            print("Opcao invalida.")


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

def main():
    while True:
        menu_principal()
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            gerir_clubes()
        elif opcao == "2":
            gerir_jogadores()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
