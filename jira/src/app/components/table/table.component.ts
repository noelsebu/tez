import { Component, OnInit, ViewChild } from '@angular/core';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MatPaginatorModule, MatPaginator, MatSort, MatTableDataSource } from '@angular/material';
import {SelectionModel} from '@angular/cdk/collections';
import { TableService } from './table.service';
@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
@Injectable({providedIn: 'root'})
export class TableComponent implements OnInit {
  public array: any;
  public displayedColumns: string[] = ['select', 'testid', 'team_name', 'testscript'];
  public data: MatTableDataSource<any[]>;
  selection = new SelectionModel<any[]>(true, []);
  configUrl = 'assets/config.json';
  filename = 'response.json';
  public pageSize = 10;
  public currentPage = 0;
  public totalSize = 0;
  @ViewChild(MatPaginator, {static: true}) paginator: MatPaginator;
  @ViewChild(MatSort, {static: true}) sort: MatSort;
  constructor(private test: TableService) {  }

  ngOnInit(): void {
        this.test.getresponse().subscribe((
        response: MatTableDataSource<any[]>) => {
          console.log(response);
          // this.data = new MatTableDataSource(response);
          this.createTable(response);
          this.data.sort = this.sort;
           });
            }
  createTable(data: any) {
      this.data = new MatTableDataSource(data);
      const sample = JSON.stringify(data);
      this.data.paginator = this.paginator;
    //  this.data.sort = this.sort;
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
    console.log(' hi ');
    console.log(filterValue);
    const filter = filterValue.trim().toLowerCase(); // MatTableDataSource defaults to lowercase matches
    this.data.filter = filter;

    }
  isAllSelected() {
      const numSelected = this.selection.selected.length;
      const numRows = this.data.data.length;
      return numSelected === numRows;
    }
  /** Selects all rows if they are not all selected; otherwise clear selection. */
    masterToggle() {
      this.isAllSelected() ?
          this.selection.clear() :
          this.data.data.forEach(row => this.selection.select(row));
    }    /** The label for the checkbox on the passed row */
    checkboxLabel(row?: any): string {
      if (!row) {
        return `${this.isAllSelected() ? 'select' : 'deselect'} all`;
      }
      return `${this.selection.isSelected(row) ? 'deselect' : 'select'} row ${row.position + 1}`;
    }
    save() {
      const selectedArray = this.selection.selected;
      console.log(selectedArray);
      this.test.postresponse(selectedArray);
    }
  }

