import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TravelService {

  constructor(private http: HttpClient) { }

  getResponse$(request:any):Observable<any> {
    return this.http.post<any>(`api/results`, request);
  }

  getDistances$(request:any):Observable<any> {
    return this.http.post<any>(`api/distances`, request);
  }
  getDescriptions$(request:any):Observable<any> {
    return this.http.post<any>(`api/descriptions`, request);
  }
  getNearestHotel$(request:any):Observable<any> {
    return this.http.post<any>(`api/nearest`, request);
  }
}
