def jogador(nome = 'desconhecido', gols = 0):
    print(f'O jogador {nome} fez {gols}')

#programaPrincipal
nome = str(input('Nome do jogador:'))
gool = str(input('Total de gols'))
if gool.isnumeric():
    gool = int(gool)
else:
    gool = 0

if nome.strip() == '':
    jogador(gols=gool)
else:
    jogador(nome, gool)