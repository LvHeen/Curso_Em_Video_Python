import math
an = int (input ('Digite o ângulo desejado: '))
sen = math.sin (math.radians (an))
cos = math.cos (math.radians (an))
tan = math.tan (math.radians (an))
print (' Ângulo: {:.2f} \n Seno: {:.2f} \n Cosseno: {:.2f} \n Tangente: {:.2f}' .format(an, sen, cos, tan))