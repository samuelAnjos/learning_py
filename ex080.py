lista = []
for c in range(0,5):
    numero = int(input('Digite um valor'))

    if c == 0 :
        lista.append(numero)
        print('Adicionado no inicio')
    elif numero > lista[-1]:
        lista.append(numero)
        print('Adicionado no fim')
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos,numero)
                print(f'Adicionado na posicao {pos}')
                break
            pos += 1
print('=-' * 30)
print(f'Os valores inseridos foram {lista}')


