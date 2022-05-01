#PROGRESSÃO ARITMÉTICA

print('=' * 20,)
print('10 TERMOS DE UMA PA')
print('=' * 20)

prim = int(input('Primeiro termo:'))
razao = int(input('Razão: '))
dec = prim + (10-1) * razao
for c in range(prim, dec + razao, razao):
    print('{}'.format(c), end=' > ')
print('ACABOU')