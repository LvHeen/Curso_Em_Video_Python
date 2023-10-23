valor = float(input('Qual o valor da casa? R$'))
tempo = int(input('Em quantos anos a casa será paga? '))
sal = float(input('Qual o salário do comprador? R$'))
parcela = valor / (tempo * 12)
minimo = sal * 30 / 100

print(f'Para pagar uma casa de R${valor:.2f} em {tempo} anos a prestaçaõ mensal será de {parcela:.2f}.')
if parcela <= minimo:
    print('Empréstimo Aprovado!')
else:
    print('Empréstimo Negado!')