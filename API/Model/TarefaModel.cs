using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace API.Model
{
    public class TarefaModel
    {
        
        public int ID { get; set; }
        public string Titulo { get; set; }
        public string Descricao { get; set; }
        public bool FinalizadoTarefa { get; set; }


    }
}