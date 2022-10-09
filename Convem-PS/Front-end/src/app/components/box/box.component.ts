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
  interface: Data[] = [];

  constructor(private apiservice: ApiService) {}

  ngOnInit(): void {}

  //Funções
  button_click(){
    if(this.value == 'sim')
      console.log(this.getData('sim'))
    else
      console.log(this.getData('nao'))
  }
  getData(answer: string): void{
    this.apiservice.getAll(answer).subscribe((data) => this.interface = data)
  }
}
