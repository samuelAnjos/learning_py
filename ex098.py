import time
def contador(inicio, fim, passo):

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ')
            time.sleep(1)
            cont+= passo
    else:
        cont = inicio
        print()
        while cont >= fim:
            print(f'{cont}', end=' ')
            time.sleep(1)
            cont -= passo
        print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar sua contagem')
inicio = int(input('Incio'))
fim = int(input('Fim'))
passo = int(input('passo'))
contador(inicio, fim, passo)

