#CRIANDO UM MENU DE OPÇÕES
from time import sleep

n1 = int(input('Primeiro Valor:'))
n2 = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
    print('=' * 25)
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    print('=' * 25)
    opcao = int(input('>>>>>>> Qual é a sua opção? '))
    print('=' * 25)
    if opcao == 1:
         soma = (n1 + n2)
         print('A soma entre {} e {} é "{}".'.format(n1, n2, soma))
    elif opcao == 2:
        mult = (n1 * n2)
        print('A multiplicação entre {} x {} é "{}"'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            menor = n2
        print('O maior valor digitado entre {} e {} é "{}".'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida, tente novamente.')
    sleep(2)
print('Fim do programa! Volte sempre!')
