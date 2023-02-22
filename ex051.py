primeiroTermo = int(input('Informe o primeiro termo da PA'))
razao = int(input('Informe a razão da PA'))
#an = a1 + (n – 1) . r
decimo = primeiroTermo + ((10 - 1) * razao)
for c in range(primeiroTermo, decimo+razao, razao):
    print('{}'.format(c), end=' -> ' )
print('Fim')