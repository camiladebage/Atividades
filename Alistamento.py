from datetime import date
anoatual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))

idade = anoatual - ano
idade2 = 18 - idade
idade3 = idade - 18

if idade == 18:
  print('Seu alistamento será esse ano')
elif idade < 18:
  print('Você deverá se alistar daqui a', idade2, 'ano(s)')  
elif idade > 18:
  print('Você deveria ter se alistado a ', idade3,  'ano(s) atrás')
