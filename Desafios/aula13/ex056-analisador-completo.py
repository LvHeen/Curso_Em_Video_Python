somaidade = 0
mediaidade = 0
homem = 0
nomehomem = ''
mulher = 0

for pess in range(1, 5):
    nome = str(input('Nome da {}º pessoa: '.format(pess)))
    idade = int(input('Idade da {}º pessoa: '.format(pess)))
    sexo = str(input('Sexo da {}º pessoa [M / F]: '.format(pess))).upper()
    print('=-' * 20)
    somaidade += idade

    if pess == 1 and sexo == 'M':
        homem = idade
        nomehomem = nome
    if sexo == 'M' and idade > homem:
        homem = idade
        nomehomem = nome
    if sexo == 'F' and idade < 20:
        mulher += 1
mediaidade = somaidade / 4

print(f'A média de idade do grupo é {mediaidade} anos.')
print(f'O homem mais velho tem {homem} anos e se chama {nome}.')
print(f'Ao todo são {mulher} mulheres com menos de 20 anos.')