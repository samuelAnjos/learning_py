import random
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

escolhidos = random.choice(numeros)

numeroUsuario = int(input('Digite um numero'))
contador = 0
while numeroUsuario != escolhidos:
    numeroUsuario = int(input('Digite um numero'))
    contador += 1
print('Você tentou {} até acertar'.format(contador))
print('Numero escolhido pela maquina = {}'.format(escolhidos))