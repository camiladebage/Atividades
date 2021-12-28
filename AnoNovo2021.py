from datetime import date
hoje = date.today()
anonovo = date(hoje.year, 12, 31) - date.today()
print(f'Faltam {anonovo.days} dias para o ano novo de 2021!!!')
