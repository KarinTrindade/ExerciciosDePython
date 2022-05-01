#ALISTAMENTO MILITAR

from datetime import date

nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = (atual - nasc)

print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))


if idade == 18:
    print('VOCÊ DEVE SE ALISTAR AGORA!!!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('O ano do seu alistamento é em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('O ano do seu alistamento foi em {}.'.format(ano))
