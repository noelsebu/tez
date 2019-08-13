import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { GitService } from './git-url.service';

@Component({
  selector: 'app-git-url',
  templateUrl: './git-url.component.html',
  styleUrls: ['./git-url.component.css']
})
export class GitUrlComponent implements OnInit {
  gitForm: FormGroup;
  constructor(private test: GitService) { }

  ngOnInit() {
    this.gitForm = new FormGroup ({
      username: new FormControl(),
      password: new FormControl()
    });
  }
  postDetails(): void {
    const selectedArray = this.gitForm.value;
    this.test.postresponsefinals(selectedArray).subscribe(res => {
      console.log('res: ' + res);
    });

  }
}
