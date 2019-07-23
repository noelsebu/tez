import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {  HttpClientModule } from '@angular/common/http';

import { MatButtonModule, MatFormFieldModule, MatInputModule, MatToolbarModule, MatRadioModule, MatCardModule } from '@angular/material';
import { MatTableModule, MatCheckboxModule, MatPaginatorModule, MatSortModule } from '@angular/material';
import { FileUploadModule } from 'ng2-file-upload';



import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { GitUrlComponent } from './components/git-url/git-url.component';
import { CheckboxComponent } from './components/checkbox/checkbox.component';
import { HeaderComponent } from './components/header/header.component';
import { SumbitComponent } from './components/sumbit/sumbit.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule } from '@angular/forms';
import { TableComponent } from './components/table/table.component';
import { HomeComponent } from './components/home/home.component';
import { UploadComponent } from './components/upload/upload.component';
import { TableService } from './components/table/table.service';
import { ReviewComponent } from './components/review/review.component';

@NgModule({
  declarations: [
    AppComponent,
    GitUrlComponent,
    CheckboxComponent,
    HeaderComponent,
    SumbitComponent,
    TableComponent,
    HomeComponent,
    UploadComponent,
    ReviewComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatInputModule,
    MatToolbarModule, MatTableModule, MatCheckboxModule, MatPaginatorModule, MatSortModule,
    MatFormFieldModule, MatButtonModule, MatInputModule, MatRadioModule, MatCardModule,
    FormsModule, HttpClientModule , FileUploadModule


  ],
  providers: [TableService],
  bootstrap: [AppComponent]
})
export class AppModule { }
