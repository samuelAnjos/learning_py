'''for c in range(0, 5):
    if c == 0:
        print('Oi é ZERO')
    else:
        print('Não é zero')'''

#fazer um algoritmo de teste tipo sorteio da mega sena
from random import randint

lista = list()
listaFinal = list()

total = 0
quantosNuemros = int(input('Quantos numero vc quer jogar?'))

while total < quantosNuemros:
    count  = 0
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            count += 1
            if count >= 9: #Aqui pode mudar
                lista.sort()
                listaFinal.append(lista[:])
                lista.clear()
                total += 1

for i, v in enumerate(listaFinal):
    print(f'O JOGO {i+1}  :  {v}')