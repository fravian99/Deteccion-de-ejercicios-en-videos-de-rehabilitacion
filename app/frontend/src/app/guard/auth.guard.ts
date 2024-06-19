import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';

export const AuthGuard: CanActivateFn = (route, state) => {
  console.log(route, route.routeConfig?.path)
  const currentmenu = route.routeConfig?.path
  
  const router = inject(Router)
  const token = sessionStorage.getItem('token')

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