dias = int ( input ('Por quantos dias você usou o carro? '))
km = float (input ('Quantos quilometros você andou com o carro? '))
totaldias = dias * 60
totalkm = km * 0.15
total = totaldias + totalkm

print ('O preço total a pagar é R${:.2f}' .format (total))