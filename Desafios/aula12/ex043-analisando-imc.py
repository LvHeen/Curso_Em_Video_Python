peso = int(input('Digite seu peso em Kg:'))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
print(f'Para uma pessoa que pesa {peso}Kg e tem {altura}M, seu IMC será {imc:.2f}.')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc > 18.6 and imc < 25:
    print('Você está no peso ideal.')
elif imc > 25.1 and imc < 30:
    print('Você está em sobrepeso.')
elif imc > 30.1 and imc < 40:
    print('Você está em obesidade.')
elif imc > 40:
    print('Você está em obesidade mórbida.')