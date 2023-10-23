vel = float (input ('Qual a sua velocidade: '))
multa = (vel - 80) * 7

if vel > 80:
    print ('Você exedeu o limite de velocidade! Sua multa será de R${:.2f}.' .format(multa))
else:
    print ('Dirija em segurança.')