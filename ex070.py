#ESTATÍSTICAS EM PRODUTOS

print('_' * 25)
print('  LOJAS SUPER BARATÃO')
print('_' * 25)
total = totalp = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço:R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totalp +=1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    opcao = ' '
    while opcao not in 'SN':
         opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

    if opcao == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra é R${total:.2f}')
print(f'Temos {totalp} produto custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')
