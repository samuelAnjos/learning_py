import random
numeros = [1,2,3,4,5]
escolhido = random.choice(numeros)
print('\033[33m_\033[m'* 36)
print('\033[1;34m         JOGO DA DESCOBERTA         \033[m')
print('\033[33m_\033[m'* 36)
numeroUsuario = float(input('Digite um número para saber se bate com o do jogo!'))
if escolhido == numeroUsuario:
    print('Parabéns! Você acertou!')
else:
    print('Número não corresponde ')
print('Fim do jogo!')
print(escolhido)