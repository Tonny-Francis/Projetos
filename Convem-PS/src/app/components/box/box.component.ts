import { Component, OnInit } from '@angular/core';

import { ApiService } from 'src/app/services/api.service';
import { Data } from 'src/app/interfaces/Data';
import { ThisReceiver } from '@angular/compiler';

@Component({
  selector: 'app-box',
  templateUrl: './box.component.html',
  styleUrls: ['./box.component.css']
})

export class BoxComponent implements OnInit {
  //Variáveis para interpolação
  empresa: string = 'Convem';
  busca: string = 'data 2';
  erro: string = 'Erro'
  value: string = '';
  interface: Data[] = [];
  bool: boolean = false;
  valueCompared: string = 'sim';

  constructor(private apiservice: ApiService) {}

  ngOnInit(): void {}

  //Funções
  button_click(){
    if(this.value.toLowerCase() == this.valueCompared){
      //Devemos chamar a API Rest e consultar a base de dados contendo a palavra sucesso
      this.getData()
      setTimeout(() => {
        this.filter()
      }, 1000);
    }
    else{
      //Mensagem de erro
      this.bool = false;
      alert(this.erro)
    }
  }
  getData(): void{
    this.apiservice.getAll().subscribe((data) => this.interface = data)
  }
  filter(){
    this.interface = this.interface.filter(
    function(obj)
    {
      return obj.data == 'data 2'
    })
    for(let dado of this.interface)
    {
      if(dado.data == this.busca)
        this.bool = true;
      else
        this.bool = false;
    }
  }
}
