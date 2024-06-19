import { Component } from '@angular/core';
import { MainService } from '../../services/main.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {
  video = undefined;

  constructor(private mainService: MainService) {
    this.mainService.getVideo("pelota2").subscribe(
      (res: any) => {
        if (res) {
          this.video = res;
          console.log(res.message);
        } else {
          console.log("error")
        }
      }
    );
  }
}
