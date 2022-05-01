#NUMERO POR EXTENSO
cont = ('zero', 'um', 'dois', 'tres', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    n = int((input('Digite um número entre 0 e 20: ')))
    if 0 <= n <=20:
        break
    print('Tente novamente. Digite um número entre 0 e 20: ')

print(f'Você digitou o número {cont[n]}')
res = str(input('Você quer continuar? [S/N]: ')).upper()

while True:
    if res != 'N':
        n = int((input('Digite um número entre 0 e 20: ')))
        if 0 <= n <= 20:
            break
        print('Tente novamente. Digite um número entre 0 e 20: ')
print(f'Você digitou o número {cont[n]}')