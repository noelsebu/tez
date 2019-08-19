import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {  HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';

import { MatButtonModule, MatFormFieldModule, MatInputModule, MatToolbarModule, MatRadioModule, MatCardModule } from '@angular/material';
import { MatTableModule, MatCheckboxModule, MatPaginatorModule, MatSortModule , MatProgressSpinnerModule} from '@angular/material';




import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { GitUrlComponent } from './components/git-url/git-url.component';
import { CheckboxComponent } from './components/checkbox/checkbox.component';
import { HeaderComponent } from './components/header/header.component';
import { SumbitComponent } from './components/sumbit/sumbit.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { TableComponent } from './components/table/table.component';
import { HomeComponent } from './components/home/home.component';
import { UploadComponent } from './components/upload/upload.component';
import { TableService } from './components/table/table.service';
import { GitService } from './components/git-url/git-url.service';
import { ReviewComponent } from './components/table/review/review.component';
import { DropdownComponent } from './components/dropdown/dropdown.component';
import { ReportComponent } from './components/report/report.component';

// loader components

import { LoaderComponent } from './components/shared/loader/loader.component';
import { LoaderService } from './components/shared/loader/loader.service';
import { LoaderInterceptor } from './components/shared/loader/loader.interceptor';

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
    ReviewComponent,
    DropdownComponent,
    ReportComponent,
    LoaderComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatInputModule,
    MatToolbarModule, MatTableModule, MatCheckboxModule, MatPaginatorModule, MatSortModule,
    MatFormFieldModule, MatButtonModule, MatInputModule, MatRadioModule, MatCardModule,
    FormsModule, HttpClientModule , ReactiveFormsModule , MatProgressSpinnerModule


  ],
  providers: [TableService, GitService, LoaderService , { provide: HTTP_INTERCEPTORS, useClass: LoaderInterceptor, multi: true }],
  bootstrap: [AppComponent]
})
export class AppModule { }
