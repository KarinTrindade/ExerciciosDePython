#PROGRESSAO ARITMETICA V.2.0

print('GERADOR DE PA')
print('-=' * 20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} > '.format(termo), end=' ')
    termo = termo + razao
    cont += 1
print('FIM')
