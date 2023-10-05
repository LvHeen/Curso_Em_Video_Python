n = int(input('Digite um número: '))
print('''Escolha uma das bases de conversão:
      [1] CONVERTER PARA BINÁRIO
      [2] CONVERTER PARA OCTAL
      [3] CONVERTER PARA HEXADECIMAL''')
opcao = int(input('Sua opçao: '))
if opcao == 1:
    print(f'A conversão em BINÁRIO do número {n} é {bin(n)}.')
elif opcao == 2:
    print(f'A conversão em OCTAL de {n} é {oct(n)}.')
elif opcao == 3:
    print(f'A conversão em HEXADECIMAL de {n} é {hex(n)}')
else:
    print('Número inválido!')