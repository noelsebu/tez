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
    // retrives jira information
    const url= this.baseUrl + '/jira/';
    return this.httpClient.get<MatTableDataSource<any[]>>(url);
    // return this.httpClient.get<MatTableDataSource<any[]>>('./assets/data.json', { responseType: 'json' });
  }


  postresponse(data) {
    // passes the info to review component
    console.log('inside resojcd');
    const httpOptions = new HttpHeaders({
        'Content-Type' : 'application/json'
      });
    this.data = data;
    }
  getselected(): MatTableDataSource<any[]> {
    // takes the selected testcases and intializes this.data  with it 

    console.log('I am selected');
    return this.data;
  }
  postresponsefinal(data) {
    // posts the selected testcases to the server
    console.log('inside resojcd');
    const url = this.baseUrl + '/testcases/';
    return this.httpClient.post<any[]>(url, data);
    // return this.httpClient.post<any[]>('/api/testcases/', data);
  }

  postcredentials(data) {
    // posts the git crdentials and authokens to the server
    console.log('inside credentials');
    const url = this.baseUrl + '/users/';
    return this.httpClient.post<any[]>(url, data);
    // return this.httpClient.post<any[]>('/api/testcases/', data);
  }

}

