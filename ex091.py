from operator import itemgetter
from random import randint
from time import sleep

jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6),
        }
print('Valores sorteados')
for k, v in jogo.items():
        print(f'{k} tirou {v} no dado')
        sleep(1)
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
        print(f'{i+1} lugar: {v[0]} com {v[1]}.')
        sleep(1)
