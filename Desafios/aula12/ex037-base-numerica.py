num = int(input('Digite um número inteiro: '))
print('''Escolha qual formatação você quer para esse número:
      [1] BINÁRIO
      [2] HEXADECIMAL
      [3] OCTAL''')
opcao = int(input('Opção número '))
if opcao == 1:
    print(f'{num} em BINÁRIO é {bin(num)}')
elif opcao == 2:
    print(f'{num} em HEXADECIMAL é {hex(num)}')
elif opcao == 3:
    print(f'{num} em OCTAL é {oct(num)}')
else:
    print('Valor inválido.')