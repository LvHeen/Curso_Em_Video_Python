n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2

#print('PARABENS' if m>=6 else 'ESTUDE MAIS')
print (f'Sua nota foi {m:.1f}')
if m >= 6:
    print('Sua nota foi boa. Parabéns!')
else:
    print('Sua nota ficou abaixo da média. Estude mais.')