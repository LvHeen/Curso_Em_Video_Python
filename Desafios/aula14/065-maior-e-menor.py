resp = 'S'
soma = qto = media = maior = menor = 0
while resp == 'S':
    num = int(input('Digite um número: '))
    soma += num
    qto += 1
    if qto == 1:
        maior = menor = num
    else: 
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = input('Quer continuar [S/N]: ').upper()
media = soma/ qto
print(f'Você digitou {qto} número e a média entre eles foi {media:.2f}')
print(f'O amior valor foi {maior} e o menor {menor}')