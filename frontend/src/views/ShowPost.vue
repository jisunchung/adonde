<template>
       <v-app
        style="background-color: #08844E">
        <v-row style="padding :50px">
            <v-col>
                <v-card>
                     <v-card-text>
                         <v-timeline :dense="$vuetify.breakpoint.smAndDown">
    <v-timeline-item
      color="purple lighten-2"
      fill-dot
      right
    >
      <v-card>
        <v-card-title class="purple lighten-2">
          <h2 class="text-h5 white--text font-weight-Bold">
            디스크도넛커피스탠드
          </h2>
        </v-card-title>
        <v-container>
          <v-row>
              <v-col>
                  <v-img 
                    style="margin: auto"
                    alt="map"
                    contain
                    :src="require(`@/assets/1-4.jpg`)"
                    width="200"
                    />
                    <v-icon>mdi-map-marker</v-icon>  부산 수영구 민락로33번길 17
              </v-col>

          </v-row>
        </v-container>
      </v-card>
    </v-timeline-item>

    <v-timeline-item
      color="amber lighten-1"
      fill-dot
      left
      small
    >
      <v-card>
        <v-card-title class="amber lighten-1 justify-end">
          <h2 class="text-h5 white--text font-weight-Bold">
            상생라멘 심야식당점
          </h2>
        </v-card-title>
        <v-container>
          <v-row>
              <v-col>
                  <v-img 
                    style="margin: auto"
                    alt="map"
                    contain
                    :src="require(`@/assets/2.jpg`)"
                    width="200"
                    /> 
                     <v-icon>mdi-map-marker</v-icon>부산 해운대구 해운대로383번길 23
              </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-timeline-item>

    <v-timeline-item
      color="cyan lighten-1"
      fill-dot
      right
    >
      <v-card>
        <v-card-title class="cyan lighten-1">
          <h3 class="text-h5 white--text font-weight-Bold">
            비아인키노 WEK BUSAN
          </h3>
        </v-card-title>
        <v-container>
          <v-row>
              <v-col>
                  <v-img 
                    style="margin: auto"
                    alt="map"
                    contain
                    :src="require(`@/assets/3-1.jpg`)"
                    width="200"
                    />
                     <v-icon>mdi-map-marker</v-icon>
                    부산 해운대구 달맞이길65번길 167
              </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-timeline-item>

    <v-timeline-item
      color="red lighten-1"
      fill-dot
      left
      small
    >
      <v-card>
        <v-card-title class="red lighten-1 justify-end">
          <h3 class="text-h5 white--text font-weight-Bold">
            해운대블루라인파크
          </h3>
        </v-card-title>
        <v-container>
          <v-row>
              <v-col>
                  <v-img 
                    style="margin: auto"
                    alt="map"
                    contain
                    :src="require(`@/assets/4-5.jpg`)"
                    width="200"
                    />
                    <v-icon>mdi-map-marker</v-icon>
                    부산 해운대구 청사포로 116 청사포정거장
              </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-timeline-item>

  </v-timeline>
                     </v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <!-- <GmapMap
    :center="{lat:10, lng:10}"
  :zoom="7"
  map-type-id="terrain"
  style="width: 500px; height: 300px"
/> -->
  <!-- <GmapMarker
    :key="index"
    v-for="(m, index) in markers"
    :position="m.position"
    :clickable="true"
    :draggable="true"
    @click="center=m.position"
  /> -->
<!-- <div>
                <h1>Your coordinates:</h1>
                <p>{{ myCoordinates.lat }} Latitude, {{ myCoordinates.lng }} Longitude</p>
            </div>
            <div>
                <h1>Map coordinates:</h1>
                <p>{{ mapCoordinates.lat }} Latitude, {{ mapCoordinates.lng }} Longitude</p>
            </div> -->
    
        <GmapMap
            :center="{lat:35.1597, lng: 129.1643}"
            :zoom="zoom"
            style="width:700px; height:700px; "
            ref="mapRef"
            @dragend="handleDrag"
        ><GmapMarker
    :key="index"
    v-for="(m, index) in markers"
    :position="m.position"
    :clickable="true"
    :draggable="true"
    @click="center=m.position"
  />
  <GmapPolyline v-if="curvedPath" :path="curvedPath" /></GmapMap>
            </v-col>
<!-- 
              <GmapMap style="width: 600px; height: 400px;" :zoom="1" :center="{lat: 0, lng: 0}"
        ref="map" @click="clicked">
      <GmapMarker v-if="start" :position="start.latLng" label="S" />
      <GmapMarker v-if="end" :position="end.latLng" label="E" />
      <GmapPolyline v-if="curvedPath2" :path="curvedPath2" />
    </GmapMap> -->
        </v-row>

       </v-app>
</template>

<script>
//import {range} from 'lodash'
export default {
     data() {
            return {
                map: null,
                myCoordinates: {
                    lat: 0,
                    lng: 0
                },
                zoom: 7,
                markers:[
                {position: {lat: 35.15757684070402, lng: 129.12095533979314}}
                ,{position: {lat: 35.17046676539149, lng: 129.13899862629918}},
                {position: {lat: 35.15692152701457, lng: 129.1791026667814}},
                {position: {lat: 35.160107059509265,lng: 129.17081241393657}}
                    ],
                     start: null,
      end: null,
                
            }
        },
        created() {
            // does the user have a saved center? use it instead of the default
            if(localStorage.center) {
                this.myCoordinates = JSON.parse(localStorage.center);
            } else {
                // get user's coordinates from browser request
                this.$getLocation({})
                    .then(coordinates => {
                        this.myCoordinates = coordinates;
                    })
                    .catch(error => alert(error));
            }
            // does the user have a saved zoom? use it instead of the default
            if(localStorage.zoom) {
                this.zoom = parseInt(localStorage.zoom);
            }
        },
    mounted(){
         //window.kakao && window.kakao.maps ? this.initMap() : this.addScript();
        this.$refs.mapRef.$mapPromise.then(map => this.map = map);
    },
    methods:{
       handleDrag() {
                // get center and zoom level, store in localstorage
                let center = {
                    lat: this.map.getCenter().lat(),
                    lng: this.map.getCenter().lng()
                };
                let zoom = this.map.getZoom();
                localStorage.center = JSON.stringify(center);
                localStorage.zoom = zoom;
            },
        // async initMap() { 
        //     var container = document.getElementById('map'); 
        //     var options = { center: new kakao.maps.LatLng(this.latitude, this.longitude), level: 10 };
        //     var map = new kakao.maps.Map(container, options); 
        //     //마커추가하려면 객체를 아래와 같이 하나 만든다. 
        //     var marker = new kakao.maps.Marker({ position: map.getCenter() }); 
        //     await marker.setMap(map); 
        // },  
        // addScript() { 
        //     const script = document.createElement('script'); 
        //     /* global kakao */ 
        //     script.onload = () => kakao.maps.load(this.initMap); 
        //     // script.src = 'http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=0b3e12f49e69284bc5e44c27065a9f7b'; 
        //     document.head.appendChild(script); 
        // },
        clicked (e) {
      if (!this.start && !this.end) {
        this.start = {
          latLng: e.latLng
        }
      } else if (this.start && !this.end) {
        this.end = {
          latLng: e.latLng
        }
      } else {
        this.start = {
          latLng: e.latLng
        }
        this.end = null
      }
    }
    },
    computed: {
            mapCoordinates() {
                if(!this.map) {
                    return {
                        lat: 0,
                        lng: 0
                    };
                }
                return {
                    lat: this.map.getCenter().lat().toFixed(4),
                    lng: this.map.getCenter().lng().toFixed(4)
                }
            },
    //         curvedPath() {
    //              if (this.markers) {
    //             return range(100)
    //       .map(i => {
    //         const tick = i / 99

    //         /* Bezier curve -- set up the control points */
    //         const dlat = this.markers[0].position.lat - this.markers[0].position.lat
    //         const dlng = this.markers[0].position.lng - this.markers[0].position.lng

    //         const cp1 = {
    //           lat: this.markers[3].position.lat + 0.33 * dlat + 0.33 * dlng,
    //           lng: this.markers[3].position.lng - 0.33 * dlat + 0.33 * dlng,
    //         }

    //         const cp2 = {
    //           lat: this.markers[0].position.lat - 0.33 * dlat + 0.33 * dlng,
    //           lng: this.markers[0].position.lng - 0.33 * dlat - 0.33 * dlng,
    //         }

    //         /* Bezier curve formula */
    //         return {
    //           lat:
    //             (tick * tick * tick) * this.markers[3].position.lat +
    //             3 * ((1 - tick) * tick * tick) * cp1.lat +
    //             3 * ((1 - tick) * (1 - tick) * tick) * cp2.lat +
    //             ((1 - tick) * (1 - tick) * (1 - tick)) * this.markers[0].position.lat,
    //           lng:
    //             (tick * tick * tick) * this.markers[0].position.lng +
    //             3 * ((1 - tick) * tick * tick) * cp1.lng +
    //             3 * ((1 - tick) * (1 - tick) * tick) * cp2.lng +
    //             ((1 - tick) * (1 - tick) * (1 - tick)) * this.markers[0].position.lng,
    //         }
    //       })
    //   }
    // },
    // curvedPath2 () {
    //   /*
    //     FIXME: This formula will work for short distances away from
    //       the poles. It will not work once the curvature of the earth is
    //       too great
    //   */
    //   if (this.start && this.end) {
    //     return range(100)
    //       .map(i => {
    //         const tick = i / 99

    //         /* Bezier curve -- set up the control points */
    //         const dlat = this.end.latLng.lat() - this.start.latLng.lat()
    //         const dlng = this.end.latLng.lng() - this.start.latLng.lng()

    //         const cp1 = {
    //           lat: this.start.latLng.lat() + 0.33 * dlat + 0.33 * dlng,
    //           lng: this.start.latLng.lng() - 0.33 * dlat + 0.33 * dlng,
    //         }

    //         const cp2 = {
    //           lat: this.end.latLng.lat() - 0.33 * dlat + 0.33 * dlng,
    //           lng: this.end.latLng.lng() - 0.33 * dlat - 0.33 * dlng,
    //         }

    //         /* Bezier curve formula */
    //         return {
    //           lat:
    //             (tick * tick * tick) * this.start.latLng.lat() +
    //             3 * ((1 - tick) * tick * tick) * cp1.lat +
    //             3 * ((1 - tick) * (1 - tick) * tick) * cp2.lat +
    //             ((1 - tick) * (1 - tick) * (1 - tick)) * this.end.latLng.lat(),
    //           lng:
    //             (tick * tick * tick) * this.start.latLng.lng() +
    //             3 * ((1 - tick) * tick * tick) * cp1.lng +
    //             3 * ((1 - tick) * (1 - tick) * tick) * cp2.lng +
    //             ((1 - tick) * (1 - tick) * (1 - tick)) * this.end.latLng.lng(),
    //         }
    //       })
    //   }
    // }
        }
}
</script>

