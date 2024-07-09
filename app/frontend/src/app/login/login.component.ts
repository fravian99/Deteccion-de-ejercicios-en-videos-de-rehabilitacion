import { Component } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { UserService } from '../services/user.service';
import { HttpParams } from '@angular/common/http';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent {
  loginForm!: FormGroup;
  showErrors: boolean = false;

  constructor(private formBuilder: FormBuilder, private userService: UserService, private router: Router, private authService: AuthService) {

  }

  ngOnInit() {
    this.showErrors = false;
    this.loginForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });
  }
  loginRedirect() {
    this.router.navigate(['/']);
  }

  submitForm() {
    if (this.loginForm!.valid) {
      const formData = new HttpParams()
      .set('grant_type', '')
      .set('username', this.loginForm.value.username)
      .set('password', this.loginForm.value.password);


      this.userService.login(formData).subscribe({
        next: (res: any) => {
          this.authService.setAccessToken(res.access_token);
          this.loginRedirect();
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
