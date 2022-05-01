#VALIDAÇÃO DE DADOS

sexo = str(input('Informe seu sexo: [M/F] ')).upper()[0].strip()
while sexo not in 'MF':
    sexo = (input('Dados inválidos. Por favor, informe seu sexo: ')).upper()[0].strip()
print('Sexo {} registrado com sucesso.'.format(sexo))
