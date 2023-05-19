import mysql.connector

startServer = mysql.connector.connect(
    host="localhost",
    user="Joao Marcos",
    password="abc123",
    database="meusdados"
)

CursorServer = startServer.cursor()

sql = "SELECT * FROM pessoas"
CursorServer.execute(sql)
#resultado_busca = CursorServer.fetchall()
resultado_busca = CursorServer.fetchone()

# for x in resultado_busca:
#    print(x)

print(resultado_busca)