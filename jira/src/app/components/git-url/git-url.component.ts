import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-git-url',
  templateUrl: './git-url.component.html',
  styleUrls: ['./git-url.component.css']
})
export class GitUrlComponent implements OnInit {
  gitForm: FormGroup;
  constructor() { }

  ngOnInit() {
    this.gitForm = new FormGroup ({
      username: new FormControl(),
      password: new FormControl()
    });
  }
  onSubmit(): void {
    console.log(this.gitForm.value);
  }
}
