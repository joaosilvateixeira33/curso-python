import mysql.connector

startServer = mysql.connector.connect(
    host="localhost",
    user="Joao Marcos",
    password="abc123",
    database="meusdados"
)

CursorServer = startServer.cursor()

sql = "UPDATE pessoas SET nome = %s WHERE id = %s"
dados_protegidos = ('Danny', '2')
CursorServer.execute(sql, dados_protegidos)
startServer.commit()
print(CursorServer.rowcount, "Registro(s) Afetado(s)")