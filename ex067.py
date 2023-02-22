valor = 0
i = 1
while True:

    valor = int(input('Quer ver a tabuada de qual valor?'))
    if valor < 0:
        break
    print('-' * 30)
    for i in range(1, 11):
        print(f'{valor} x {i} = {valor*i}')
    print('-' * 30)
