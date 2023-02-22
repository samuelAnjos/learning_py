valores = list()

for i in range(1, 6):
    valores.append(int(input(f'Informe valor {i}:')))

print(f'Voce digitou {valores}')
print(f'Maior valor: {max(valores)} na posiçao ', end=' ')
for indece, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{indece}...',end='')
print(f'\nMenor valor: {min(valores)} na posiçao ', end=' ')
for indece, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{indece}...',end='')