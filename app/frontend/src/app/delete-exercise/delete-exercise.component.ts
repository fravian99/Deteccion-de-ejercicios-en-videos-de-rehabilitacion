import { Component } from '@angular/core';
import { ExerciseService } from '../services/exercise.service';
import { ExerciseName } from '../models/exerciseName';
import { tap } from 'rxjs';
import {TranslateService} from '@ngx-translate/core';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-delete-exercise',
  templateUrl: './delete-exercise.component.html',
  styleUrl: './delete-exercise.component.scss'
})
export class DeleteExerciseComponent {
  exercises: ExerciseName[] = [];
  constructor(private exerciseService: ExerciseService, private translate: TranslateService) {
    this.reloadExercises().subscribe();
  }

  reloadExercises() {
    return this.exerciseService.getExercises().pipe(
      tap((res: any) => {
        this.exercises = res.exercises;
      })      
    ); 
  }

  deleteExercise(exercise: ExerciseName) {
    Swal.fire({
      title: this.translate.instant('delete-exercise.deleting.title'),
      text:  this.translate.instant('delete-exercise.deleting.text'),
      icon: "warning",
      showCancelButton: true,
      confirmButtonText: this.translate.instant('delete-exercise.deleting.confirm'),
      cancelButtonText: this.translate.instant('delete-exercise.deleting.cancel')
    }).then((result) => {
      if (result.isConfirmed) {
        this.exerciseService.deleteExercise(exercise.id).subscribe({
          next: (_: any) => {
            Swal.fire({
              title: this.translate.instant('delete-exercise.deleted.title'),
              text:  this.translate.instant('delete-exercise.deleted.text'),
              icon: "success"
            });
            this.reloadExercises().subscribe();
          }
        });
      }
    });
  }
}
