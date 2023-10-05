from datetime import date
genero = input('Qual o seu gênero (M - masculino, F - feminino)? ').upper()
if genero == 'F':
    print('Você não tem obrigação de se alistar.')
else:
    atual = date.today().year
    nascimento = int(input('Em que ano você nasceu? '))
    idade = atual - nascimento
    if idade < 18:
        conversao = 18 - idade
        print(f'Ainda vai se alistar! Falta {conversao} anos para sua data de alistamento.')
    elif idade == 18:
        print('Está na hora de alistar!')
    elif idade > 18:
        conversao = idade - 18
        print(f'Já passou da hora de se alistar! Passou {conversao} anos da sua data de alistamento.')