#AUMENTO SALARIAL MULTIPLOS

salario = float(input('Digite seu salário: '))

if salario <=1250:
    novo = salario + (salario * 15 / 100 )
else:
    novo = salario + (salario * 10 / 100)

print('Seu antigo salário era R${:.2f} e o novo agora é R${:.2f}'.format(salario, novo))
