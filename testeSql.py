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

#Criar tabela
vaql = """ CREATE TABLE TB_CONTATOS(
                N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
                T_NOMECONTATO VARCHAR(30),
                T_TELEFONECONTATO VARCHAR(14),
                T_EMAILCONTATO VARCHAR(30)
           );"""

def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print('Tabela Criada')
    except Error as ex:
        print(ex)

criarTabela(vconexao, vaql)

vconexao.close()


