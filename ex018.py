#Seno, Cosseno, Tangente

import math

angulo = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cose = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))


print('O angulo de {} tem o SENO de {:.2f} '.format(angulo, seno))
print ('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cose))
print ('O angulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tang))
