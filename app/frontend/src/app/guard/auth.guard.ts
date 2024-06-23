import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { UserService } from '../services/user.service';

export const AuthGuard: CanActivateFn = (route, state) => {
  console.log(route, route.routeConfig?.path)
  const currentmenu = route.routeConfig?.path;
  let authService = inject(AuthService);
  let userService = inject(UserService);
  const router = inject(Router);
  const token = authService.getAccessToken();


  if (authService.isExpired()) {
    authService.removeToken();
  }
  userService.getUsername()

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