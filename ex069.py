#ANALISE DE DADOS EM GRUPO
total18 = totalho = totalm20 = cont = 0
opcao = ''
while True:
    print('-' * 25)
    print('CADASTRE UMA PESSOA')
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if idade >= 18:
        total18 += 1
    if sexo in 'M':
        totalho += 1
    if sexo in 'F' and idade < 20:
        totalm20 += 1
    if opcao != 'S':
        break
print(f'O total de pessoas maiores de 18 anos é {total18}.')
print(f'O total de homens é {totalho}.')
print(f'E o total de mulheres com menos de 20 anos é {totalm20}.')
print('====== FIM DO PROGRAMA ======')