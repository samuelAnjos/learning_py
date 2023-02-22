soma = 0
for c in range(1, 7):
    numero = int(input('Informe número:'))
    if numero % 2 == 0:
        soma += numero
print('Soma: {}'.format(soma))