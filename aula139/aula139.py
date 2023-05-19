import mysql.connector

startServer = mysql.connector.connect(
    host="localhost",
    user="Joao Marcos",
    password="abc123",
    database="meusdados"
)

CursorServer = startServer.cursor()

#sql = "alter table pessoas add sobrenome varchar(255)"
sql = "ALTER TABLE pessoas ADD id INT AUTO_INCREMENT PRIMARY KEY FIRST"

CursorServer.execute(sql)