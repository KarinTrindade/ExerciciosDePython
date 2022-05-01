#TABUADA V.2.0

n = int(input('Digite um número para saber a tabuada: '))
print('A tabuada do número {} é'.format(n))
for c in range(1, 11):
    print('> {} x {} = {}'.format(n, c, c*n))

