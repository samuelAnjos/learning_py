lista = []
listaPar = []
listaImpar = []
while True:
    lista.append(int(input('Digite um numero:')))
    resposta = str(input('Quer continuar? [s/n]')).lower()
    if resposta == 'n':
        break


for i in lista:
    if i % 2 == 0:
        listaPar.append(i)
    else:
        listaImpar.append(i)

print(f'Lista Completa {lista}')
print(f'Lista com Pares {listaPar}')
print(f'Lista com Impares {listaImpar}')