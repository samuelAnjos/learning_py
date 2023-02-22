import sqlite3
from sqlite3 import Error

def conexaoBanco():
    caminho = "D:\\1_python\\bd\\agenda.db"
    conexao = None

    try:
        conexao = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return conexao

v_conexao = conexaoBanco()


#deletar
def atualizar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro atualizado")

update = str(input('Qual o registro você deseja atualizar: '))
nome = str(input('Informe nome para atualizar: '))
v_sql = "UPDATE tb_contatos SET T_NOMECONTATO='"+nome+"' WHERE N_IDCONTATO = "+update+""

atualizar(v_conexao, v_sql)