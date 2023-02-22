from datetime import date
nascimento = int(input('Digite seu ano de nascimento'))
dataAtual = date.today()
diferencaIdade = dataAtual.year - nascimento
print(diferencaIdade)
if diferencaIdade < 18:
    print('Vc ainda vai ter que ir! Falta {} anos'.format(18-diferencaIdade))
    saldo = (18-diferencaIdade) + dataAtual.year
    print('Seu alistamento sera {}'.format(saldo))
elif diferencaIdade == 18:
    print('Esta na hora de se alistar')
else:
    saldo = dataAtual.year -(diferencaIdade-18)
    print('Ja passou o tempo! Passou {} anos'.format(diferencaIdade-18))
    print('Seu alistamento seria {}'.format(saldo))

