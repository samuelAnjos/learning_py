def area(largura, comprimento):
    print(f'A area de um terrno {largura}x{comprimento} é {largura*comprimento}')


print('Controle de terreno')
print('-------------------')
largura = float(input('Informe a largura do terreno (m)'))
comprimento = float(input('Informe o comprimento do terreno (m)'))
area(largura, comprimento)