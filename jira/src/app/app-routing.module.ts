import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { TableComponent } from './components/table/table.component';
import { HomeComponent } from './components/home/home.component';
import { ReviewComponent } from './components/table/review/review.component';



const routes: Routes = [
   { path: 'table', component: TableComponent },
   { path: '', component: HomeComponent },
   { path: 'table/review', component: ReviewComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
