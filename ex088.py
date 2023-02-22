from random import randint
lista = list()
listFinal = list()

total = 0
round = int(input('Quantos numeros vc quer que sorteie'))
while total < round:
    count = 0
    while True:
        number = randint(1, 60)
        if number not in lista:
            lista.append(number)
        count += 1
        if count >= 9:
            break
    lista.sort()
    listFinal.append(lista[:])
    lista.clear()
    total += 1

for indice, v in enumerate(listFinal):
    print(f'Jogo {indice+1} : {v}')

#04 05 17 20 48 52