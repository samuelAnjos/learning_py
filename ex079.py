numbers = list()
while True:
    num = (int(input('Digite um valor: ')))
    if num not in numbers:
        numbers.append(num)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Não vou adicionar...')

    resposta = str(input('Quer continuar [s/n]')).lower()
    if resposta == 'n':
        break
numbers.sort()
print(f'Você digitou os valores {numbers}')

