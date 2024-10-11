# ToDo API - ASP.NET Core com Integração Python

## Descrição

Este projeto é uma API REST simples criada com ASP.NET Core, que permite gerenciar uma lista de tarefas (ToDo List). Além das operações CRUD (Criar, Ler, Atualizar, Deletar) de tarefas, a API integra-se com um script Python para gerar um relatório das tarefas.

### Funcionalidades da API:

- Adicionar novas tarefas
- Listar todas as tarefas
- Atualizar uma tarefa existente
- Deletar tarefas
- Gerar um relatório básico de tarefas (número total, concluídas e pendentes)

A integração com Python ocorre na rota `/api/todo/report`, onde a API gera um arquivo JSON contendo as tarefas, chama um script Python que processa o arquivo e gera um relatório em formato `.txt`.

## Tecnologias Utilizadas

- **C# (ASP.NET Core)**
- **Python 3**

## Requisitos

- **.NET Core SDK**
- **Python 3** (deve estar configurado no `PATH` do sistema)

