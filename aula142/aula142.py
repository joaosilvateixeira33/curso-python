import mysql.connector

startServer = mysql.connector.connect(
    host="localhost",
    user="Joao Marcos",
    password="abc123",
    database="meusdados"
)

CursorServer = startServer.cursor()

sql = "SELECT * FROM pessoas WHERE sobrenome = 'Silva'"
CursorServer.execute(sql)
resultado_busca = CursorServer.fetchall()

for x in resultado_busca:
    print(x)