from random import randint 
from time import sleep

print('-' * 24)
play = input('OK, vamos lá. Você quer mesmo jogar comigo? \n').strip().lower()
s = 'sim' in play
n = 'não' in play

sleep (1)

if s == True:
    dificuldade = input('Beleza, então escolha a dificuldade (fácil, normal, dificil: ) \n').strip().lower()
    facil = 'fácil' in dificuldade
    normal = 'normal' in dificuldade
    dificil = 'dificil' in dificuldade
    d1 = randint(1, 3)
    d2 = randint(1,6)
    d3 = randint(1, 9)

    sleep(1)

    if facil == True:
        num1 = int (input('Oxi, fácil? Vai né, quem sou eu para julgar. Pode adivinhar aí um número de 1 a 3: \n'))
        if num1 == d1:
            sleep(1)
            print('Acertou, mas também no fácil né...')
        else:
            sleep(1)
            print('Bro, nem no fácil...')

    if normal == True:
        num2 = int(input('OK, isso está começando a ficar interessante. Adivinha o número entre 1 e 6: \n'))
        if num2 == d2:
            print('Espera...')
            sleep(1)
            print('você acertou? Como?')
        else:
            sleep(1)
            print('Não fica triste, você não decepcionou ninguém porque a gente sabia que você ia errar :)')

    if dificil == True:
        num3 = int(input('KKkkkkkkkkkkkkkkkkkkkkkkkkkkkk beleza então. Tenta aí um número de 1 a 9: \n'))
        if num3 == d3:
            sleep(1)
            print('Impossível...')
            sleep(1)
            print('IMPOSSÍVEL! eu nunca perdi esse jogo!!!')
        else:
            sleep(1)
            print('Perder não é vergonha, eu fui programado para ser perfeito mesmo. Bjs')

if n == True:
    sleep(1)
    print('Corre mesmo, covarde')
sleep(1)
print('-----END-----')
