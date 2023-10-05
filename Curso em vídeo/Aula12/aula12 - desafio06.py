from datetime import date

atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc

if idade < 9:
    print(f'As pessoas com {idade} anos pertencem à Categoria Mirim')
elif idade < 14:
    print(f'As pessoas com {idade} anos pertencem à Categoria Infantil')
elif idade < 19:
    print(f'As pessoas com {idade} anos pertencem à Categoria Junior')
elif idade < 25:
    print(f'As pessoas com {idade} anos pertencem à Categoria Senior')
else:
    print(f'As pessoas com {idade} anos pertencem à Categoria Master')