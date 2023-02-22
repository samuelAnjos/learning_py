import os
import random
from colorama import Fore, Back, Style

jogarNovamente = 's'
jogadas = 0
quemJoga = 2
maximoJogadas = 9
vit = 'n'
velha = [
         [' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']
        ]

def showTela():
    global velha
    global jogadas
    os.system('cls')
    print('    0   1   2')
    print(f'0:  {velha[0][0]}  |  {velha[0][1]}| {velha[0][2]}' )
    print('---------------')
    print(f'1:  {velha[1][0]}  |  {velha[1][1]}| {velha[1][2]}')
    print('---------------')
    print(f'2:  {velha[2][0]}  |  {velha[2][1]}| {velha[2][2]}')
    print(f'Jogadas: {Fore.BLUE + str(jogadas) + Fore.RESET}')

def jogadorJoga():
    global jogadas
    global quemJoga
    global maximoJogadas

    if quemJoga == 2 and jogadas < maximoJogadas:

        try:
            linha = int(input('Informe linha :'))
            coluna = int(input('Informe coluna :'))
            while velha[linha][coluna] != " ":
                linha = int(input('Informe linha :'))
                coluna = int(input('Informe coluna :'))
            velha[linha][coluna] = 'X'
            quemJoga = 1
            jogadas += 1
        except:
            print('Linha e/ou coluna inválida!')
            os.system('pause')

def cpuJogar():
    global jogadas
    global quemJoga
    global maximoJogadas
    if quemJoga == 1 and jogadas < maximoJogadas:
        # cpu aleatorio
        linha = random.randrange(0,3)
        coluna = random.randrange(0,3)
        velha[linha][coluna] = 'O'
        quemJoga = 2
        jogadas += 1

def verificarVitoria():
    global velha
    vitoria = 'n'
    simbolos = ['X', 'O']
    for s in simbolos:
        vitoria = 'n'
        #verificar linhas
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if velha[il][ic] == s:
                    soma += 1
                ic += 1
            if soma == 3:
                vitoria = s
                break
            il += 1
        if vitoria != 'n':
            break

        #verificar colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if velha[il][ic] == s:
                    soma += 1
                il += 1
            if soma == 3:
                vitoria = s
                break
            ic += 1
        if vitoria != 'n':
            break

        #verificar diagonal 1

        soma = 0
        indiceDiagonal= 0
        while indiceDiagonal < 3:
            if velha[indiceDiagonal][indiceDiagonal] == s:
                soma += 1
            indiceDiagonal += 1
        if soma == 3:
            vitoria = s
            break

            # verificar diagonal 2

            soma = 0
            indiceDiagonalL = 0
            indiceDiagonalC = 2
            while indiceDiagonalC >= 0:
                if velha[indiceDiagonalL][indiceDiagonalC] == s:
                    soma += 1
                indiceDiagonalL += 1
                indiceDiagonalC -= 1
            if soma == 3:
                vitoria = s
                break
        return vitoria

def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maximoJogadas
    global vit
    jogadas = 0
    quemJoga = 2
    maximoJogadas = 9
    vit = 'n'
    velha = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

while jogarNovamente == 's':
    while True:
        showTela()
        jogadorJoga()
        cpuJogar()
        showTela()
        vit = verificarVitoria()
        if vit != 'n' or jogadas >= maximoJogadas:
            break

    print(Fore.RED + 'FIM DE JOGO' + Fore.YELLOW)
    if vit == 'X' or vit == 'O':
        print(f'O resultado: Jogador {vit} venceu')
    else:
        print('Houve empate')

    jogarNovamente = input(Fore.BLUE + 'Jogar Novamente? [S/N]: ' + Fore.RESET)
    redefinir()
