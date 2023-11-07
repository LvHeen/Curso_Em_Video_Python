cont_idade = homens = mulheres_vinte = 0
while True:
    print(10 * '=', 'CADASTRO DE PESSOAS', 10 * '=')
    idade = int(input('Idade da pessoa: '))
    sexo = str(input('Sexo da pessoa [F/M]: ')).upper()
    opcao = str(input('Quer continuar [S/N]: ')).upper()
    if opcao == 'N':
        break
    else:
        if idade > 18:
            cont_idade += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F':
            if idade < 20:
                mulheres_vinte += 1
print(f'Total de pessoas com mais de 18 anos: {cont_idade}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres_vinte} mulheres com menos de 20 anos.')