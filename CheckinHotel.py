print('>>>>> Bem-vindo(a) ao hotel Bom Descanso <<<<<')

quartos_reservados = {}
opcao = ''


while opcao != 's':
    # Obtém a opção escolhida pelo usuário.
    print('''
 >>>>> OPÇÕES DO SISTEMA <<<<<
  [N] = Nova reserva
  [D] = Remover reserva
  [R] = Exibir Relatório 
  [S] = Sair do Programa 
    ''')
    opcao = input('Opção: ').lower()

    if opcao == 'n':
        # Perguntar o quarto para o usuário.
        quarto = int(input('Informe o número do quarto: '))
        if quarto in quartos_reservados:
            print('Quarto ocupado!')
        else:
            # Perguntar o nome do hospede.
            hospede = input('Informe o nome do hospede: ')
            quartos_reservados[quarto] = hospede
    elif opcao == 'r':
        print('*' * 5, 'RELATÓRIO DOS QUARTOS', '*' * 5)
        for quarto, hospede in quartos_reservados.items():
            print(f'QUARTO Nº {quarto} = {hospede.upper()}')
    elif opcao == 'd':
        del quartos_reservados[quarto]
    elif opcao == 's':
        exit()
