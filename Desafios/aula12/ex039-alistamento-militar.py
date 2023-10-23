from datetime import date

atual = date.today().year
nasc = int(input('ano de nascimento: '))
idade = atual - nasc
if idade == 18:
    print('Você precisa se alistar imediatamente.')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você deveria ter se alistado há {saldo} anos.')