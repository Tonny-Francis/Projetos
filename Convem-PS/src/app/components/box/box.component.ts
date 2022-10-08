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
  empresa: String = 'Convem';
  busca: any = 'sucesso';
  value: String = '';
  interface: Data[] = [];
  bool: boolean = false;
  tamanho: Number = 0;

  constructor(private apiservice: ApiService) {}

  ngOnInit(): void {}

  //Funções
  button_click(){
    if(this.value.toLowerCase() == 'sim'){
      //Devemos chamar a API Rest e consultar a base de dados contendo a palavra sucesso
      this.getData()
      setTimeout(() => {
        this.filter()
        console.log(this.bool)
      }, 1000);
    }
    else{
      //Mensagem de erro
      this.bool = false;
      alert('Erro')
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
      if(dado.data == 'data 2')
        this.bool = true;
      else
        this.bool = false;
    }
  }
}
