def leiaInt(mensagem):

    ok = False
    valor = 0
    while True:
        n = str(input(mensagem))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um numero inteiro valido')
        if ok:
            break
    return valor

#prograPrincipal
n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}:')