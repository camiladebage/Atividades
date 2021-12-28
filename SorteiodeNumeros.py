from random import randint

numeros = randint(0,5)

escolha = int(input('Qual número você acha que foi sorteado: '))
if escolha == numeros:
  print('Você acertou') 
else:
  print('Você não acertou') 

print (f'O número sorteado foi: ' ,numeros)  
