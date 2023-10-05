num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2:
    print(f'{num1} é maior que {num2}.')
elif num2 > num1:
    print(f'{num2} é maior que {num1}.')
elif num1 == num2:
    print('Ambos os números são iguais.')