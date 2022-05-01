#GERENCIADOR DE PAGAMENTOS
print('========== LOJAS KARIN ==========')
valor = float(input('Preço das compras R$:'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a sua opção? '))
um = valor - (valor * 10 / 100)
dois = valor - (valor * 5 / 100)
quatro = valor + (valor * 20 / 100)

if opcao == 1:
    print('Sua compra de R${:.2f} vai custar \033[40;32;1mR${:.2f}\033[m no final.'.format(valor, um))
elif opcao ==2:
    print('Sua compra de R${:.2f} vai custar \033[40;32;1mR${:.2f}\033[m no final.'.format(valor, dois))
elif opcao ==4:
    parc = int(input('Quantas parcelas?: '))
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS'.format(parc, (quatro / parc), end=''))
    print('Sua compra de R${:.2f} vai custar \033[40;32;1mR${:.2f}\033[m no final.'.format(valor, quatro))
elif opcao ==3:
    print('Sua compra será parcelada em 2x SEM JUROS de {}'.format(valor / 2))
    print('O total da sua compra é de \033[40;32;1mR${:.2f}\033[m'.format(valor))

else:
    print('Opção inválida, tente novamente.')
