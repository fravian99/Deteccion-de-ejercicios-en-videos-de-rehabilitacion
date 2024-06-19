import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { UserService } from '../services/user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrl: './signup.component.scss'
})
export class SignupComponent {
  signupForm!: FormGroup;
  showErrors: boolean = false;

  constructor(private formBuilder: FormBuilder, private userService: UserService, private router: Router) {

  }

  ngOnInit() {
    this.signupForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });
  }

  submitForm() {
    if (this.signupForm.valid) {
      this.userService.newUser(this.signupForm.value).subscribe({
        next: (res: any) => {
          if (res) {
            this.router.navigate(['home'])
          }
        }
      });
    } else {
      this.showErrors = true;
    }
  }
}
