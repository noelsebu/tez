import { Injectable } from '@angular/core';
import { MatTableDataSource } from '@angular/material';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'environments/environment';


@Injectable({
  providedIn: 'root'
})
export class TableService {
  baseUrl = environment.baseUrl;
  private data: MatTableDataSource<any[]>;
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
    }
  getselected(): MatTableDataSource<any[]> {
    console.log('I am selected');
    return this.data;
  }
  postresponsefinal(data) {
    console.log('inside resojcd');
    const url = this.baseUrl + '/testcases/';
    return this.httpClient.post<any[]>(url, data);
    // return this.httpClient.post<any[]>('/api/testcases/', data);
  }

  postcredentials(data) {
    console.log('inside credentials');
    const url = this.baseUrl + '/users/';
    return this.httpClient.post<any[]>(url, data);
    // return this.httpClient.post<any[]>('/api/testcases/', data);
  }

}

