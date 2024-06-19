import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../environments/environment';
import { map } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MainService {

  private basesUrl: string = environment.url;
  
  constructor( private http: HttpClient) { }

  testApi() {
    return this.http.get(this.basesUrl + 'test');
  }

video(exercise:string) {
    return this.http.get(this.basesUrl + 'video/' + exercise, { responseType: 'arraybuffer' }).pipe(
      map((video) => {
        const blob = new Blob([video], { type: 'video/mp4' });
        return URL.createObjectURL(blob);  
      })
    );
  }
}
