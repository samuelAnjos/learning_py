numberOne = float(input('Digite o 1º numero'))
numberTwo = float(input('Digite o 2º numero '))
resposta = 0

while resposta != 5:
    resposta = int(input('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos Numeros\n[5]Sair do Programa\n'))

    if resposta == 1:
        soma = numberOne + numberTwo
        print('Soma entre {} + {} = {}'.format(numberOne, numberTwo, soma))
    elif resposta == 2:
        multiplicar = numberOne * numberTwo
        print('Multiplicação entre {} x {} = {}'.format(numberOne, numberTwo, multiplicar))
    elif resposta == 3:
        if (numberOne > numberTwo):
            maior = numberOne
        else:
            maior = numberTwo
        print('O maior {}'.format(maior))
    elif resposta == 4:
        numberOne = float((input('Digite o 1º numero')))
        numberTwo = float(input('Digite o 2º numero '))




