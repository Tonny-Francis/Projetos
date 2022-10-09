import { Component, OnInit } from '@angular/core';

import { ApiService } from 'src/app/services/api.service';
import { Data } from 'src/app/interfaces/Data';
import { MatDialog } from '@angular/material/dialog';
import { DialogComponent } from '../dialog/dialog.component';

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

  constructor(
    private apiservice: ApiService,
    public dialog: MatDialog) {}

  ngOnInit(): void {}

  //Funções
  button_click(){
    if(this.value == 'sim'){
      this.getData('sim')
      setTimeout(() => {
        for(let answer of this.interface){
          if(answer.answer == 'sucesso')
            this.openDialog()
          else
            alert('Erro Database')
        }
      }, 1000);
    }
    else{
      this.getData('nao')
      setTimeout(() => {
        for(let answer of this.interface){
          if(answer.answer == 'erro')
            alert('Erro')
          else
            alert('Erro Database')
        }
      }, 1000);
    }

  }
  getData(answer: string): void{
    this.apiservice.getAll(answer).subscribe((data) => this.interface = data)
  }
  openDialog(): void {
    const dialogRef = this.dialog.open(DialogComponent, {
      width: '350px',
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
  }
}
