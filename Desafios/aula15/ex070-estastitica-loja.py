total = totmil = menor = cont = 0
barato = ''
while True:
    print(10*'=', 'LOJA SLA', 10*'=')
    nome = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o preço do produto? R$'))
    total += preco
    cont += 1
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar [S/N]? ')).upper()
    if resp == 'N':
        break
print(10*'=', 'FIM DO PROGRAMA', 10*'=')
print(f'O total foi R${total:.2f}.')
print(f'Temos {totmil} produtos custando menos de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')