pessoa = {}
galera = []
mulheres = []
soma = 0
while True:
    pessoa['nome'] = str(input('Informe o nome'))
    sex = str(input('Informe o sexo'))[0]
    while sex not in 'MmFf':
        print('ERRO! Por favor, digite apenas M ou F.')
        sex = str(input('Informe o sexo'))[0]
        if sex in 'MmFf':
            break
    if sex in 'Ff':
        mulheres.append(pessoa['nome'])

    pessoa['sexo'] = sex

    pessoa['idade'] = int(input('Digite a sua idade'))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    response = str(input('Deseja continuar [S/N]'))[0]
    if response in 'Nn':
        break
print('-=' * 30)
print(f'Total de pessoas cadastradas: {len(galera)}')
print(f'Média de idade: {soma/len(galera)}')
print(f'Lista com todas as mulheres {mulheres}')
print('Pessoas com idade acima da Média: ',end=' ')
for p in galera:
    if p['idade'] >= soma/len(galera):
        print(p['nome'], end=' ')

