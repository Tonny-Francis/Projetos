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
    console.log('click')
  }
  getData(): void{
    this.apiservice.getAll().subscribe((data) => this.interface = data)
  }
}
