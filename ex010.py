#Conversor de Moedas para Dolar

real = float(input('Quanto dinheiro você tem na sua carteira?: R$'))
dolar = real /5.19

print('Com seus R${} reais você pode comprar U${:.2f} em dolar'.format(real, dolar))