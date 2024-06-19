import { getHtmlTagDefinition } from '@angular/compiler';
import { Component, ElementRef, ViewChild } from '@angular/core';
import {TranslateService} from '@ngx-translate/core';
import { MainService } from '../services/main.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = "app.title";
  video = undefined;

  constructor(private mainService: MainService) {
    this.mainService.testApi().subscribe(
      (res: any) => {
        if (res) {
          console.log(res.message);
        } else {
          console.log("error")
        }
      }
    );
  }
}
