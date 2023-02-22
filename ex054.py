from datetime import date
ano = date.today().year
contadorMaior = 0
contadorMenor = 0
for c in range(1, 8):
    anoNascimento = int(input('Informe o ano do seu nascimento'))
    if(ano-anoNascimento >= 18):
        contadorMaior += 1
    else:
        contadorMenor += 1
print('Maiores de 18 anos {}'.format(contadorMaior))
print('Menores de 10 anos {}'.format(contadorMenor))


