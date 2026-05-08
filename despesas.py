def cadastrar_despesa(despesa):
    print('====CADASTRAR DESPESAS====')
    
    while True:
        try:
            cadastro = float(input('Adicione o valor da despesa:'))

            if cadastro <= 0:
                print('Valor invalido, adicione um valor válido!')
                continue
        except ValueError:
            print('Digite um valor válido')
        while True:
            descricao = str(input('Qual a descrição dessa despesa:'))
            if descricao.strip == '':
                print('Adicione uma descrição valida!')
            else:
                print('Descrição válida!')
                break
        while True:
            data = input('Digite a data (a data deve ser adicionada dessa forma: dd/mm/aaaa)\n')
            if "/" not in data:
                print('Adicione a data da forma que foi pedido.')
            else:
                break
        print('Despesa adicionada')

        print("\nDespesa cadastrada:")
        print(f"Valor: R${cadastro:.2f}")
        print(f"Descrição: {descricao}")
        print(f"Data: {data}")
        break
despesa = []
cadastrar_despesa(despesa)
