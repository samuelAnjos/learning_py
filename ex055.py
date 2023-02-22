maior = 0
menor = 200
for c in range(1, 6):
    peso = float(input('peso?'))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('Maior Peso {}'.format(maior))
print('Menor Peso {}'.format(menor))