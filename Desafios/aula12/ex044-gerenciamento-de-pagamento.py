preco = float(input('Digite o preço a ser pagado: R$'))
print('''
Qual será a forma de pagamento: 
[1] à vista no dinheiro ou cheque
[2] à vista no cartão
[3] em 2x no cartão
[4] 3x ou mais no cartão
''')
pag = int(input('-> '))
novo = 0

if pag == 1:
    novo = preco - ((preco * 10) / 100)
    print(f'Nessa opção de pagamento você recebe 10% de desconto, logo o novo preço é {novo:.2f}')
elif pag == 2:
    novo = preco - ((preco * 5) / 100)
    print(f'Nessa opção de pagamento você recebe 5% de desconto, logo o novo preço será R${novo:.2f}.')
elif pag == 3:
    print(f'Nessa opção de pagamento não há desconto. O preço permaneceu R${preco:.2f}')
elif pag == 4:
    novo = preco + ((preco * 20) / 100)
    print(f'Nessa opção de pagamento há 20% de juros, logo o novo preço será {novo:.2f}.')