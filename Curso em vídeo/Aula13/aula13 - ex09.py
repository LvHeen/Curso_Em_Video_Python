'''LEVANDO EM BASE O ANO DE 2023'''
maior = 0
menor = 0
for pessoa in range(1, 4):
    nasc = int(input(f'Data de nascimento da {pessoa}º pessoa: '))
    if nasc <= 2005:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'Dentre as 7 pessoas {maior} são maiores de idade e {menor} são menores de idade.')