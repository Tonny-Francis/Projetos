import { Component, OnInit } from '@angular/core';

import { ApiService } from 'src/app/services/api.service';
import { Answer } from 'src/app/interfaces/Answer';
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
  error_messager: string = 'Erro'
  sucesso: string ='Sucesso'

  constructor(
    private apiservice: ApiService,
    public dialog: MatDialog) {}

  ngOnInit(): void {}

  //Funções
  Enviar(){
    if(!this.value)
      alert(this.error_messager)
    else
      this.addAnswer()
  }

  addAnswer(): void{
    const answer:Answer = {
      answer: this.value.toLowerCase()
    }

    this.apiservice.postAll(answer)
      .then(answer => {
        if(answer.answer == this.sucesso)
          this.openDialog()
        else
          alert(this.error_messager)
      })
  }

  openDialog(): void {
    const dialogRef = this.dialog.open(DialogComponent, {
      width: '350px',
    });

    dialogRef.afterClosed().subscribe(result => {

    });
  }
}
