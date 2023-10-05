resp = 'S'
soma = media = cont = 0
while resp in 'S':
    num = int(input('Digite um número: '))
    resp = input('Quer continuar? [S /N] ').upper().strip()
    if resp != 'S' and resp != 'N':
        print('Resposta inválida.')
    soma = soma + num
    cont = cont + 1
    media = (num * cont) / cont
print(f'Você digitou {cont} números. A soma entre eles foi {soma} e a média foi {media}')