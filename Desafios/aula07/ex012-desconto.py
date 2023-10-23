preço = float (input ('Qual o preço do produto? R$'))
desc = preço - (preço * 5 / 100)
print ('Com desconto de 5% sobre {}, o novo preço é {}' .format (preço, desc))