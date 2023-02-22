import sqlite3
from sqlite3 import Error

########## Criando conexao com o banco de dados
def ConexaoBanco():
    caminho = "D:\\1_python\\bd\\agenda.db"
    conexao = None
    try:
        conexao = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return conexao

vconexao = ConexaoBanco()

nome = input(str('Informe o seu nome: '))
telefone = input(str('Informe o seu telefone: '))
email = input(str('Informe o seu email: '))

variavelSQL = "INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) values('"+nome+"','"+telefone+"','"+email+"')"

def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro Inserido')
    except Error as ex:
        print(ex)

inserir(vconexao, variavelSQL)
