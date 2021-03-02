import Vue from 'vue'
//https://www.emqx.io/blog/how-to-use-mqtt-in-vue 
import VueMqtt from 'vue-mqtt';
if (process.browser) {
  const mqtt = require('vue-mqttsocket').default
  Vue.use(mqtt, {uri: 'ws://10.0.0.70:9001'}, {username: 'tiger', password: 'tiger'})
  
}   