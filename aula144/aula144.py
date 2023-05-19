import mysql.connector

startServer = mysql.connector.connect(
    host="localhost",
    user="Joao Marcos",
    password="abc123",
    database="meusdados"
)

CursorServer = startServer.cursor()

sql = "DELETE FROM pessoas WHERE nome = %s"
valor = ('Danny',)
CursorServer.execute(sql, valor)
startServer.commit()
print(CursorServer.rowcount, "Registros excluidos")