#Calcular desconto

preço = float(input('Qual o preço do produto? R$: '))
porcen = preço*5/100

print('O seu valor de R${:.2f} com 5% de desconto passa a valer R${:.2f}'.format(preço, porcen))