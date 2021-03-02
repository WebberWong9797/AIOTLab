<template>
  <div>
    <b-row>
      <base-input
        class="newM col-lg-4 col-md-3 col-sm-4 col-xs-6 col-xs-6"
        label="ph Value: "
      ></base-input>
      <base-input
        v-model="password"
        class=""
        label="Password: "
      ></base-input>
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
  layout: "navbar",
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
    
  },
};
</script>
<style></style>
