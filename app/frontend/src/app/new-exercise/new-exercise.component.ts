import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { NewExercise } from '../models/newExercise';
import { MainService } from '../services/main.service';
import { ExerciseService } from '../services/exercise.service';
import { Observable, tap } from 'rxjs';
import Swal from 'sweetalert2';
import { Router } from '@angular/router';
import {TranslateService} from '@ngx-translate/core';

@Component({
  selector: 'app-new-exercise',
  templateUrl: './new-exercise.component.html',
  styleUrl: './new-exercise.component.scss'
})
export class NewExerciseComponent {
  newExerciseForm!: FormGroup;
  showErrors:boolean = false;
  angles: any[] = [];
  coords: any[] = []

  constructor(private formBuilder: FormBuilder, private translate: TranslateService, private exerciseService: ExerciseService, private router: Router) {
    
  }

  ngOnInit() {
    this.showErrors = false;
    this.newExerciseForm = this.formBuilder.group({
      name: ['', Validators.required],
      data: ['', Validators.required],
      video: ['', Validators.required],
      angles: ['', Validators.required],
      coords: ['', Validators.required]
    });

    this.setAngles().subscribe({
      next: () => {
      }
    })
    
  }


  setAngles(): Observable<any> {
    return this.exerciseService.getDefaultParts().pipe(
      tap((res:any) => {
        this.angles = res.angles;
        this.coords = res.coords;
      }
    ))
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
      this.exerciseService.postNewExercise(newExercise).subscribe({
        next: (res: any) => {
          Swal.fire({
            title: this.translate.instant('new-exercise.saved.title'),
            text: this.translate.instant('new-exercise.saved.text'),
            icon: "success"
          }).then(
            () => {
              this.router.navigate(['exercises']);
            }
          );
        }
      });
    } else {
      this.showErrors = true;
    }
  }
}
