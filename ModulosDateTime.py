from datetime import date, datetime
print(f'Hoje é dia {date.today()}')
print(f'Hoje é dia {date.today().strftime("%d/%m/%Y")}')
print (f'Hoje é dia {date.today().day},' f'o mês  {date.today().month},' f'e o ano é {date.today().year}')
print(f'Agora é:  {datetime.now().strftime("%H:%M:%S")}')

## Exercicio

nascimento = int(input('Digite seu ano de nascimento: '))

print(f'Sua idade é: {date.today().year - nascimento} ano(s)')
