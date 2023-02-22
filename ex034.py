salario = float(input('Informe o salario'))
if salario > 1250.00:
    print('Novo salario {:.2f}'.format(salario + (salario * 10/100)))
else:
    print('Novo salario {:.2f}'.format(salario + (salario * 15/100)))