#CLASSIFICAÇÃO DO ATLETA
from datetime import date
ano = int(input('Digite o ano de nascimento do aluno para saber a sua categoria: '))
data = date.today().year
idade = (data - ano)

if idade <= 9:
    print('Quem nasceu em {} tem {} anos. Sua categoria é MIRIM'.format(ano, idade))
elif idade <= 14:
    print('Quem nasceu em {} tem {} anos. Sua categoria é INFANTIL'.format(ano, idade))
elif idade <= 19:
    print('Quem nasceu em {} tem {} anos. Sua categoria é JUNIOR'.format(ano, idade))
elif idade <= 25:
    print('Quem nasceu em {} tem {} anos. Sua categoria é SÊNIOR'.format(ano, idade))
else:
    print('Quem nasceu em {} tem {} anos. Sua categoria é MASTER'.format(ano, idade))