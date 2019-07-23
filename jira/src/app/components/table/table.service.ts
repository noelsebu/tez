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
  saveresponse(data, filename) {
    if (!data) {
      console.error('Console.save: No data');
      return;
    }

    if (!filename) { filename = 'console.json'; }

    let blob = new Blob([data], {type: 'application/json'});
    let  e    = document.createEvent('MouseEvents');
    let  a    = document.createElement('a');
    a = document.createElement('a');
    a.download = filename;
    a.href = window.URL.createObjectURL(blob);
    a.dataset.downloadurl = ['application/json', a.download, a.href].join(':');
    e.initEvent('click', true, false); //  window, 0, 0, 0, 0, 0, false, false, false, false, 0, null );
    a.dispatchEvent(e);
  }






  postresponse(data) {
    console.log('inside resojcd');
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type' : 'application/json'
      })
    };
    this.httpClient.post('http://10.60.163.75:8000/api/test ', httpOptions , data );
    }
}

