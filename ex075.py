nove = 9
contador = 0
tuplas = (int(input('Digite o 1 valor')),
          int(input('Digite o 2 valor')),
          int(input('Digite o 3 valor')),
          int(input('Digite o 4 valor')))

for num in tuplas:
    if num == nove:
        contador+=1

print(tuplas)
print(contador if contador > 0 else 0)
print(tuplas.index(3))

print('Os numeros para são ', end='')
for nu in tuplas:
    if nu % 2 == 0:
        print(nu,end=' ')



