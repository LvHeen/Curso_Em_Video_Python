from random import randint
from time import sleep

pc = randint(0, 10)
acertou = False

print('Vamos jogar de novo?')
sleep(2)
print('Acabei de pensar em um número de 0 a 10.')
sleep(2)
player = int(input('Qual seu palpite? '))

while not acertou:
    if player > pc:
        player = int(input('Errado, chuta mais baixo:  '))
    elif player < pc:
        player = int(input('Errado. Chuta mais alto: '))
    elif player== pc:
        acertou = True
print(f'Boa! Eu pensei em {pc} mesmo :D')