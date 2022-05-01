#CALCULAR O IMC

print('-*-' * 15)
alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / alt **2
print('Seu IMC (índice de massa corpórea é de {:.1f}'.format(imc))

if imc < 18.5:
    print('RESULTADO: Abaixo do Peso')
elif imc <= 25:
    print('RESULTADO: PESO IDEAL')
elif imc <= 30:
    print('RESULTADO: SOBREPESO')
elif imc <= 40:
    print('RESULTADO: OBESIDADE')
else:
    print('RESULTADO: OBESIDADE MÓRBIDA')

print('-*-' * 15)