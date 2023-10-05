from time import sleep
n1 = int(input('Primeiro valor: '))
n2  = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('========-ESCOLHA SUA OPÇÃO-=========')
    opcao = int(input('''
        [1] somar
        [2] multiplicar
        [3] maior valor
        [4] novos números
        [5] sair do programa
        >>>>>> Qual opção: '''))
    sleep(2)

    if opcao == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
        sleep(2)

    elif opcao == 2:
        mult = n1 * n2
        print(f'{n1} x {n2} = {mult}')
        sleep(2)

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior valor entre {n1} e {n2} é {maior}')
        sleep(2)

    elif opcao == 4:
       print('Informe os valores outra vez: ')
       n1 = int(input('Primeiro valor: '))
       n2 = int(input('Segundo valor: '))
       sleep(2)

    elif opcao == 5:
        print('Fim do programa.')
        sleep(2)

    else:
       print('Opção inválida. Tente novamente: ')