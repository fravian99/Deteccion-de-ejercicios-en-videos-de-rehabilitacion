import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { UserService } from '../services/user.service';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';

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
            this.router.navigate(['/'])
          }
        }, 
        error: (err) => {
          Swal.fire({
            icon: "error",
            title: err.statusText,
            text: err.error.detail
          });
        }
      });
    } else {
      this.showErrors = true;
    }
  }
}
