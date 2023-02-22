mais18 = totalMan = totalWoman = 0
while True:
    idade = int(input('Informe a sua idade'))

    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input("Informe o seu sexo [M/F]")).strip().lower()[0]

    if idade > 18:
        mais18 += 1

    if sexo == 'm':
        totalMan += 1

    if sexo == 'f' and idade < 20:
        totalWoman += 1

    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input('Desejas continuar? [S/N]')).strip().lower()[0]

    if resposta == 'n':
        break
print(f'Total de pessoas com mais de 18 anos {mais18}')
print(f'Total de homens {totalMan}')
print(f'Total de mulheres com menos de 20 anos {totalWoman}')

