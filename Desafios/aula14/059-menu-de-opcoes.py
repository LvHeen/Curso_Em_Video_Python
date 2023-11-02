n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Outro número inteiro: '))
maior = 0
res = 0
if n1 > n2:
    maior = n1
else:
    maior = n2

while res != 5:
    print('''
========================
Escolha uma opção: 
[1] a soma
[2] a multiplicação
[3] o maior
[4] digitar novos números
[5] sair''')
    res = int(input('---> '))
    if res == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif res == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif res == 3:
        print(f'O maior entre {n1} e {n2} é {maior}')
    elif res == 4:
        print('Digite os valores novamente: ')
        n1 = int(input('Primeiro número'))
        n2 = int(input('Segundo número'))
print('Fim')