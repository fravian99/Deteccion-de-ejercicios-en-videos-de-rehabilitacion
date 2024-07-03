import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { User } from '../models/user';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private basesUrl: string = environment.url + "user/";

  username: string | undefined = undefined;

  private editors = ["admin"]

  headers = new HttpHeaders({
    Authorization: `Bearer ${sessionStorage.getItem('token')}`
  });

  constructor( private http: HttpClient, private auth: AuthService) { }

  newUser(user: User) {
    return this.http.post(this.basesUrl + 'new-user', user);
  }

  login(user: any) {
    return this.http.post(this.basesUrl + "login", user, {headers: this.headers});
  }

  getUsername() {
    this.username = this.auth.getUserName()
    return this.username
  }

  canEdit() {
    let role = this.auth.getRole()
    if (role && this.editors.includes(role)) {
      return true;
    }
    return false;
  }

  isLogged() {
    if (this.auth.getAccessToken() != null && this.auth.getAccessToken() != undefined) {
      return true;
    } else {
      return false;
    }
  }
}
