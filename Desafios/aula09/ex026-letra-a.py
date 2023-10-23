frase = input ('Digite uma frase: ').upper().strip()
print ('Quantas vezes aparece a letra A: {}' .format(frase.count('A')))
print ('A primeira letra A aparece pela primeira vez na posição: {}' .format(frase.find('A') + 1))
print ('A letra A aparece pela última vez a posição: {}' .format(frase.rfind('A')))