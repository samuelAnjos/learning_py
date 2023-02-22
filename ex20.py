from random import shuffle
nome1 = input('Informe o nome do primeiro aluno')
nome2 = input('Informe o nome do segundo aluno')
nome3 = input('Informe o nome do 3 aluno')
nome4 = input('Informe o nome do 4 aluno')
alunos = [nome1, nome2, nome3, nome4]
shuffle(alunos)
print(alunos)