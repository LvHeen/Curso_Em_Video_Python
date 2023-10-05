print('======LOJAS SEI LÁ======')

preco = float(input('Qual o preço do produto: R$'))
print('''FORMA DE PAGAMENTO:
      [1] à vista dinheiro / cheque 
      [2] à vista no cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção: '))
total = 0
diferenca = 0

if opcao == 1:
    diferenca = (preco * 10) / 100
    total = preco - diferenca
elif opcao == 2:
    diferenca = (preco * 5) / 100
    total = preco - diferenca
elif opcao == 3:
    total = preco
elif opcao == 4:
    diferenca = (preco * 20) / 100
    total = preco + diferenca


print(f'Sua compra de R${preco} vai custar R${total} no final.')