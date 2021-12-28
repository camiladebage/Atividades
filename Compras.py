precoproduto = float(input('Digite o valor do produto: '))
pagamento = float(input('''>>>Escolha a forma de pagamento<<< 
1- À vista dinheiro/cheque: 10% de desconto
2- À vista no cartão: 5% de desconto
3- Em até 2x no cartão:  preço normal
4- 3x ou mais no cartão: 20% de juros no valor total
Método de pagamento: '''))
                        
if pagamento == 1:
    print('O valor do produto ficará: R${:.2f}'.format(precoproduto-(precoproduto*0.1)))
elif pagamento == 2:
    print('O valor do produto ficará: R${:.2f}'.format(precoproduto-(precoproduto*0.05)))
elif pagamento == 3:
    total = precoproduto
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de '
    f'R$ {parcela:.2f} SEM JUROS!')
elif pagamento == 4:
    total = precoproduto+(precoproduto*0.2)
    qtdparcelas = int(input('Quantas parcelas: '))
    valorparcelas = total / qtdparcelas
    print(f'Sua compra será parcelada em {qtdparcelas}x '
          f'de R$ {valorparcelas:.2f} e o total é {total}')
else:
    print('Essa não é uma forma válida de pagamento.')
