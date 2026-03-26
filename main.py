# ============================================
#   main.py — Programa Principal
#
#   Importa os 4 ficheiros:
#     - clubes.py
#     - empresarios.py
#     - jogadores.py
#     - transferencias.py
# ============================================

import clubes
import empresarios
import jogadores
import transferencias


def linha():
    print("-" * 45)


def menu_principal():
    while True:
        print("\n")
        print("  ╔═══════════════════════════════════╗")
        print("  ║   GESTOR DE TRANSFERENCIAS        ║")
        print("  ║   Futebol — 10o Ano               ║")
        print("  ╚═══════════════════════════════════╝")
        print("  1. Clubes")
        print("  2. Empresarios")
        print("  3. Jogadores")
        print("  4. Transferencias")
        print("  0. Sair")
        linha()
        opcao = input("  Opcao: ")

        if opcao == "1":
            # Passa a lista de jogadores para o menu de clubes
            # (para verificar dependencias antes de eliminar)
            clubes.menu_clubes(jogadores.jogadores)

        elif opcao == "2":
            empresarios.menu_empresarios()

        elif opcao == "3":
            # Passa clubes, empresarios e transferencias ao menu de jogadores
            jogadores.menu_jogadores(
                clubes.clubes,
                empresarios.empresarios,
                transferencias.transferencias
            )

        elif opcao == "4":
            # Passa tudo ao menu de transferencias
            transferencias.menu_transferencias(
                jogadores.jogadores,
                clubes.clubes,
                empresarios.empresarios
            )

        elif opcao == "0":
            print("\n  Ate logo!\n")
            break

        else:
            print("  Opcao invalida!")


# Inicia o programa
menu_principal()
