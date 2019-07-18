import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GitUrlComponent } from './git-url.component';

describe('GitUrlComponent', () => {
  let component: GitUrlComponent;
  let fixture: ComponentFixture<GitUrlComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GitUrlComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GitUrlComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
