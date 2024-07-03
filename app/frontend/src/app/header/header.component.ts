import { Component, EventEmitter, Input, Output } from '@angular/core';
import { AuthService } from '../services/auth.service';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent {
  @Output() toggle: EventEmitter<void> = new EventEmitter<void>;
  user: string | undefined = undefined;
  
  constructor(public userService: UserService, private authService: AuthService) {
    this.user = this.userService.getUsername();
  }

  logOut() {
    this.authService.removeToken();
    window.location.reload();
  }

  emitToggle() {
    this.toggle.emit()
  }

}
