#MEDIA DO ALUNO MOSTRANDO SE ESTÁ APROVADO, REPROVADO OU RECUPERAÇÃO

n1 = float(input('Digite a sua primeira média: '))
n2 = float(input('Digite a sua segunda média: '))
media = (n1 + n2) / 2

if media < 5:
    print('Tirando {} e {} a média do aluno é {:.1f} -- O aluno está \033[7;49;31mREPROVADO\033[m'.format(n1, n2, media))
elif media >= 7:
    print('Tirando {} e {} a média do aluno é {:.1f} -- O aluno está \033[7;49;32mAPROVADO\033[m'.format(n1, n2, media))
else:
    print('Tirando {} e {} a média do aluno é {:.1f} -- O aluno está em RECUPERAÇÃO'.format(n1, n2, media))
