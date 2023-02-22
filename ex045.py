from random import randint
from time import sleep
itens = ('pedra','papel','tesoura')
computador = randint(0, 2)
print('''Sua opções
[0] PEDRA
[1] PAPEL
[2] TEROURA''')
jogador = int(input('Qual é a sua jogada'))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada Inválida')
elif computador == 1:
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('Jogada Inválida')
elif computador == 2:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Inválida')