import mysql.connector

from banco import DB_CONFIG

def conectar():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        return conexao
    except mysql.connector.Error as erro:
        print(f'Erro: {erro}')