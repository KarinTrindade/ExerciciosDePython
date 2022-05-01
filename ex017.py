#Catetos e Hipotenusa

from math import hypot
cateto = float(input('Qual o comprimento do cateto oposto? '))
adj = float(input('Qual o comprimento do cateto adjacente? '))

"""result = hypot(cateto, adj)"""

print('A hipotenusa vai medir {:.2f}'.format(hypot(cateto, adj)))