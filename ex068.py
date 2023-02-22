from random import randint
while True:
    valorUsuario = int(input('Digite um valor'))
    valorPc = randint(0, 10)
    soma = valorUsuario + valorPc
    parImpar = ' '
    while parImpar not in 'PI':
        parImpar = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Voce jogou {valorUsuario} e o computador {valorPc}. Total de {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if parImpar == 'P':
        if soma % 2 == 0:
            print('Voce GANHOU')
        else:
            print('Voce PERDEU')
            break
    elif parImpar == 'I':
        if soma % 2 == 1:
            print('Voce GANHOU')
        else:
            print('Voce PERDEU')
            break
    print('Vamos jogar novamente')
print('GAME OVER')

