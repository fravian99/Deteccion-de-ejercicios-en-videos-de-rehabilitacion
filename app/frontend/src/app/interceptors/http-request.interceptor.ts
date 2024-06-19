import { HttpErrorResponse, HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, throwError } from 'rxjs';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

@Injectable()
export class HttpRequestInterceptor implements HttpInterceptor  {

  private isRefreshing = false;

  constructor(private router: Router, private authService: AuthService) {
  }

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {

      let token = this.authService.getAccessToken();
      
      /*if (
          !request.headers.has('Content-Type') &&
          !request.url.includes('/login')
      ) {
          request = request.clone({
              headers: request.headers.set('Content-Type', 'application/json')
          });
      }*/

      if (token) {
          request = request.clone({
              headers: request.headers.set('Authorization', `Bearer ${token}`)
          });
         
      }

      return next.handle(request).pipe( 
        catchError((err: any) => {
            if (err instanceof HttpErrorResponse) {
                if (err.status === 401) {      
                    this.router.navigate(['login']);
                    if(token) {
                        console.error('HTTP error:', err);
                        this.authService.removeToken()
                    }
                } else {
                    console.error('HTTP error:', err);
                }
            } else {
                console.error('An error occurred:', err);
            }
            return throwError(() => err); 
        }));
  }

}