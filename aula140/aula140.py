import mysql.connector

startServer = mysql.connector.connect(
    host="localhost",
    user="Joao Marcos",
    password="abc123",
    database="meusdados"
)

CursorServer = startServer.cursor()


#sql = "INSERT INTO pessoas(id, nome, sobrenome,idade) VALUES (NULL, 'João Marcos', 'Silva','24')"
sql = "INSERT INTO pessoas(id, nome, sobrenome,idade) VALUES (NULL, %s, %s, %s)"
val = ("Danny", "Logan", "35")

CursorServer.execute(sql, val)
startServer.commit()
print(CursorServer.rowcount, "Registros inseridos")