import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

export const AuthGuard: CanActivateFn = (route, state) => {
  console.log(route, route.routeConfig?.path)
  const currentmenu = route.routeConfig?.path
  let authService = inject(AuthService);
  const router = inject(Router)
  const token = authService.getAccessToken()

  if (token) {
    if(currentmenu == 'login' || currentmenu == 'signup'){
      router.navigate([''])
      return false
    } else {
      return true
    }
  } else {
    router.navigate(['/login'])
    return false
  }
};