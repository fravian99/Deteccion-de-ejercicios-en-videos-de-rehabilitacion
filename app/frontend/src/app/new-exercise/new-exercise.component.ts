import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { NewExercise } from '../models/newExercise';
import { MainService } from '../services/main.service';
import { ExerciseService } from '../services/exercise.service';

@Component({
  selector: 'app-new-exercise',
  templateUrl: './new-exercise.component.html',
  styleUrl: './new-exercise.component.scss'
})
export class NewExerciseComponent {
  newExerciseForm!: FormGroup;
  showErrors:boolean = false;

  constructor(private formBuilder: FormBuilder, private exerciseService: ExerciseService) {

  }

  ngOnInit() {
    this.showErrors = false;
    this.newExerciseForm = this.formBuilder.group({
      name: ['', Validators.required],
      data: ['', Validators.required],
      video: ['', Validators.required]
    });
  }

  onFilePicked(event: any) {
    let file = event.target.files[0];
    this.newExerciseForm.patchValue({ data: file});
  }

  onVideoPicked(event: any) {
    let file = event.target.files[0];
    this.newExerciseForm.patchValue({ video: file});
  }

  submitForm() {
    if (this.newExerciseForm.valid) {
      let newExercise: NewExercise = this.newExerciseForm.value;
      this.exerciseService.postNewExercise(newExercise).subscribe();
    } else {
      this.showErrors = true;
    }
  }
}
