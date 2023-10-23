viagem = float (input ('Qual a distância da sua viagem? '))
v1 = viagem * 0.50
v2 = viagem * 0.45

if viagem <= 200:
    print('O preço da sua passagem é R${:.2f}' .format(v1))
else:
    print('O preço da sua viagem é R${:.2f}' .format(v2))
