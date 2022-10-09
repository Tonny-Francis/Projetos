import { Injectable } from '@angular/core';

import {HttpClient, HttpHeaders} from '@angular/common/http'
import { Observable } from 'rxjs';
import { Data } from '../interfaces/Data';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl: string = 'https://633f2d4c0dbc3309f3c64f7d.mockapi.io/api/v1/'
  constructor(private http: HttpClient) { }

  getAll(answer: string): Observable<Data[]>{
    return this.http.get<Data[]>(this.apiUrl+answer)
  }
}
