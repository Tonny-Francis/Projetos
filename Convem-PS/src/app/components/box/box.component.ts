import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-box',
  templateUrl: './box.component.html',
  styleUrls: ['./box.component.css']
})

export class BoxComponent implements OnInit {
  //Variáveis para interpolação
  empresa: string = 'Convem';
  value: String = '';

  //Funções
  button_click(){
    if(this.value.toLowerCase() === 'sim'){
      //Devemos chamar a API Rest e consultar a base de dados contendo a palavra sucesso
      console.log('Sucesso')
    }
    else{
      //Mensagem de erro
      alert('Erro')
    }
  }
  constructor() {
  }

  ngOnInit(): void {
  }

}
