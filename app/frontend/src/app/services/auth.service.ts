import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { JwtHelperService } from "@auth0/angular-jwt";


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  //private baseUrl = environment.url;
  //private authUrl = this.baseUrl + 'auth/'

  //private accessToken: string | null=  null;

  private helper: JwtHelperService = new JwtHelperService();

  private editors = ["admin"]

  private tokenStorage = "token"

  constructor(private http: HttpClient) {}

  getAccessToken(): string | null{
    let accessToken = sessionStorage.getItem(this.tokenStorage);
    return this.isExpired() ? null : accessToken;
  }

  setAccessToken(token: string): void {
    sessionStorage.setItem(this.tokenStorage,token);
  }

  removeToken() {
    sessionStorage.removeItem(this.tokenStorage);
    return true;
  }

  getUserName() {
    let accessToken = sessionStorage.getItem(this.tokenStorage);
    if (!accessToken) {
      return undefined
    }
    let decodedToken = this.helper.decodeToken(accessToken!);
    return decodedToken.username
  }

  canEditExercises() {
    let accessToken = sessionStorage.getItem(this.tokenStorage);
    if (!accessToken) {
      return false;
    }
    let decodedToken = this.helper.decodeToken(accessToken!);
    return decodedToken.rol
  }

  isExpired() {
    let accessToken = sessionStorage.getItem(this.tokenStorage);
    const expirationDate = this.helper.getTokenExpirationDate(accessToken!);
    return accessToken ? this.helper.isTokenExpired(accessToken) : true;
  }
}
