import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { NewExercise } from '../models/newExercise';
import { DomSanitizer } from '@angular/platform-browser';
import { map } from 'rxjs';
import { UserExercise } from '../models/userExercise';

@Injectable({
  providedIn: 'root'
})
export class ExerciseService {

  private basesUrl: string = environment.url;
  private exerciseUrl: string = this.basesUrl + "exercise/";

  headers = new HttpHeaders({
    Authorization: `Bearer ${sessionStorage.getItem('token')}`
  });

  constructor(private http: HttpClient, private sanitizer: DomSanitizer) { }

  postNewExercise(exercise: NewExercise) {
    //let headers = new HttpHeaders().set('Content-Type', 'multipart/form-data'); 
    const formData = new FormData();
    formData.append('name', exercise.name);
    for (let angle of exercise.angles) {
      formData.append('angles', angle);
    }
    for (let coord of exercise.coords) {
      formData.append('coords', coord);
    }
    formData.append('data', exercise.data);
    formData.append('video', exercise.video);
    
    return this.http.post(this.exerciseUrl + 'new-exercise', formData);
  }

  postUserExercise(exercise: UserExercise) {
    //let headers = new HttpHeaders().set('Content-Type', 'multipart/form-data'); 
    const formData = new FormData();
    formData.append('data', exercise.data);
    return this.http.post(this.exerciseUrl + 'send-user-exercise/' + exercise.id, formData, {headers: this.headers});

  }

  getExercises() {
    return this.http.get(this.exerciseUrl + 'get-exercises', {headers: this.headers});
  }

  getExercise(exercise: number) {
    return this.http.get(this.exerciseUrl + 'get-exercise/' + exercise, {headers: this.headers});
  }

  getVideo(exercise:number) {
    return this.http.get(this.exerciseUrl + 'get-video/' + exercise, {headers: this.headers, responseType: 'arraybuffer'}).pipe(
      map((video) => {
        const blob = new Blob([video], { type: 'video/mp4' });
        return this.sanitizer.bypassSecurityTrustResourceUrl(URL.createObjectURL(blob));  
      })
    );
  }

  getDefaultParts() {
    return this.http.get(this.exerciseUrl + 'default-parts', {headers: this.headers});
  }

  deleteExercise(id: number) {
    return this.http.delete(this.exerciseUrl + 'delete-exercise/' + id);
  }
}
