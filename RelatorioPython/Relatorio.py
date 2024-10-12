import json

with open("http://localhost:5221/Tarefa") as tarefas:
    dados = json.load(tarefas)

print (dados)