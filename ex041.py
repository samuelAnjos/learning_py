from datetime import date
ano = date.today().year
anoNascimento = int(input('Informe ano de nascimento'))
anosAtleta = ano - anoNascimento
if anosAtleta <= 9:
    print('vc tem {} anos, entao é mirim'.format(anosAtleta))
elif anosAtleta <= 14:
    print('vc tem {} anos, entao é infantil'.format(anosAtleta))
elif anosAtleta <= 19:
    print('junior')
elif anosAtleta <= 20:
    print('senior')
else:
    print('master')
