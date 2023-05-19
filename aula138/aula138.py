import mysql.connector

startServer = mysql.connector.connect(
    host="localhost",
    user="Joao Marcos",
    password="abc123",
    database="meusdados"
)

CursorServer = startServer.cursor()

#sql = "alter table pessoas add sobrenome varchar(255)"
sql = "alter table pessoas drop sobrenome"

CursorServer.execute(sql)