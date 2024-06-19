import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../environments/environment';
import { User } from '../models/user';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private basesUrl: string = environment.url;

  constructor( private http: HttpClient) { }

  newUser(user: User) {
    return this.http.post(this.basesUrl + 'user/new-user', user)
  }
}
