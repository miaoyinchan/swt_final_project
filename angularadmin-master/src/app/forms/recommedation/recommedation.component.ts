import { AfterViewInit, Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { TravelService } from 'app/travel.service';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'app-recommedation',
  templateUrl: './recommedation.component.html',
  styleUrls: ['./recommedation.component.css']
})

export class RecommedationComponent implements OnInit,AfterViewInit {
  @Input() value = Object;
  @Input() city = '';
  text_arr = []
  results = []
  isDataAvailable = false
  localData ={}
  hotel = {}
  @Output() distanceResults = new EventEmitter<any>();

  constructor(private travelService:TravelService, private sanitized: DomSanitizer) { }
  ngAfterViewInit(): void {
  }

  ngOnInit(): void {

    if(this.value['interests']){
      this.getDescription(this.value['interests']);
      this.getHotel();
    }
    for (let key in this.value){
      if(key !== 'interests'){
       this.text_arr.push()
      }
    }
  }

  private async getHotel(){
    var hotels = []
    Object.keys(this.value).forEach(e => {if(e!="interests"){
      hotels.push(e)
    };});
    for(let i = 0; i < this.value['interests'].length; i++){
      let request = { interest: this.value['interests'][i],
        hotels:hotels
      }
      var results = await this.travelService.getNearestHotel$(request).toPromise();

      this.hotel[this.value['interests'][i]]= results[0].label.value;

    }
  }
   private async getDescription(interests:any){
    for(let i = 0; i < this.value['interests'].length; i++){
      let request = { name: interests[i],

      }
      var description = await this.travelService.getDescriptions$(request).toPromise();
      if(description.length >0){
        this.localData[interests[i]] = description[0].desc.value;
      } else{
        this.localData[interests[i]] = "";
      }


    }
  }


  onClick(hotel:any,interests:any):void{
    let request = { name: hotel,
      interests:interests
    }
    this.getInterests(request);
  }

  parseResults(hotel:any,interests:any){
    let res = []
    let op = {}
    let distance = 'distance'
    let new_distance = ''
    for (let i = 0; i < interests.length; i++) {
      new_distance = distance + (i+1)
      op["distance"] = this.results[0][new_distance]
      op["interest"] = interests[i]
      op["accommodation"] = hotel
      res.push(op)
    }
    return res

  }


  private async getInterests(request:any){
    this.results = await this.travelService.getDistances$(request).toPromise();
    let res = []
    let op = {}
    let distance = 'distance'
    let new_distance = ''
    for (let i = 0; i < request.interests.length; i++) {
      new_distance = distance + (i+1)
      op["distance"] = this.results[0][new_distance].value
      op["interest"] = request.interests[i]
      op["accommodation"] = request.name
      res.push(op)
      op = {}
    }
    this.results = res
    this.distanceResults.emit(res);
  }

}
