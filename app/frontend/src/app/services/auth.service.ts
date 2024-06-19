import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private baseUrl = environment.url;
  private authUrl = this.baseUrl + 'auth/'

  private accessToken: string | null= "";

  constructor(private http: HttpClient) {}

  getAccessToken(): string | null{
    this.accessToken = sessionStorage.getItem('token');
    return this.accessToken;
  }

  setAccessToken(token: string): void {
    sessionStorage.setItem('token',token);
  }

  removeToken() {
    sessionStorage.removeItem('token');
    this.accessToken = "";
  }
}
