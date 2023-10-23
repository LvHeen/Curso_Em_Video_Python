sal = float (input ('Qual seu salário atual? R$'))
sal1 = sal * (15 / 100)
sal2 = sal * (10 / 100)

if sal <= 1250:
    print('Seu aumento será de 15%. Seu novo salário é R${:.2f}' .format (sal + sal1))
else:
    print ('Seu aumento será de 10%. Seu novo salário é R${:.2f}' .format (sal + sal2))