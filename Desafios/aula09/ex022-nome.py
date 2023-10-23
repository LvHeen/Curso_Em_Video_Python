nome = input('Qual seu nome completo? ')
dividido = nome.split()
espaços = "".join(nome.split()) ##divide tudo com split e junta os espaços a nada com o join


print ('Todo maísculo: {}' .format(nome.upper()))
print ('Todo minusculo: {}' .format(nome.lower()))
print ('Quantidade de letras: {}' .format(len(espaços)))
print ('Quantidade de letras no primeiro nome: {}' .format(len(dividido [0])))