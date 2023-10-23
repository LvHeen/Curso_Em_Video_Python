from datetime import date
ano = int (input('Digite um ano ou digite 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('{} é ano BISSEXTO' .format(ano))
else:
    print ('{} não é ano BISSEXTO' .format(ano))