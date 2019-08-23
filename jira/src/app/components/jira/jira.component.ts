import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { JiraService } from './jira.service';
@Component({
  selector: 'app-jira',
  templateUrl: './jira.component.html',
  styleUrls: ['./jira.component.css']
})
export class JiraComponent implements OnInit {
  jiraForm: FormGroup;
  constructor(private jira: JiraService) { }

  ngOnInit() {
    this.jiraForm = new FormGroup ({
      username: new FormControl(),
      password: new FormControl()
  });
}

  postDetails(): void {
    const selectedArray = this.jiraForm.value;
    this.jira.postresponsefinals(selectedArray).subscribe(res => {
      console.log('res: ' + res);
    });

  }

}
