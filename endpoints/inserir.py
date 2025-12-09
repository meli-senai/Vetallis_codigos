from conexao import conectar_db
import mysql.connector

def adicionar_usuario(dados):
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO usuario (usuario_senha, usuario_email, usuario_nome, usuario_cpf, usuario_cargo) values (%s, %s, %s, %s, %s)"
            values = (dados['senha'], dados['email'], dados['nome'], dados['cpf'], dados['cargo'])
            cursor.execute(sql, values)
            conn.commit()
            return True
        except mysql.connector.Error as err:
            print(f'erro {err}')
        finally:
            cursor.close()
            conn.close()
