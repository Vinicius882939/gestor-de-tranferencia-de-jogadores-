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
from empresarios import (
    criar_empresario,
    listar_empresarios,
    consultar_empresario,
    atualizar_empresario,
    remover_empresario
)
from transferencias import (
    criar_transferencia,
    listar_transferencias,
    consultar_transferencia,
    atualizar_transferencia,
    remover_transferencia
)


# ==============================
# MENUS
# ==============================

def menu_principal():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Gerir Clubes")
    print("2 - Gerir Jogadores")
    print("3 - Gerir Empresarios")
    print("4 - Gerir Transferencias")
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


def menu_empresarios():
    print("\n===== MENU EMPRESARIOS =====")
    print("1 - Criar empresario")
    print("2 - Listar empresarios")
    print("3 - Consultar empresario")
    print("4 - Atualizar empresario")
    print("5 - Remover empresario")
    print("0 - Voltar")


def menu_transferencias():
    print("\n===== MENU TRANSFERENCIAS =====")
    print("1 - Criar transferencia")
    print("2 - Listar transferencias")
    print("3 - Consultar transferencia")
    print("4 - Atualizar transferencia")
    print("5 - Remover transferencia")
    print("0 - Voltar")


# ==============================
# AUXILIARES — mostrar listas
# ==============================

def _mostrar_clubes():
    return_code = listar_clubes()
    if return_code[0] == 200 and len(return_code[2]) > 0:
        print("\n  Clubes disponiveis:")
        for c in return_code[2]:
            print(f"    [{c['id']}] {c['nome']} ({c['pais']})")
    else:
        print("  (Sem clubes registados)")


def _mostrar_jogadores():
    return_code = listar_jogadores()
    if return_code[0] == 200 and len(return_code[2]) > 0:
        print("\n  Jogadores disponiveis:")
        for j in return_code[2]:
            print(f"    [{j['id']}] {j['nome']} ({j['posicao']})")
    else:
        print("  (Sem jogadores registados)")


def _mostrar_empresarios():
    return_code = listar_empresarios()
    if return_code[0] == 200 and len(return_code[2]) > 0:
        print("\n  Empresarios disponiveis:")
        for e in return_code[2]:
            print(f"    [{e['id']}] {e['nome']} | Licenca: {e['licenca']}")
    else:
        print("  (Sem empresarios registados)")


def _nome_clube(id_clube):
    if id_clube is None:
        return "Livre"
    return_code = consultar_clube(id_clube)
    if return_code[0] == 200:
        return return_code[2]["nome"]
    return "-"


def _nome_jogador(id_jogador):
    return_code = consultar_jogador(id_jogador)
    if return_code[0] == 200:
        return return_code[2]["nome"]
    return "-"


def _nome_empresario(id_empresario):
    if id_empresario is None:
        return "Sem empresario"
    return_code = consultar_empresario(id_empresario)
    if return_code[0] == 200:
        return return_code[2]["nome"]
    return "-"


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
                    print(f"\n{'ID':<5} {'Nome':<20} {'Pais':<15} {'Liga':<18} {'Estadio':<18} {'Fundacao'}")
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
                print(f"\n  ID       : {c['id']}")
                print(f"  Nome     : {c['nome']}")
                print(f"  Pais     : {c['pais']}")
                print(f"  Liga     : {c['liga']}")
                print(f"  Estadio  : {c.get('estadio', '-')}")
                print(f"  Fundacao : {c.get('fundacao', '-')}")
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
            lista_j = rc_j[2] if rc_j[0] == 200 else []

            return_code = remover_clube(id_clube, lista_j)
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
            clube_id_str  = input("ID do clube (enter para sem clube): ")
            clube_id      = int(clube_id_str) if clube_id_str else None

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
                    rc_c = listar_clubes()
                    mapa = {c["id"]: c["nome"] for c in rc_c[2]} if rc_c[0] == 200 else {}
                    print(f"\n{'ID':<5} {'Nome':<20} {'Pos':<6} {'Valor':>7}  {'Nac.':<14} {'Data Nasc.':<12} {'Clube'}")
                    print("-" * 80)
                    for j in return_code[2]:
                        print(f"{j['id']:<5} {j['nome']:<20} {j['posicao']:<6} {j['valor']:>5.1f}M  {j.get('nacionalidade','-'):<14} {j.get('data_nasc','-'):<12} {mapa.get(j['clube_id'],'Sem clube')}")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "3":
            print("\n--- Consultar Jogador ---")
            _mostrar_jogadores()
            id_jogador = input("ID do jogador: ")

            return_code = consultar_jogador(id_jogador)
            if return_code[0] == 200:
                j = return_code[2]
                rc_c = listar_clubes()
                mapa = {c["id"]: c["nome"] for c in rc_c[2]} if rc_c[0] == 200 else {}
                print(f"\n  ID            : {j['id']}")
                print(f"  Nome          : {j['nome']}")
                print(f"  Posicao       : {j['posicao']}")
                print(f"  Valor         : {j['valor']}M euros")
                print(f"  Nacionalidade : {j.get('nacionalidade', '-')}")
                print(f"  Data Nasc.    : {j.get('data_nasc', '-')}")
                print(f"  Clube         : {mapa.get(j['clube_id'], 'Sem clube')}")
            elif return_code[0] == 404:
                print("Jogador nao encontrado.")
            else:
                print("Internal Error: " + return_code[1])

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
            _mostrar_jogadores()
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
# LOGICA DE EMPRESARIOS
# ==============================

def gerir_empresarios():
    while True:
        menu_empresarios()
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            print("\n--- Criar Empresario ---")
            nome     = input("Nome: ")
            licenca  = input("Numero de licenca: ")
            email    = input("Email (enter para ignorar): ")
            telefone = input("Telefone (enter para ignorar): ")

            return_code = criar_empresario(nome, licenca, email, telefone)
            if return_code[0] == 201:
                print("Empresario criado com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "2":
            print("\n--- Listar Empresarios ---")
            return_code = listar_empresarios()
            if return_code[0] == 200:
                if len(return_code[2]) == 0:
                    print(return_code[1])
                else:
                    print(f"\n{'ID':<5} {'Nome':<20} {'Licenca':<15} {'Email':<25} {'Telefone'}")
                    print("-" * 75)
                    for e in return_code[2]:
                        print(f"{e['id']:<5} {e['nome']:<20} {e['licenca']:<15} {e.get('email','-'):<25} {e.get('telefone','-')}")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "3":
            print("\n--- Consultar Empresario ---")
            _mostrar_empresarios()
            id_emp = input("ID do empresario: ")

            return_code = consultar_empresario(id_emp)
            if return_code[0] == 200:
                e = return_code[2]
                print(f"\n  ID       : {e['id']}")
                print(f"  Nome     : {e['nome']}")
                print(f"  Licenca  : {e['licenca']}")
                print(f"  Email    : {e.get('email', '-')}")
                print(f"  Telefone : {e.get('telefone', '-')}")
            elif return_code[0] == 404:
                print("Empresario nao encontrado.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "4":
            print("\n--- Atualizar Empresario ---")
            _mostrar_empresarios()
            id_emp   = input("ID do empresario a atualizar: ")
            nome     = input("Novo nome (enter para manter): ")
            licenca  = input("Nova licenca (enter para manter): ")
            email    = input("Novo email (enter para manter): ")
            telefone = input("Novo telefone (enter para manter): ")

            return_code = atualizar_empresario(
                id_emp,
                nome     if nome     else None,
                licenca  if licenca  else None,
                email    if email    else None,
                telefone if telefone else None
            )
            if return_code[0] == 200:
                print("Empresario atualizado com sucesso.")
            elif return_code[0] == 404:
                print("Empresario nao encontrado.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "5":
            print("\n--- Remover Empresario ---")
            _mostrar_empresarios()
            id_emp = input("ID do empresario a remover: ")

            return_code = remover_empresario(id_emp)
            if return_code[0] == 200:
                print("Empresario removido com sucesso.")
            elif return_code[0] == 404:
                print("Empresario nao encontrado.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


# ==============================
# LOGICA DE TRANSFERENCIAS
# ==============================

def gerir_transferencias():
    while True:
        menu_transferencias()
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

            clube_origem  = int(clube_origem_str)  if clube_origem_str  else None
            clube_destino = int(clube_destino_str) if clube_destino_str else None
            empresario_id = int(empresario_str)    if empresario_str    else None

            return_code = criar_transferencia(
                jogador_id, clube_origem, clube_destino,
                empresario_id, valor, data
            )
            if return_code[0] == 201:
                print("Transferencia criada com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "2":
            print("\n--- Listar Transferencias ---")
            return_code = listar_transferencias()
            if return_code[0] == 200:
                if len(return_code[2]) == 0:
                    print(return_code[1])
                else:
                    print(f"\n{'ID':<5} {'Jogador':<18} {'Origem':<14} {'Destino':<14} {'Valor':>7}  {'Data':<12} {'Estado'}")
                    print("-" * 85)
                    for t in return_code[2]:
                        print(f"{t['id']:<5} {_nome_jogador(t['jogador_id']):<18} {_nome_clube(t['clube_origem_id']):<14} {_nome_clube(t['clube_destino_id']):<14} {t['valor']:>5.1f}M  {t.get('data','-'):<12} {t['estado']}")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "3":
            print("\n--- Consultar Transferencia ---")
            return_code_lista = listar_transferencias()
            if return_code_lista[0] == 200 and len(return_code_lista[2]) > 0:
                print("\n  Transferencias disponiveis:")
                for t in return_code_lista[2]:
                    print(f"    [{t['id']}] {_nome_jogador(t['jogador_id'])} -> {_nome_clube(t['clube_destino_id'])} | {t['estado']}")
            id_t = input("ID da transferencia: ")

            return_code = consultar_transferencia(id_t)
            if return_code[0] == 200:
                t = return_code[2]
                print(f"\n  ID            : {t['id']}")
                print(f"  Jogador       : {_nome_jogador(t['jogador_id'])}")
                print(f"  Clube origem  : {_nome_clube(t['clube_origem_id'])}")
                print(f"  Clube destino : {_nome_clube(t['clube_destino_id'])}")
                print(f"  Empresario    : {_nome_empresario(t['empresario_id'])}")
                print(f"  Valor         : {t['valor']}M euros")
                print(f"  Data          : {t.get('data', '-')}")
                print(f"  Estado        : {t['estado']}")
            elif return_code[0] == 404:
                print("Transferencia nao encontrada.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "4":
            print("\n--- Atualizar Transferencia ---")
            return_code_lista = listar_transferencias()
            if return_code_lista[0] == 200 and len(return_code_lista[2]) > 0:
                print("\n  Transferencias pendentes:")
                for t in return_code_lista[2]:
                    if t["estado"] == "pendente":
                        print(f"    [{t['id']}] {_nome_jogador(t['jogador_id'])} -> {_nome_clube(t['clube_destino_id'])}")
            id_t   = input("ID da transferencia a atualizar: ")
            valor  = input("Novo valor (enter para manter): ")
            data   = input("Nova data YYYY-MM-DD (enter para manter): ")
            print("  Estado: pendente / concluida / cancelada")
            estado = input("Novo estado (enter para manter): ")

            return_code = atualizar_transferencia(
                id_t,
                valor  if valor  else None,
                data   if data   else None,
                estado if estado else None
            )
            if return_code[0] == 200:
                print("Transferencia atualizada com sucesso.")
            elif return_code[0] == 404:
                print("Transferencia nao encontrada.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "5":
            print("\n--- Remover Transferencia ---")
            return_code_lista = listar_transferencias()
            if return_code_lista[0] == 200 and len(return_code_lista[2]) > 0:
                print("\n  Transferencias disponiveis:")
                for t in return_code_lista[2]:
                    print(f"    [{t['id']}] {_nome_jogador(t['jogador_id'])} -> {_nome_clube(t['clube_destino_id'])} | {t['estado']}")
            id_t = input("ID da transferencia a remover: ")

            return_code = remover_transferencia(id_t)
            if return_code[0] == 200:
                print("Transferencia removida com sucesso.")
            elif return_code[0] == 404:
                print("Transferencia nao encontrada.")
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
        elif opcao == "3":
            gerir_empresarios()
        elif opcao == "4":
            gerir_transferencias()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
