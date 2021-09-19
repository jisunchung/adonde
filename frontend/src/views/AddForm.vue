<template>
    <v-app style="background-color: #08844E">
    <v-container>
        <v-card>
            <v-card-text>
                 <form>
      <h1>post</h1>
      <div class="work-experiences">

        <div class="form-row" v-for="(experience, index) in workExperiences" :key="index">
          <div class="form-group col-md-6">
            <label>Name</label><br>
            <input v-model="experience.company" :name="`workExperiences[${index}][company]`" type="text" class="form-control" placeholder="input name">
          </div>
          <div class="form-group col-md-6">
            <label>Address</label><br>
            <input v-model="experience.title" :name="`workExperiences[${index}][title]`" type="text" class="form-control" placeholder="input address">
          </div>
          <div class="form-group col-md-6">
            <label>image</label>
            <v-file-input 
                @change="Preview_image(index)"
                v-model="experience.image"
                >
                </v-file-input>
            <v-img :src="experience.url" width=100></v-img>
           
          </div>
          
          
        </div>
      </div>

      <div class="form-group">
        <v-btn @click="addExperience" type="button" class="btn btn-secondary">Add form</v-btn>
      </div>
      <br>

      <div class="form-group">
       
      </div>
    </form>
      <v-btn
        class="white--text"
        color="teal"
        @click="[overlay = false,submit()]"
      >
        submit
      </v-btn>

            </v-card-text>
        </v-card>
    </v-container>
    </v-app>
</template>

<script>
export default {
    data(){
        return{
            workExperiences: [
      {
        Name: "Foxconn",
        Address: "Engineer",
        image: null,
        url:null
      }]
        }    
    },
    methods: {
        addExperience () {
      this.workExperiences.push({
        company: '',
        title: ''
      })
    },

    submit () {
      const data = {
        workExperiences: this.workExperiences
      }
      alert(JSON.stringify(data, null, 2))
history.back()

    },
    Preview_image(i) {
      this.workExperiences[i].url= URL.createObjectURL(this.workExperiences[i].image)
    }
    }
}
</script>