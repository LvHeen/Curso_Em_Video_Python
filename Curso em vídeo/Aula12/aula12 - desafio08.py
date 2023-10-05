peso = float(input('Qual seu peso em kg? '))
altura = float(input('Qual sua altura em metros? '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Individuo abaixo do peso.')
elif 18.5 < imc < 25:
    print('Individuo em peso ideal.')
elif 25 < imc < 40:
    print('Individuo em obesidade.') 
elif imc > 40:
    print('Indivicuo em obesidade mórbida.')
