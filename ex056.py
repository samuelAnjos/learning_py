totalIdade = 0
maisVelho = 0
totalMulheres = 0
nomeMaisVelho = ''
for c in range(1, 5):
    nome = str(input('Infome o nome da  primeira pessoa'))
    idade = int(input('Digite idade'))
    sexo = str(input('Informe o sexo [f]/[m]')).lower()

    totalIdade += idade #total de idade

    if sexo == 'm':  # o homem mais velho
        if idade > maisVelho:
            maisVelho = idade
            nomeMaisVelho = nome

    if sexo in 'Ff': # total de mulheres com menos de 20 anos
        if idade < 20:
            totalMulheres += 1

print('Media de idades {}'.format(totalIdade/4))
print('Nome do homem mais velho {}'.format(nomeMaisVelho))
print('Quantas mulheres tem mais de 20 anos {}'.format(totalMulheres))

