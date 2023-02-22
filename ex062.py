primeiroTermo = int(input('Informe o primeiro termo da PA'))
razao = int(input('Informe a razão da PA'))

termo = primeiroTermo
contador = 1
resposta = 10
totalTermos = 0
while resposta != 0:
    totalTermos += resposta
    while contador <= totalTermos:
        print('{} ->'.format(primeiroTermo), end=' ')
        primeiroTermo += razao
        contador += 1
    print('Pause')
    resposta = int(input('Quantos termos você que digitar a mais?'))
