import random
lista = list()

def sorteia():
    for i in range(1, 6):
        lista.append(random.randint(1,10))
    print(lista)

def somaPar():
    soma=0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(soma)


sorteia()
somaPar()