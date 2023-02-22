import datetime
from datetime import date
from datetime import datetime
information = dict()

information['nome'] = str(input('Informe nome:'))
dateBorn = int(input('Informe seu ano de nascimento'))
currentDate = datetime.datetime.now()
date = currentDate.date()
idade = date.year - dateBorn
information['idade'] = idade
information['carteitaTrabalho'] = int(input('Digite o numero da carteira de trabalho'))

if information['carteitaTrabalho'] != 0:
    information['yearContract'] = int(input('Qual o ano de contratação'))
    information['salario'] = float(input('Informe seu salário:'))
    information['adeAposento'] = information['idade'] + (information['yearContract'] + 35) - datetime.now().year()
    print('-='*30)
for key, value in information.items():
    print(f'{key} tem o valor {value}')


'''
como pegar o ano atual
fron datetime import datetime
ano = datetime.now().year - anoNascimento
'''


