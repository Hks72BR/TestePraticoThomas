import requests as re
import json

response  = re.get('http://localhost:5221/Tarefa')
lista = response.text
lista_final = json.loads(lista)


TarefaFinalizada = 0
TarefaPendente = 0

for chave in lista_final:
    if chave['finalizadoTarefa'] == True: TarefaFinalizada +=1
    if chave['finalizadoTarefa'] == False: TarefaPendente  +=1

TextoTarefasFinalizas = str(TarefaFinalizada) + " tarefa(s) finalizada(s)."
TextoTarefasPendentes = str(TarefaPendente) + " tarefa(s) pendente(s)."

with open('Relatório de tarefas.txt', 'w') as arquivo:
    arquivo.write(TextoTarefasFinalizas + "\n" + TextoTarefasPendentes)
        