num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro: ')),
       int(input('DIgite o último número: ')))
print(f'Você digitou {num}')
print(f'O valor 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 aparece na {num.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')