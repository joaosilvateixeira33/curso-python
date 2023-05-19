import json

x ='{"nome": "Joao", "idade": 24, "cidade": "Rio de Janeiro"}'
print(json.dumps(x, indent=6, separators=(" | ", " = ")))