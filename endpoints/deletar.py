import mysql.connector
from conexao import conectar_db

def deletar_usuario_bd(usuario_id):
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM usuario WHERE usuario_id = %s"
            values = ((usuario_id), )
            cursor.execute(sql, values)
            conn.commit()
            return {'status': 'sucesso', 'mensagem': f"usuario {usuario_id} deletado com sucesso!"}
        except mysql.connector.Error as err:
            print(f'Erro: {err}')
            return {'status': 'erro', 'mensagem': f"Erro ao deletar usuario|:{err}"}
        finally:
            cursor.close()
            conn.close()