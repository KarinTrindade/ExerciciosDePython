#RADAR ELETRÔNICO

vel = float(input('Qual a velocidade atual do carro? '))
multa = (vel-80) * 7

if vel <80:
    print('Tenha um bom dia! Dirija com segurança')
else:
    print('Você ultrapassou os 80km/h, recebeu a multa no valor de R${:.2f}'.format(multa))
