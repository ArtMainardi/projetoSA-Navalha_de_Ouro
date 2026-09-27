import mysql.connector

import banco
from config import DB_CONFIG
from models import Agendamento


def listar_agendamentos():
    conexao = None
    agendamentos = []
    try:
        conexao = banco.conectar()
        cursor = conexao.cursor()

        cursor.execute(f"select * from agendamentos order by data asc")
        lista = cursor.fetchall()
        if len(lista) > 0:
            for i in lista:
                agendamentos.append(Agendamento.reverte_tupla(i))
        else:
            print(f"Tabela de agendamentos vazia!")
        conexao.commit()
        return agendamentos

    except mysql.connector.Error as erro:
        print(f"Erro: {erro}")

    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def buscar_agendamento(id):
    conexao = None
    agendamento = None
    try:
        conexao = banco.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"select * from agendamentos where id = %s", (id,))
        agendamento_busca = cursor.fetchone()
        if agendamento_busca:
            agendamento = Agendamento.reverte_tupla(agendamento_busca)
        else:
            print(f"Agendamento não encontrado!")

        conexao.commit()
        return agendamento

    except mysql.connector.Error as erro:
        print(f"Erro: {erro}")

    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def listar_por_status(status):
    conexao = None
    agendamentos = None
    try:
        conexao = banco.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"select * from agendamentos where status = %s", (status,))
        agendamento_busca = cursor.fetchall()
        if agendamento_busca:
            agendamentos = Agendamento.reverte_tupla(agendamento_busca)
        else:
            print(f"Agendamentos não encontrados!")

        conexao.commit()
        return agendamentos

    except mysql.connector.Error as erro:
        print(f"Erro: {erro}")

    finally:
        if conexao and conexao.is_connected():
            conexao.close()