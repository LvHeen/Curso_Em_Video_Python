from random import randint

c = 0
while True:
    player = int(input('Digite um número de 1 a 20: '))
    pc = randint(1, 20)
    soma = player + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Você quer apostar em par ou impar [P/I]? ').upper().strip() [0]
    print(f'Você jogou {player} e o computador jogou {pc}. O total deu {soma}')
    print(f'DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')

    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            c += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAMER OVER! Você venceu {c} vezes seguidas.')
    