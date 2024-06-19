import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { NewExercise } from '../../models/newExercise';
import { MainService } from '../../services/main.service';

@Component({
  selector: 'app-new-exercise',
  templateUrl: './new-exercise.component.html',
  styleUrl: './new-exercise.component.scss'
})
export class NewExerciseComponent {
  newExerciseForm!: FormGroup;

  constructor(private formBuilder: FormBuilder, private mainService: MainService) {

  }

  ngOnInit() {
    this.newExerciseForm = this.formBuilder.group({
      name: ['', Validators.required],
      video: ['', Validators.required]
    });
  }

  onVideoPicked(event: any) {
    let file = event.target.files[0];
    console.log(file);
    this.newExerciseForm.patchValue({ video: file});
  }

  submitForm() {
    console.log(this.newExerciseForm.value);
    let newExercise: NewExercise = this.newExerciseForm.value;
    this.mainService.postNewExercise(newExercise).subscribe();
  }
}
