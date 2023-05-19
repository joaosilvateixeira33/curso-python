import mysql.connector

banco_dados = mysql.connector.connect(
    host="localhost",
    user="Joao Marcos",
    password="abc123",
    database="meusdados"
)

CursorServer = banco_dados.cursor()

sql = ""

CursorServer.execute(sql)