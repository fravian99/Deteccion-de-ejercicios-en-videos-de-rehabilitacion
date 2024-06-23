import { Component } from '@angular/core';
import { ExerciseName } from '../models/exerciseName';
import { ExerciseService } from '../services/exercise.service';

@Component({
  selector: 'app-exercises',
  templateUrl: './exercises.component.html',
  styleUrl: './exercises.component.scss'
})
export class ExercisesComponent {
  
  exercises: ExerciseName[] = [];

  constructor(private exerciseService: ExerciseService) {
    this.exerciseService.getExercises().subscribe({
      next: (res: any) => {
        this.exercises = res.exercises;
      }      
    }); 
  }
}
