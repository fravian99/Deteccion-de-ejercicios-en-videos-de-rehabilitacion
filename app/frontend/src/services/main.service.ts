import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../environments/environment';
import { DomSanitizer } from '@angular/platform-browser';
import { map } from 'rxjs';
import { NewExercise } from '../models/newExercise';

@Injectable({
  providedIn: 'root'
})
export class MainService {
  
  private basesUrl: string = environment.url;

  headers = new HttpHeaders({
    Authorization: `Bearer ${sessionStorage.getItem('token')}`
  });

  jsonHeaders = this.headers.set('Content-Type', 'application/json; charset=utf-8');
  
  constructor( private http: HttpClient, private sanitizer: DomSanitizer) { }

  testApi() {
    return this.http.get(this.basesUrl + 'test');
  }

  getVideo(exercise:string) {
    return this.http.get(this.basesUrl + 'video/' + exercise, { responseType: 'arraybuffer' }).pipe(
      map((video) => {
        const blob = new Blob([video], { type: 'video/mp4' });
        return this.sanitizer.bypassSecurityTrustResourceUrl(URL.createObjectURL(blob));  
      })
    );
  }

  postNewExercise(exercise: NewExercise) {
    
    console.log(exercise)
    //let headers = new HttpHeaders().set('Content-Type', 'multipart/form-data'); 
    const formData = new FormData();
    formData.append('name', exercise.name);
    formData.append('video', exercise.video);
    return this.http.post(this.basesUrl + 'exercise/new-exercise', formData, {headers: this.headers});

  }
}
