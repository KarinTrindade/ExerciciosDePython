#TABUADA V3.0

while True:
    print('-' * 30)
    n = int(input('Quer ver a tabuada de qual valor?: '))
    if n < 0:
        break
    print('-' * 30)
    print(f'A tabuada do número {n} é')
    for c in range(1,11):
     print(f'{n} x {c} = {c*n}')
print('PROGRAMA TABUADA ENCERRADO, VOLTE SEMPRE!!!')