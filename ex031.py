#CUSTO DA VIAGEM

n = float(input('Qual a distância da sua viagem? '))

if n <=200:
    print('O total da sua viagem de {}Km é R${:.2f}'.format(n, n*0.50))
else:
    print('O total da sua viagem de {}Km é R${:.2f}'.format(n, n*0.45))