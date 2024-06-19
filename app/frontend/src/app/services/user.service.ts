import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { User } from '../models/user';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private basesUrl: string = environment.url + "user/";

  headers = new HttpHeaders({
    Authorization: `Bearer ${sessionStorage.getItem('token')}`
  });

  constructor( private http: HttpClient) { }

  newUser(user: User) {
    return this.http.post(this.basesUrl + 'new-user', user);
  }

  login(user: any) {
    return this.http.post(this.basesUrl + "login", user, {headers: this.headers});
  }
}
