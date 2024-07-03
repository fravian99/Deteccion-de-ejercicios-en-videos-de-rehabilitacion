import { Component, OnInit } from '@angular/core';
import { ExerciseService } from '../services/exercise.service';
import { ActivatedRoute } from '@angular/router';
import { ExerciseName } from '../models/exerciseName';
import { UserExercise } from '../models/userExercise';

@Component({
  selector: 'app-compare-exercise',
  templateUrl: './compare-exercise.component.html',
  styleUrl: './compare-exercise.component.scss'
})
export class CompareExerciseComponent implements OnInit{
  video: any | undefined = undefined;
  id!: number;
  exercise!: ExerciseName;
  file: any
  score: number | undefined = undefined;

  constructor(
    private route: ActivatedRoute,
    private exerciseService: ExerciseService
  ) {
    this.id = this.route.snapshot.params['id'];
    
  }

  ngOnInit(): void {
    this.exerciseService.getVideo(this.id).subscribe({
      next: (video: any) => {
        this.video = video;
      } 
    });
    this.exerciseService.getExercise(this.id).subscribe({
      next: (res: any) => {
        this.exercise = res;
      }
    })
  }

  setFile(event: any) {
    this.file = event.target.files[0];
  }

  sendExerciseWithFile() {
    this.score = undefined;
    if (this.file != undefined && this.file != null){
      let userExercise: UserExercise = new UserExercise();
      userExercise.id = this.id;
      userExercise.data = this.file;
      this.exerciseService.postUserExercise(userExercise).subscribe({
        next: (res: any) => {
          this.score = res;
        }
      });
    }
  }
}
