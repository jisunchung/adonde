<template>
       <v-app
        style="background-color: #08844E">
        <v-row>
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
                <v-img 
                style="margin: auto"
                alt="map"
                contain
                :src="require(`@/assets/map.jpeg`)"
                width="700"
                />
            </v-col>
        </v-row>

       </v-app>
</template>

