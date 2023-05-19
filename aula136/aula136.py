import mysql.connector

startServer = mysql.connector.connect(
    host="localhost",
    user="Joao Marcos",
    password="abc123"
)

CursorServer = startServer.cursor()
#CursorServer.execute("CREATE DATABASE meusDados")
CursorServer.execute("show databases")
for x in CursorServer:
    print(x)
