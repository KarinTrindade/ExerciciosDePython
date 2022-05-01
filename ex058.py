#JOGO ADIVINHAÇÃO V.2.0
from random import randint
computador = randint(0, 10) #FAZ O COMPUTADOR "PENSAR"
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente novamente')
        else:
            print('Menos...Tente novamente')
print('Acertou {} tentativas. Parabéns'.format(palpites))
