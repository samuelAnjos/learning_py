lista = list()
hasFive = 0
while True:
    lista.append(int(input('Informe valores')))


    resposta = str(input('Deseja continuar? (s/n)')).lower()
    if resposta == 'n':
        break

lista.sort(reverse=True)
print(f'Voce digitou {len(lista)}')
print(f'Os valores em ordem decrescente são {lista}')
for i in lista:
    if i == 5:
        hasFive = 1
print('O valor 5 faz parte da lista' if hasFive == 1 else "O valor 5 nao faz parte da lista")






