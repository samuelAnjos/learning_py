from math import sqrt
print('====Calculo da hipotenusa====')
comprimentoCatetoOposto = float(input('Informe o cateto oposto'))
comprimentoCatetoAdjacente = float(input('Informe o cateto adjacente'))
hipotenuda = (comprimentoCatetoOposto**2) + (comprimentoCatetoAdjacente**2)
print(hipotenuda)
print('Valor da hipotenuda para CO {} e CA {} = {:.2f}'.format(comprimentoCatetoOposto, comprimentoCatetoAdjacente, sqrt((hipotenuda))))