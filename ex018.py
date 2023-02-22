import math
angulo = float(input('Informe o angulo'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Seno {:.2f}, Cosseno {:.2f} e Tangente {:.2f} de Angulo {}'.format(seno, cosseno, tangente, angulo))