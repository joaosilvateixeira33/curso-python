import json
x ='{"nome":"Joao", "idade":24, "cidade":"Rio de Janeiro"}'
y = json.loads(x)

print(y)
print(y["nome"])