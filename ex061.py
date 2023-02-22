primeiroTermo = int(input('Informe o primeiro termo da PA'))
razao = int(input('Informe a razão da PA'))

termo = primeiroTermo
contador = 1
while contador <= 10:
    print('{} ->'.format(primeiroTermo), end=' ')
    primeiroTermo += razao
    contador += 1
print('Fim')