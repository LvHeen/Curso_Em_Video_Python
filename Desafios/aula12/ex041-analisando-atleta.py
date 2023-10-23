from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade < 9.1:
    print('MIRIM')
elif idade > 9.1 and idade < 14:
    print('INFANTIL')
elif idade > 14.1 and idade < 19:
    print('JUNIOR')
elif idade > 19.1 and idade < 25:
    print('SENIOR')
elif idade > 25.1:
    print('MASTER')