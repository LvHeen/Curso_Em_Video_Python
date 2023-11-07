numextenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')

while True:
    opcao = int(input('Digite um número entre 0 e 20: '))
    if 0 < opcao < 20:
        break
    print('Número inválido, tente novamente: ')
print(f'O número {opcao} escrito em extenso é {numextenso[opcao]}')
