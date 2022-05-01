#ANALISADOR DE TEXTO

frase = str(input('Digite seu nome completo:')).strip()

print('Seu nome MAIUSCULO é {}'.format(frase.upper()))
print('Seu nome MINUSCULO é {}'.format(frase.lower()))
print('Quantas Letras ao todo? - {} LETRAS'.format(len(frase) - frase.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(frase.find(' ')))

separa = frase.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))