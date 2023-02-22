def maior(* numemos):
    maior = 0
    print('Os valores digitados foram: ', end=' ')
    for i in numemos:
        print(f'{i}', end= ' ')
        if i > maior:
            maior = i
    print(f'\nO maior valor {maior}')

maior(1, 2, 9, 4, 5, 6)



