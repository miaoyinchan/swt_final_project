import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TravelOptionsComponent } from './travel-options.component';

describe('TravelOptionsComponent', () => {
  let component: TravelOptionsComponent;
  let fixture: ComponentFixture<TravelOptionsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TravelOptionsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TravelOptionsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
