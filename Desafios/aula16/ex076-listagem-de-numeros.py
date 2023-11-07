lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Compasso', 9.99,
         'Mochila', 150.32)
print('=' * 40)
print(F'{"LISTAGEM DE PREÇOS":^40}')
print('=' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:<30}', end='')
    else:
        print(f'R${lista[pos]:7.2f}')
print('=' * 40)  
