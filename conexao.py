import mysql.connector 

def conectar_db():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "vetallis_db_2_0"
        )
        return connection
    except mysql.connector.Error as err:
        print(f'Erro na conexão {err}')
