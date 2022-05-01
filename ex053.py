#DETECTOR DE PALÍNDROMO

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
'''inverso = junto[::-1]'''#OUTRA FORMA, UTILIZANDO O FATIAMENTO
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('É um PALINDROMO')
else:
    print('NÃO é um PALINDROMO')

