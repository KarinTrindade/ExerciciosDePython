#JOGO DO PAR OU IMPAR

from random import randint

v = 0
print('=-' * 25)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 25)
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print('=-' * 25)
print(f'GAME OVER! Você venceu {v} vezes.')