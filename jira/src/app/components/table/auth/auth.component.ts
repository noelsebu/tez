import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { TableService } from '../table.service';
@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css']
})
export class AuthComponent implements OnInit {
  authForm: FormGroup;
  constructor(private test: TableService) { }

  ngOnInit() {
      this.authForm = new FormGroup ({
      mie: new FormControl(),
      token: new FormControl(),
      username: new FormControl(),
      password: new FormControl()

    });
  }
  postDetails(): void {
    const selectedArray = this.authForm.value;
    this.test.postcredentials(selectedArray).subscribe(res => {
      console.log('res: ' + res);
    });

}
}
