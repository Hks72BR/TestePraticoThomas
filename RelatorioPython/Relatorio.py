import requests as re
import json
from pathlib import Path

response  = re.get('http://localhost:5221/Tarefa')
lista = response.text
lista_final = json.loads(lista)


TarefaFinalizada = 0
TarefaPendente = 0
TotalTarefas = 0

for chave in lista_final:
    if chave['finalizadoTarefa'] == True: TarefaFinalizada +=1
    if chave['finalizadoTarefa'] == False: TarefaPendente  +=1

TotalTarefas = TarefaFinalizada + TarefaPendente

TextoTotalTarefas = str(TotalTarefas) + " Tarefa(s) na lista."
TextoTarefasFinalizas = str(TarefaFinalizada) + " tarefa(s) finalizada(s)."
TextoTarefasPendentes = str(TarefaPendente) + " tarefa(s) pendente(s)."

desktop = Path.home() / "Desktop"

with open(desktop /'Relatório de tarefas.txt', 'w') as arquivo:
    arquivo.write(TextoTotalTarefas + "\n" + TextoTarefasFinalizas + "\n" + TextoTarefasPendentes)