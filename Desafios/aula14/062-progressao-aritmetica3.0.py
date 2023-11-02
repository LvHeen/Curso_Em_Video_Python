primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da progressão aritmética: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'PA finalizada com {total} termos mostrados.')