import { Component } from '@angular/core';
import { MainService } from '../services/main.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {
  video = undefined;

  constructor(private mainService: MainService) {
  }
}
