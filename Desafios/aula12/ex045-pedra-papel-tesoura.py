from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''
SUAS OPÇÕES:
[0] Pedra
[1] Papel
[2] Tesoura''')
player = int(input('Qual sua jogada? '))

print('=-' * 20)
print(f'Você jogou {player}')
print(f'O computador jogou {pc}')
print('=-' * 20)

if pc == 0:
    if player == 0:
        print('Empate')
    elif player == 1:
        print('Jogador Ganha')
    elif player == 2:
        print('Computador Ganha')

if pc == 1:
    if player == 0:
        print('Computador Ganha')
    elif player == 1:
        print('Empate')
    elif player == 2:
        print('Jogador Ganha')

if pc == 2:
    if player == 0:
        print('Jogador Ganha')
    elif player == 1:
        print('Computador Ganha')
    elif player == 2:
        print('Empate')
        