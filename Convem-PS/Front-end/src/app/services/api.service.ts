import { Injectable } from '@angular/core';

import {HttpClient, HttpHeaders} from '@angular/common/http'
import { Observable } from 'rxjs';
import { Data } from '../interfaces/Data';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl: string = 'https://convemapi.herokuapp.com/sim'
  constructor(private http: HttpClient) { }

  getAll(answer: string): Observable<Data[]>{
    return this.http.get<Data[]>(this.apiUrl)
  }
}
