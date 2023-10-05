valor = float(input('Qual o valor total da casa? R$'))
sal = float(input('Qual o sálario bruto do comprador? R$'))
tempo = int(input('Em quantos anos o comprador vai pagar essa casa? '))
prestação = valor / (tempo * 12)
total = (sal * 30) / 100

if prestação <= total:
    print(f'Para pagar uma casa de R${valor:.2f} em {tempo} anos, a parcela mensal será de R${prestação:.2f}')
    print('Empéstimo Aprovado!')
else:
    print(f'Para pagar uma casa de R${valor:.2f} em {tempo} anos, a parcela mensal será de R${prestação:.2f}')
    print('Empréstimo Negado!')

    '''REFAZER - dificuldade na organização'''