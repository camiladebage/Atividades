lideranca = []
opcao = ''

while opcao != 's':
    print('''
            Qual tipo de liderança você mais se identifica? 
            [1] = Liderança Autocrática
            [2] = Liderança Democrática
            [3] = Liderança Liberal
            [4] = Sair do Programa 
            ''')
    opcao = input('Opção: ').lower()
    if opcao == '1':
        print('''
        Liderança autocrática é um modelo de gestão em que o líder tem a 
        palavra final sobre tudo e tende a não ouvir ou aceitar opiniões divergentes.
        Podemos definir então que liderança autocrática como um modelo de gestão em que o líder 
        centraliza em si todo o poder decisório de uma equipe, departamento ou empresa como um todo.
        -------------------------------------------------------------------------------------------
        ''')

    elif opcao == '2':
        print('''
        O líder democrático é aquele que praticamente divide a tarefa de liderança com seus funcionários.
        Ele incentiva a participação de seus liderados em todos os projetos da equipe.
        ------------------------------------------------------------------------------
        ''')

    elif opcao == '3':
        print('''
        A liderança liberal é conhecida como a ausência de influência direta do líder no processo de 
        evolução dos seus liderados. Dessa forma, permite-se que a equipe tome decisões com mais liberdade,
        pois o gestor participa apenas quando a sua presença é requisitada.
        --------------------------------------------------------------------------------------------------
        ''')

    elif opcao == '4':
        exit()
