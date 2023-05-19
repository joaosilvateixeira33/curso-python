import mysql.connector

startServer = mysql.connector.connect(
    host="localhost",
    user="Joao Marcos",
    password="abc123",
    database="meusdados"
)

CursorServer = startServer.cursor()

sql = """create table pessoas 
    (nome varchar(255), 
    idade int(2))"""

CursorServer.execute(sql)