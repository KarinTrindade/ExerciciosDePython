#ANALISE DE DADOS EM UMA TUPLA

num = (int(input('Digite um numero: ')),
      int(input('Digite outru numero: ')),
      int(input('Digite mais um numero: ')),
      int(input('Digite o último numero: ')),
      )
print(f'Você digitou os valores {num}')

print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma opção.')
print('Os valores pares digitados foram: ', end=' ')
for n in num:
    if n % 2 ==0:
        print(n, end=' ')