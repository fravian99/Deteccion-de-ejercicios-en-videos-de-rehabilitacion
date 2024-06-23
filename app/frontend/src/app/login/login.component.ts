import { Component } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { UserService } from '../services/user.service';
import { HttpParams } from '@angular/common/http';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

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
    this.router.navigate(['home']);
  }

  submitForm() {
    if (this.loginForm!.valid) {
      const formData = new HttpParams()
      .set('grant_type', '')
      .set('username', this.loginForm.value.username)
      .set('password', this.loginForm.value.password)


      this.userService.login(formData).subscribe(
        (res: any) => {
          console.log(res)
          this.authService.setAccessToken(res.access_token);
          this.loginRedirect()
        }
      );
    } else {
      this.showErrors = true;
    }
  }
}
