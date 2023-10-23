n1 = int (input ('Digite um número: '))
n2 = int (input ('Agora outro número: '))
soma = n1 + n2
multi = n1 * n2
div = n1 / n2
pot = n1 ** n2

print('A soma entre {} e {} é {}.\nJá a multiplicação é {}.\nA divisão é {:.2f} e a potencialização é {}.'.format(n1, n2, soma, multi, div, pot))
