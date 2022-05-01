#COMPARANDO NÚMEROS

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Não existe valor maior, \033[7;49;36m os dois são iguais\033[m!')
