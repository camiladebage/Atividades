frase = str(input('Digite sua frase:'))

print (f'A letra "A" aparece {frase.lower().count("a")} vezes')
print (f'A letra "E" aparece {frase.lower().count("e")} vezes')
print (f'A letra "I" aparece {frase.lower().count("i")} vezes')
print (f'A letra "O" aparece {frase.lower().count("o")} vezes')
print (f'A letra "U" aparece {frase.lower().count("u")} vezes')

comprimento = len(frase)
ultima = frase[comprimento-1]

print('A primeira letra da frase é: ',frase[0])
print(f'A ultima letra da frase é: ', ultima)

frase2 = frase.split()

print(f'A frase tem {frase2} palavras')
