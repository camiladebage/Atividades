filmes = []
opcao = ''

while opcao != 's':
    print('''
            =-=-=-= OPÇÕES DO SISTEMA =-=-=-=
                [N] = Nova cadastro de filme
                [F] = Remover filme
                [R] = Relatório 
                [S] = Sair do Programa 
            ''')
    opcao = input('Opção: ').lower()
    if opcao == 'n':
        novofilme = input('Digite o novo filme: ')
        filmes.append(novofilme)
    elif opcao == 'f':
        posicao = int(input('Posição para remover: '))
        filmes.pop(posicao)
    elif opcao == 'r':
        print('---- Relatório de filmes ----')
        for item in filmes:
            print(item)
    elif opcao == 's':
        exit()
