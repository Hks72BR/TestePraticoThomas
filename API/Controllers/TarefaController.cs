using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using API.ListaTemporaria;
using API.Model;

namespace API.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class TarefaController : ControllerBase
    {

        [HttpPost]
        public Model.TarefaModel Salvar(Model.TarefaModel tarefa)
        {
            ListaDeTarefas.Lista.Add(tarefa);

            return tarefa;
        }

        [HttpGet]
        public List<Model.TarefaModel> Consultar()
        {
            ListaTemporaria.ListaDeTarefas lista = new ListaTemporaria.ListaDeTarefas();

            List<Model.TarefaModel> tarefas = ListaDeTarefas.Lista.ToList();

            return tarefas;
        }

        [HttpPut]
        public void Alterar (Model.TarefaModel tarefa)
        {
            Model.TarefaModel atual = ListaDeTarefas.Lista.First(x => x.ID == tarefa.ID);
            atual.Titulo = tarefa.Titulo;
            atual.Descricao = tarefa.Descricao;
            atual.FinalizadoTarefa = tarefa.FinalizadoTarefa;
        }

        [HttpDelete]
        public void Remover (int tarefa)
        {
            Model.TarefaModel atual = ListaDeTarefas.Lista.First(x => x.ID == tarefa);

            ListaDeTarefas.Lista.Remove(atual);         
        }
    }
}
