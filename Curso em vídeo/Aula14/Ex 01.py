sexo = input('Informe seu sexo [M/F]: ').upper().strip()[0]
while sexo not in 'MF':
    sexo = input('Dado inválido. Indique seu sexo: ').upper().strip()[0]
print('Sexo registrado com sucesso.')