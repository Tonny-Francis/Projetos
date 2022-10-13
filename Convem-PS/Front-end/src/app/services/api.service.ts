import { Injectable } from '@angular/core';

import {HttpClient, HttpHeaders} from '@angular/common/http'
import { firstValueFrom } from 'rxjs';
import { Answer } from '../interfaces/Answer';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl: string = 'https://convemapi.herokuapp.com/answer'
  constructor(private httpClient: HttpClient) { }

  postAll(answer:Answer){
    return firstValueFrom(this.httpClient.post<Answer>(this.apiUrl, answer))
  }
}
