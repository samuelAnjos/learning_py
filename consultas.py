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
def consulta(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado

v_sql = "SELECT * FROM tb_contatos"
res = consulta(v_conexao, v_sql)
for r in res:
    print(r)
