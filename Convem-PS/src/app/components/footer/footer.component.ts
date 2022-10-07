import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {
  //Links das redes sociais
  facebook = ['https://www.facebook.com/Convem.Store', '../../../assets/Facebook 30x30.png'];
  instagram = ['https://www.instagram.com/convem.store/', '../../../assets/Instagram 30x30.png'];
  linkedin = ['https://www.linkedin.com/company/convem---loja-online/', '../../../assets/Linkedin 30x30.png']
  website = ['https://www.convemstore.com/', '../../../assets/Internet 30x30.png']

  //Nomes
  empresa: string = 'Convem Stores';

  constructor() {}

  ngOnInit(): void {
  }

}
