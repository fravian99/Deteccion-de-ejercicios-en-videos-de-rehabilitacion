import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { DomSanitizer } from '@angular/platform-browser';

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
}
