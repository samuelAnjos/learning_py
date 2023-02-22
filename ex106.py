import os
carros = list()

class Carro:
    nome = ''
    potencia = 0
    valocidadeMaxima = 0
    ligado = False

    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia
        self.valocidadeMaxima = potencia * 2
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def info(self):
        print(f'Nome..............{self.nome}')
        print(f'Potencia..........{self.potencia}')
        print(f'Velocidade Maxima.{self.valocidadeMaxima}')
        print(f'Ligado............{"Sim" if self.ligado == True else "Não"}')

def Menu():
    os.system("cls") or None
    print('1 - Novo Carro')
    print('2 - Info Carro')
    print('3 - Excluir Carro')
    print('4 - Ligar Carro')
    print('5 - Desligar Carro')
    print('6 - Listar Carro')
    print('7 - Sair')
    opc = input('Digite uma Opcao: ')
    return opc

def NovoCarro():
    os.system("cls") or None
    nome = input('Nome do carro:')
    potencia = input('Potencia do carro')
    carro = Carro(nome, potencia)
    carros.append(carro)
    print('New car create')
    os.system('pause')

def informacoes():
    os.system("cls") or None
    number = input('Informe o nome do carro que deseja ver as informações:')

    try:
        print(carros[int(number)].info())
    except:
        print('Car not exists')
    os.system('pause')

def excluirCarro():
    os.system("cls") or None
    number = input('Informe o nome do carro que deseja excluir')
    try:
        del carros[int(number)]
    except:
        print('Carro not exists')
    os.system('pause')

def LigarCarro():
    os.system("cls") or None
    number = input('Informe o nome do carro que deseja ligar:')
    try:
        carros[int(number)].ligar()
    except:
        print('Carro not exists')
    os.system('pause')

def DesligarCarro():
    os.system("cls") or None
    number = input('Informe o nome do carro que deseja desligar:')
    try:
        carros[int(number)].desligar()
        print('Carro desligado')
    except:
        print('Carro not exists')
    os.system('pause')

def listarCarros():
    os.system("cls") or None
    p = 0
    for i in carros:
        print(f'{p} " - " {i.nome}')
        p += 1
    os.system('pause')

resposta = Menu()
while resposta < '7':
    if resposta == '1':
        NovoCarro()
    elif resposta == '2':
        informacoes()
    elif resposta == '3':
        excluirCarro()
    elif resposta == '4':
         LigarCarro()
    elif resposta == '5':
        DesligarCarro()
    elif resposta == '6':
        listarCarros()
    resposta = Menu()

os.system('cls') or None
print('Programa finalizado')





