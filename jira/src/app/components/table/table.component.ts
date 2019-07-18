import { Component, OnInit, ViewChild } from '@angular/core';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MatPaginatorModule, MatPaginator, MatSort } from '@angular/material';
import { MatTableDataSource } from '@angular/material/table';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
@Injectable({providedIn: 'root'})
export class TableComponent implements OnInit {
  public array: any;
  public displayedColumns: string[] = ['select', 'testid', 'team_name', 'testscript'];
  public data: MatTableDataSource<any>;
  configUrl = 'assets/config.json';
  public pageSize = 10;
  public currentPage = 0;
  public totalSize = 0;
  @ViewChild(MatPaginator, {static: true}) paginator: MatPaginator;
  @ViewChild(MatSort, {static: true}) sort: MatSort;
  constructor(private httpClient: HttpClient) { }



  ngOnInit(): void {
    this.httpClient.get('./assets/data.json', { responseType: 'json' }).subscribe(
        response => {
          this.createTable(response);
             });
   // this.data.paginator = this.paginator;
    // this.data.sort = this.sort;
          }
            createTable(data: any) {
              this.data = new MatTableDataSource(data);
              const sample = JSON.stringify(data);
              this.data.paginator = this.paginator;
              this.data.sort = this.sort;
              this.array = data;
              this.totalSize = this.array.length;
              this.iterator();
            }
  public handlePage(e: any) {
      this.currentPage = e.pageIndex;
      this.pageSize = e.pageSize;
      this.iterator();
      }
  private iterator() {
      const end = (this.currentPage + 1) * this.pageSize;
      const start = this.currentPage * this.pageSize;
      const part = this.array.slice(start, end);
      this.data = part;
      }
  applyFilter = (filterValue: string) => {
    console.log(filterValue);
    const filter = filterValue.trim().toLowerCase(); // MatTableDataSource defaults to lowercase matches
    this.data.filter = filter;

    }

}
