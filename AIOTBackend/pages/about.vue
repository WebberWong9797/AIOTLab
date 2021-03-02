<template>
  <v-container id="about" class="pa-0" fluid tag="section">
    <b-row class="ma-0" no-gutters>
      <b-col cols="6" md="6">
        <img class="aboutimg" :src="require('~/assets/banner1.jpg')" />
        <img class="aboutimg" :src="require('~/assets/banner2.jpg')" />
      </b-col>
      <b-col class="topIntro" cols="6" md="6">
        <div v-html="this.topIntro"></div
      ></b-col>
    </b-row>
    <div
      class="d-block d-md-flex align-center grey lighten-3 pa-6"
      cols="12"
      md="6"
    >
      <div class="mx-auto px-3 px-md-12" max-width="650">
        <div class="signature">Sengital Aiot Team</div>
      </div>
    </div>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  name: "About",
  layout: "navbar",
  data() {
    return {
      topIntro: "",
      rules: [
        [/\*\*(.*?)\*\*/g, "<b class=black--text>$1</b>"],
        [/__(.*?)__/g, "<u>$1</u>"],
        [/~~(.*?)~~/g, "<i>$1</i>"],
        [/--(.*?)--/g, "<del>$1</del>"],
        [/<<(.*?)>>/g, "<a href='$1'>Link</a>"],
        [/[\n\r]/g, "<br>"],
        [/#(.*?)#/g, "<h1>$1</h1>"],
        [/##(.*?)##/g, "<h2>$1</h2>"],
        [/###(.*?)###/g, "<h3>$1</h3>"],
        [/####(.*?)####/g, "<h4>$1</h4>"],
        [/#####(.*?)#####/g, "<h5>$1</h5>"],
        [/######(.*?)######/g, "<h6>$1</h6>"],
      ],
    };
  },
  async created() {
    const result = await axios.get(
      this.$store.state.BASE_URL + "/aiot-webcontent"
    );
    if (result.error) {
      console.log(result.error);
    } else {
      this.topIntro = result.data.about;
      let html = result.data.about;
      this.rules.forEach(([rule, template]) => {
        html = html.replace(rule, template);
      });
      this.topIntro = html;
    }
  },
};
</script>

<style lang="sass">
.signature
  font-family: 'Cedarville Cursive', cursive !important
  font-size: 2rem
  font-style: italic
.aboutimg
  width: 100%
  padding: 0px 50px
.topIntro
  padding-top: 20px
</style>
