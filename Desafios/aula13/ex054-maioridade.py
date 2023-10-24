from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 4):
    nasc = int(input('Em que ano essa pessoa nasceu? '))
    idade = atual - nasc
    if idade < 18:
        totmenor += 1
    else:
        totmaior += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade e {totmenor} pessoas menores de idade.')