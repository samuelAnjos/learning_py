sexo = ' '
while sexo not in 'MnFf':
    sexo = str(input('Informe o sexo')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))