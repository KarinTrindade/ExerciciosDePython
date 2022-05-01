times = ('America-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG',
         'Avaí','Botafogo','Ceará SC', 'CORINTHIANS',
         'Coritiba','Cuiabá','Flamengo','Fluminense',
         'Fortaleza','Goias','Internacional','Juventude',
         'Palmeiras','Bragantino','Santos','São Paulo')
print (f'Lista de times {times}')
print('=-' * 20)
print('Apenas os 5 primeiros colocados da tabela.')
print(times[:5])
print('=-' * 20)
print('Os últimos 4 colocados da tabela.')
print(times[-4:])
print('=-' * 20)
print('Lista com os times em ordem alfabética.')
print(sorted(times))
print('=-' * 20)
print('Em qual posição o time Corinthians está na tabela?')
print('O time CORINTHIANS está na {}° posição.'.format(times.index('CORINTHIANS')))

