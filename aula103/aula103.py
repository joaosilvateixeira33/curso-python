import json

x ='{"nome":"Joao", "idade":24, "cidade":"Rio de Janeiro"}'
y = json.dumps(x)

print(y)