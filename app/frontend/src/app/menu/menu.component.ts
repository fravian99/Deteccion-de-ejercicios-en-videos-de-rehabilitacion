import { Component, Input } from '@angular/core';
import { MainService } from '../services/main.service';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrl: './menu.component.scss'
})
export class MenuComponent {
  
  
  constructor(private mainService: MainService, protected userService: UserService) {
  }

  
}
