media1 = float(input('Digite a 1º nota:'))
media2 = float(input('Digite a 2º nota:'))
media3 = float(input('Digite a 3º nota:'))

notafinal = (media1 + media2 + media3) / 3
print(f'Sua nota final é: {notafinal:.1f}')
if notafinal >= 7.0:
  print('APROVADO!')
elif notafinal > 5.0 and notafinal <= 6.9:
  print('RECUPERAÇÃO!')
elif notafinal < 5.0:
  print('REPROVADO!')  
