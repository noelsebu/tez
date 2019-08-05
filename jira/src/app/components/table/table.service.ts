import { Injectable } from '@angular/core';
import { MatTableDataSource } from '@angular/material';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TableService {
  private data: MatTableDataSource<any[]>;
  url: any  = 'http://localhost:8081/testcases/';
  constructor(private httpClient: HttpClient) { }
  getresponse() {
    return this.httpClient.get<MatTableDataSource<any[]>>('./assets/data.json', { responseType: 'json' });
  }


  postresponse(data) {
    console.log('inside resojcd');
    const httpOptions = new HttpHeaders({
        'Content-Type' : 'application/json'
      });
    this.data = data;
    // return this.httpClient.post<any[]>('/api/test', data, {headers: httpOptions});

    // return this.httpClient.post<any[]>('http://localhost:4200/test ', data, {headers: httpOptions} );
    }
  getselected(): MatTableDataSource<any[]> {
    console.log('I am selected');
    return this.data;
  }
  postresponsefinal(data) {
    console.log('inside resojcd');
    // const httpOptions = new HttpHeaders({
    //    'Content-Type' : 'application/json'
    //  });
    // this.data = data;
    return this.httpClient.post<any[]>(this.url, data);
          // {headers: httpOptions});
    // return this.httpClient.post<any[]>('/api/test', data, {headers: httpOptions});
    // return this.httpClient.post<any[]>('http://localhost:4200/test ', data, {headers: httpOptions} );
    }
}

