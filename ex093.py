time = list()
jogador = dict()
aproveitamento = list()
while True:
    jogador.clear()
    jogador['name'] = str(input('Informe nome do jogador:'))
    total = int(input('Quantas partidas o jodagor jogou:'))
    for i in range(0, total):
        aproveitamento.append(int(input(f'Quantos gols o jogador fez na partida {i}')))
    jogador['gols'] = aproveitamento
    jogador['totalGols'] = sum(aproveitamento)
    time.append(jogador.copy())
    while True:
        response = str(input('Deseja continuar [S/N]')).lower()[0]
        if response in 'ns':
            break
        print('ERRO! Responda apenas S ou N.')

print('=-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {jogador["name"]} jogou {len(jogador["gols"])} partidas')
print('-=' * 30)
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i} fez {v} gols')



