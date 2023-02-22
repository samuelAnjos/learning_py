matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somaColuna = maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        matrix[i][j] = int(input('Informe valor:'))

for i in range(0, 3):
    print()
    for j in range(0, 3):
        print(f'[{matrix[i][j]:^5}]', end=' ')

#Soma dos pares
for i in range(0, 3):
    for j in range(0, 3):
        if matrix[i][j] % 2 == 0:
            soma += matrix[i][j]
print(f'\nA soma dos valores pares: {soma}')

#Soma da 3ª coluna
for linha in range(0, 3):
        somaColuna += matrix[linha][2]
print(f'A soma dos valores 3ª coluna: {somaColuna}')

#Soma da 2ª linha
for coluna in range(0, 3):
        if matrix[1][coluna] > maior:
            maior = matrix[1][coluna]
print(f'O maior da 2ª linha: {maior}')
