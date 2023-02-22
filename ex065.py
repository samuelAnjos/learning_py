media = contador  = soma = 0
maior = 0
menor = 10000
resposta = 's'
while resposta != 'n':
    numero = float(input('Digite numero'))
    soma += numero
    contador += 1
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    resposta = str(input('Deseja continuar [s/n]'))
print('Media: {:.2f}'.format(soma/contador))
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))

