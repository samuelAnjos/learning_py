def calculoFatorial(valor, show=False):
    fatorial = 1
    valorFinal = 0
    if show:
        for i in range(valor,0, -1):
            print(f'{i}', end=' ')
            if i > 1:
                print('x', end=' ')
            else:
                print(f'=', end=' ')
            fatorial *= i
        return fatorial
            #valorFinal += (i * v)
        #print(valorFinal)
    else:
        print('Não vádido')

print(calculoFatorial(5, show=True))

