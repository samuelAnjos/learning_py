aluno = dict()
aluno['nome'] = str(input('Informe seu nome: '))
aluno['media'] = float(input('Qual a sua media'))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

for k , v in aluno.items():
    print(f'{k} é igual a {v}')