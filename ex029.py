velocidade  = float(input('Qual a velocidade do carro'))
velocidadeUltra = velocidade - 80
valorPagar = velocidadeUltra * 7
if velocidade > 80 and velocidadeUltra > 0:
    print('Foi multado, por passar de 80km/h. Valor da multa {:.2f}'.format(valorPagar))
else:
    print('Faça, uma boa viajem, que Deus lhe proteja!')