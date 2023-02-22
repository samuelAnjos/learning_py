
final = [[], []]
for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valor:'))
    if valor % 2 == 0:
        final[0].append(valor)
    else:
        final[1].append(valor)

final[0].sort()
final[1].sort()
print(f'Os valores pares: {final[0]}')
print(f'Os valores impares: {final[1]}')
