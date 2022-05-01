#Sorteando Item na Lista
from random import choice

aluno = input('Primeiro Aluno:')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')

lista = [aluno, aluno2, aluno3, aluno4]

print('O aluno sorteado foi {}'.format(choice(lista)))