n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print(f'REPROVADO! Sua media foi {media}.')
elif 7 > media >= 5:
    print(f'RECUPERAÇÃO! Sua média foi {media}.')
elif media > 7:
    print(f'APROVADO! Sua média foi {media}.')