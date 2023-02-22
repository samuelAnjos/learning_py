ficha = []

while True:
    nome = str(input('Informe nome:'))
    noteOne = float(input('Nota 1'))
    noteTwo = float(input('Nota 2'))
    media = (noteOne + noteTwo) / 2
    ficha.append([nome, [noteOne, noteTwo], media])

    response = str(input('Qur continuar [S/N]'))
    if response in 'Nn':
        break
print('=-' * 20)
print('"Number     Nome      Média"')
print('=-' * 18)
for ind, alu in enumerate(ficha):
    print(f'{ind:<12}{alu[0]:<10}{alu[2]:>6.1f}')

while True:
    opcao = int(input('Quer ver dados de qual aluno:  [999 interrompe]'))
    if opcao == 999:
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')

