larg = float (input ('Qual a largura da sua parede? '))
alt = float (input ('E a altura? '))
area = larg*alt
tinta = area/2

print ('A area dessa parede é de {} metros quadrados \nPara pintá-la completamente você vai precisar de {}l de tinta' .format(area, tinta))
