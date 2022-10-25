import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  title: string = 'Login'
  fields: string[] = ['Email', 'Password', 'Forgot Password']
  logo: string = '../../assets/Logo.png'
  constructor() { }

  ngOnInit(): void {
  }

}
