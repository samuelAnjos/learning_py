flag = soma = contador = 0
flag = int(input('Informe numero'))
while flag != 999:
    soma += flag
    contador += 1
    flag = int(input('Informe numero'))
print('Total de numeros: {}'.format(contador))
print('Soma total: {}'.format(soma))