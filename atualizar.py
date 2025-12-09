import mysql.connector 
from conexao import conectar_db

def atualizar_usuario(dados):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        try:
            
            sql = "UPDATE usuario SET usuario_nome = %s WHERE usuario_id = %s"
            values = (dados['nome'], dados['usuario_id'])
            cursor.execute(sql, values)
            conn.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
        finally:
            cursor.close()
            conn.close()