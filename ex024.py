#VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO

cid = str(input('Digite o nome da sua cidade: ')).strip()

print('A cidade começa com a palavra "SANTO?"')

print(cid[:5].upper() == 'SANTO')
