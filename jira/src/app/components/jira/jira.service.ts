import { Injectable } from '@angular/core';
import { MatTableDataSource } from '@angular/material';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'environments/environment';

@Injectable({
    providedIn: 'root'
})

export class JiraService {
    baseUrl = environment.baseUrl;
    constructor(private httpClient: HttpClient) { }
    postresponsefinals(data) {
        const url = this.baseUrl + '/users';
        return this.httpClient.post<any[]>(url, data);
    }
}
