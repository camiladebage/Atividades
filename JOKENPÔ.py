from random import randint

print('>>>Vamos jogar JOKENPÔ<<<')
usuario = int(input('Escolha entre: '
           '\n1- Pedra'
           '\n2- Papel'
           '\n3- Tesoura '
           '\n'))
pc = randint (1, 3)

if usuario == 1:
  if pc == 1:
    print('Seu adversário escolheu PEDRA')
    print('Empate!')
  elif pc == 2:
    print(' Seu adversário escolheu PAPEL')
    print ('Você perdeu!')
  elif pc == 3:
    print(' Seu adversário escolheu TESOURA')
    print('Você ganhou!')  

if usuario == 2:
  if pc == 1:
    print('Seu adversário escolheu PEDRA')
    print('Você ganhou!')
  elif pc == 2:
    print(' Seu adversário escolheu PAPEL')
    print ('Empate!')
  elif pc == 3:
    print(' Seu adversário escolheu TESOURA')
    print('Você perdeu!')  

if usuario == 3:
  if pc == 1:
    print('Seu adversário escolheu PEDRA')
    print('Você perdeu!')
  elif pc == 2:
    print(' Seu adversário escolheu PAPEL')
    print ('Você ganhou!')
  elif pc == 3:
    print(' Seu adversário escolheu TESOURA')
    print('Empate!')  
