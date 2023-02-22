distacia = float(input('Informe a distancia percorrida'))
preco = distacia*0.50 if distacia <= 200 else distacia*0.45
print('Valor a pagar {:.2f}'.format(preco))
