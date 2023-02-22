lista = list()
pilha = []
maior = menor = 0
while True:
    lista.append(str(input('Informe seu nome')))
    lista.append(float(input('Informe seu peso')))
    if len(pilha) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    pilha.append(lista[:])
    lista.clear()
    resposta = str(input('Deseja continuar [s/n]'))
    if resposta in 'Nn':
        break

print(f'Total de pessoas cadastradas {len(pilha)}')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pilha:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
print()
for p in pilha:
    if p[1] ==  menor:
        print(f'[{p[0]}]', end='')
print()
