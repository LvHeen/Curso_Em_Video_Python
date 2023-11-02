sexo = input('Informe seu sexo [M/F]: ').upper()
while sexo not in 'MF':
    sexo = input('Dado inválido, digite seu sexo [M/F]: ').upper()
print('Dado cadastrado com sucesso.')