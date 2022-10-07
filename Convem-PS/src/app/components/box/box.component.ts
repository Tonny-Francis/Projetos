import { Component, OnInit } from '@angular/core';

import { ApiService } from 'src/app/services/api.service';
import { Data } from 'src/app/interfaces/Data';

@Component({
  selector: 'app-box',
  templateUrl: './box.component.html',
  styleUrls: ['./box.component.css']
})

export class BoxComponent implements OnInit {
  //Variáveis para interpolação
  empresa: string = 'Convem';
  value: string = '';
  data: Data[] = []

  constructor(private apiservice: ApiService) {}

  ngOnInit(): void {}

  //Funções
  button_click(){
    if(this.value.toLowerCase() == 'sim'){
      //Devemos chamar a API Rest e consultar a base de dados contendo a palavra sucesso
      this.getData()
      console.log(this.data.values())
    }
    else{
      //Mensagem de erro
      alert('Erro')
    }
  }
  getData(): void{
    this.apiservice.getAll().subscribe((data) => this.data = data)
  }
}
