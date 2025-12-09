import mysql.connector
from conexao import conectar_db

def consultar_usuario():
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "SELECT * FROM usuario"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            return resultado
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
        finally:
            cursor.close()
            conn.close()