#Pintando Parede

larg = float(input('Largura da Parede: '))
alt = float(input('Altura da Parede: '))
área = larg * alt
tinta = área / 2
print ('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, área))

print('Para pintar essa parede você precisará de {}l de tinta'.format(tinta))

