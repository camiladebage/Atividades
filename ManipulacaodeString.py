frase = 'Aprendendo Python'

# Pegar caracteres do indice 11 ao 16
print(frase[11:16])
# Omitindo o segundo parametro (ir até o fim)
print(frase[11:])
# Omitindo o primeiro parametro (ir desde o inicio)
print(frase[:10])
# Vai de 0 a 10 pulando de 2 em 2
print(frase[:10:2])
# Descobrir o tamanho da string
print(f'A frase tem {len(frase)} posições')
# Descobrir quantas vezes aparece a letra P
print(f'A letra P aparece {frase.lower().count("p")} vezes')

print('Quantas letras d de 0-10: ',frase.count('d', 0, 10))

print('Quantidade que aparece a palavra Python: ', frase.count('Python'))

print('Frase em minusculo: ', frase.lower())
print('Frase em maiusculo: ', frase.upper())
print('Frase capitalizada: ', frase.capitalize())
print('Primeira letra da frase: ', frase.title())
# Verificar se existe Python na frase
print('Tem Python? ',('Python' in frase))
# Substituir valor
print(frase.replace('Python', 'java').title())

# Remove o espaço das pontas
print('Quantas letras: ', len(frase.strip()))

# Remove o espaço do lado esquerdo
print('Quantas letras: ', len(frase.lstrip()))

# Remove o espaço do lado direito
print('Quantas letras tem sem espaço: ', len(frase.rstrip()))
