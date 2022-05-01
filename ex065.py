#TRATANDO VÁRIOS VALORES

n = cont = media = soma = maior = menor = 0
opcao = ''
while opcao != 'N':
    num = int(input('Digite um número: '))
    opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = soma/cont
print('Você digitou {} numeros e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
