reta1 = float(input('Informe comprimento da reta 1'))
reta2 = float(input('Informe comprimento da reta 2'))
reta3 = float(input('Informe comprimento da reta 3'))

if reta1 + reta2 > reta3 and reta3 + reta1 > reta2 and reta2 + reta3 > reta1:
    print('Forma triângulo')
else:
    print('Não forma triângulo')