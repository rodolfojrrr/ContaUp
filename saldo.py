import sqlite3


def obter_conexao():

    return sqlite3.connect("banco.db")


def calcular_saldo():

    conexao = obter_conexao()
    cursor = conexao.cursor()

    cursor.execute("SELECT SUM(valor) FROM receitas")
    total_receitas = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(valor) FROM despesas")
    total_despesas = cursor.fetchone()[0]

    conexao.close()

    total_receitas = total_receitas if total_receitas is not None else 0.0
    total_despesas = total_despesas if total_despesas is not None else 0.0

    saldo = total_receitas - total_despesas

    return {
        "total_receitas": total_receitas,
        "total_despesas": total_despesas,
        "saldo": saldo,
    }


def mostrar_saldo():
    
    dados = calcular_saldo()

    print("\n========== SALDO ==========")
    print(f"Total de receitas : R$ {dados['total_receitas']:.2f}")
    print(f"Total de despesas : R$ {dados['total_despesas']:.2f}")
    print("----------------------------")

    if dados["saldo"] >= 0:
        print(f"Saldo atual       : R$ {dados['saldo']:.2f}")
    else:
        print(f"Saldo atual       : R$ {dados['saldo']:.2f} saldo negativo")

    print("============================\n")


if __name__ == "__main__":
    mostrar_saldo()
