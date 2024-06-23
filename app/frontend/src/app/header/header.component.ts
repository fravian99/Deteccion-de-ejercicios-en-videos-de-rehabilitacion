import { Component } from '@angular/core';
import { AuthService } from '../services/auth.service';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent {
  user: string | undefined = undefined;
  
  constructor(public userService: UserService, private authService: AuthService) {
    this.user = this.userService.getUsername();
  }

  logOut() {
    this.authService.removeToken();
    window.location.reload();
  }
}
