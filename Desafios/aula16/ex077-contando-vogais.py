palavra = ('aprender', 'programar', 'linguagem', 'python', 'computador', 'aula', 'praticar', 'mercado', 'futuro', 'trabalhar')
for p in palavra:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')