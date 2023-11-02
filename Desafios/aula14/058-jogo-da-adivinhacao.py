from random import randint
pc = randint(0, 10)
palpites = 1
res1 = input(('Oi, sou seu computador e pensei em um número de 1 a 10, quer tentar adivinhar? ')).upper()
print(pc)
if res1 == 'S':
    res2 = int(input('Beleza, qual seu palpite? '))
    while res2 != pc:
        res2 = int(input('Errado, tenta de novo: '))
        palpites += 1
    print(f'Boa! Era {pc} mesmo! Você conseguiu em {palpites} tentativas.')
else:
    print('Ok :/')