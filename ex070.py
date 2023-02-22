total = totalMaisMil = 0
maisEmConta = 10000
nomeMaisBarato = ' '
while True:
    nome = str(input('Informe o nome do produto'))
    preco = float(input('Digite o preço do produto'))

    total += preco

    if preco > 1000:
        totalMaisMil += 1

    if preco < maisEmConta:
        nomeMaisBarato = nome
        maisEmConta = preco

    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input('Deseja continuar [s/n]')).strip().lower()[0]

    if resposta == 'n':
        break

print(f'Total gasto: {total}')
print(f'Total que custa mais de mil: {totalMaisMil}')
print(f'Nome do produto mais barato {nomeMaisBarato}')


