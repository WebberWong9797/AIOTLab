<template>
  <div class="login">
    <b-row>
      <span class="heading">Sengital AIOT Lab</span>
    </b-row>
    <b-row>
      <base-input
        v-model="username"
        class="newM col-lg-12 col-md-3 col-sm-4 col-xs-6 col-xs-6"
        label="Username / Email: "
      ></base-input>
    </b-row>
    <b-row>
      <base-input v-model="password" type="password" class="newM col-lg-12 col-md-3 col-sm-4 col-xs-6 col-xs-6" label="Password: "></base-input>
    </b-row>
    <div class="errmsg">{{ this.errmsg }}</div>
    <base-button
      type="primary"
      class="mr-3 col-lg-4 col-md-3 col-sm-4 col-xs-6 col-xs-6"
      @click="login()"
    >
      <i class="tim-icons icon-wallet-43"></i>
      <span class="caption text-uppercase"> Login </span>
    </base-button>
  </div>
</template>
<script>
export default {
  name: "login",
  layout: "blank",
  data() {
    return {
      username: "",
      password: "",
      errmsg: "",
    };
  },
  computed: {
    enableRTL() {
      return this.$route.query.enableRTL;
    },
    isRTL() {
      return this.$rtl.isRTL;
    },
  },
  methods: {
    async login() {
      try{ 
        let result = await this.$strapi.login({
        identifier: this.username,
        password: this.password,
      });
      //console.log(result)
      console.log(this.$strapi.user)
      this.$store.commit('userInfo', this.$strapi.user)
      //this.$store.getters.getuserInfo.avatar)
      this.$router.push('/dashboard')
      }catch(e){
        //console.log(e.toString().replace("HTTPError: ",""))
        this.errmsg = e.toString().replace("HTTPError: ","")

      }

    },
  },
};
</script>
<style>
.errmsg {
  color: red;
}
.login {
  position: fixed;
  top: 50%;
  left: 50%;
  margin-top: -100px;
  margin-left: -200px;
}
.heading {
  padding-left: 15px;
  font-size: 50px;
}
</style>
