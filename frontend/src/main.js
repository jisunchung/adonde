import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import VueKakaoSdk from 'vue-kakao-sdk'
import i18n from './i18n'
import router from './router'
import store from './store'
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'
import VueCascaderSelect from 'vue-cascader-select';
import VueConfetti from 'vue-confetti';
import VGoogleTranslate from "v-google-translate";
import * as VueGoogleMaps from 'vue2-google-maps'
import VueGeolocation from 'vue-browser-geolocation';
Vue.use(VueGeolocation);
 
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyBw4p75RbUNxOTRp97PsbKKMfHk3kisBhw',
    }
})
Vue.use(VueConfetti);
Vue.config.productionTip = false;
Vue.use(VGoogleTranslate)

Vue.component('modal', {
  template: '#modal-template'
})


Vue.use(VueCascaderSelect);

Vue.component('VueSlider', VueSlider)

Vue.config.productionTip = false

const apiKey = '75fadd5808d741eea9e1e3900de5a7a3'

window.Kakao.init(apiKey)

Vue.use(VueKakaoSdk, { apiKey })

new Vue({
  data: {
    showModal: false
  },
  VueCascaderSelect,
  store,
  vuetify,
  i18n,
  router,
  render: h => h(App)
}).$mount('#app')
