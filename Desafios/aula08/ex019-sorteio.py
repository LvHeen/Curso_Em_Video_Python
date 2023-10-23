import random
a1 = input ('Digite o nome do primeiro aluno: ')
a2 = input ('O segundo: ')
a3 = input ('O terceiro: ')
a4 = input ('O quarto: ')
lista = [a1, a2, a3, a4]
print ('O aluno escolhido foi {}' .format(random.choice(lista)))