palavras = ('APRENDER', 'PROGRAMA', 'LINGUAGENS', 'PYTHON', 'CURSO', 'GRATIS')


for i in palavras:
    print(f'\nNa palavra {i} temos ',end=' ')
    for x in i:
        if x.lower() in 'aeiou':
            print(f'{x}',end='')

