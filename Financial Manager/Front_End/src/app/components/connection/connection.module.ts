import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';

import { LoginComponent } from './login/login.component';
import { SingInComponent } from './sing-in/sing-in.component';
import { ForgotPasswordComponent } from './forgot-password/forgot-password.component';
import { ConnectionComponent } from './connection.component';

const routes: Routes = [
  { path: 'forgot', component: ForgotPasswordComponent }
];

@NgModule({
  declarations: [
    LoginComponent,
    SingInComponent,
    ForgotPasswordComponent,
    ConnectionComponent
  ],
  imports: [
  RouterModule.forRoot(routes),
    CommonModule
  ],
  exports:[
    ConnectionComponent
  ]
})
export class ConnectionModule { }
