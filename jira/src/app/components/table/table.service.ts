import { Injectable } from '@angular/core';
import { MatTableDataSource } from '@angular/material';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TableService {
  constructor(private httpClient: HttpClient) { }
  getresponse() {
    return this.httpClient.get<MatTableDataSource<any[]>>('./assets/data.json', { responseType: 'json' });
  }


  postresponse(data) {
    console.log('inside resojcd');
    const httpOptions = new HttpHeaders({
        'Content-Type' : 'application/json'
      });

    return this.httpClient.post<any[]>('/api/test', data, {headers: httpOptions});

    // return this.httpClient.post<any[]>('http://localhost:4200/test ', data, {headers: httpOptions} );
    }
}

