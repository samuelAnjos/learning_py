from random import randint
maior = 0
menor = 100
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

for num in numeros:
    if num > maior:
        maior = num

    if num < menor:
        menor = num
print(numeros)
print(f'O maio foi {maior}') #max(numeros)
print(f'O menor foi {menor}') #min(numeros)
