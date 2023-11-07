num = cont = 0
while True:
    num = int(input('A tabuada de qual número você quer saber? '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
print('Programa encerrado.')