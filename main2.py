import os
import time
import database
from receitas import cadastrar_receita, relatorio_receitas, editar_receita, deletar_receita
from despesas import cadastrar_despesa, relatorio_despesas, editar_despesa, deletar_despesa
from relatorios import mostrar_saldo, relatorio_geral
from backup import exportar_backup, importar_backup
from login import tela_login

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregando():
    print("Carregando", end="", flush=True)
    for _ in range(3):
        time.sleep(0.6)
        print(".", end="", flush=True)
    time.sleep(0.3)
    limpar()
    
def exibir_menu():
    carregando()
    print("\n========== ContaUP ==========")
    print("--- RECEITAS ---")
    print("  1 - Cadastrar receita")
    print("  2 - Listar receitas")
    print("  3 - Editar receita")
    print("  4 - Deletar receita")
    print("--- DESPESAS ---")
    print("  5 - Cadastrar despesa")
    print("  6 - Listar despesas")
    print("  7 - Editar despesa")
    print("  8 - Deletar despesa")
    print("--- RELATORIOS ---")
    print("  9 - Mostrar saldo")
    print(" 10 - Relatorio geral")
    print("--- BACKUP ---")
    print(" 11 - Exportar backup")
    print(" 12 - Importar backup")
    print("  0 - Sair")
    print("=" * 30)


def main():
    database.inicializar_banco()
    limpar()
    print("Bem-vindo ao ContaUP!")
    time.sleep(2)
    carregando()
    
    acessou = tela_login()
    opcao = None
    
    while acessou and opcao != 0:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            carregando()
            print("Digite um numero valido!")
            continue
    
        if opcao == 1:
            carregando()
            cadastrar_receita()
        elif opcao == 2:
            carregando()
            relatorio_receitas()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == 3:
            carregando()
            editar_receita()
        elif opcao == 4:
            carregando()
            deletar_receita()
        elif opcao == 5:
            carregando()
            cadastrar_despesa()
        elif opcao == 6:
            carregando()
            relatorio_despesas()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == 7:
            carregando()
            editar_despesa()
        elif opcao == 8:
            carregando()
            deletar_despesa()
        elif opcao == 9:
            carregando()
            mostrar_saldo()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == 10:
            carregando()
            relatorio_geral()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == 11:
            carregando()
            exportar_backup()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == 12:
            carregando()
            importar_backup()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == 0:
            carregando()
            print("Sistema encerrado. Ate logo!")
           
        else:
            print("Opcao invalida!")

    database.fechar_banco()


if __name__ == "__main__":
    main()
