import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { AuthGuard } from './guard/auth.guard';
import { NewExerciseComponent } from './new-exercise/new-exercise.component';
import { SignupComponent } from './signup/signup.component';
import { ExercisesComponent } from './exercises/exercises.component';
import { CompareExerciseComponent } from './compare-exercise/compare-exercise.component';
import { DeleteExerciseComponent } from './delete-exercise/delete-exercise.component';

const routes: Routes = [
  {path: '', redirectTo: 'home', pathMatch:'full'},
  {path: 'home', component: HomeComponent},
  {path: 'test', component: HomeComponent},
  {path: 'login', component: LoginComponent},
  {path: 'signup', component: SignupComponent},
  {path: 'new-exercise', component: NewExerciseComponent,  canActivate: [AuthGuard]},
  {path: 'exercises', component: ExercisesComponent,  canActivate: [AuthGuard]},
  {path: 'compare-exercise/:id', component: CompareExerciseComponent,  canActivate: [AuthGuard]},
  {path: 'delete-exercise', component: DeleteExerciseComponent,  canActivate: [AuthGuard]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
