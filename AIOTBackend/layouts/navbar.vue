<template>
  <div>
    <base-nav type="white">
      <div class="d-flex align-center nav-left">
        <a href="https://sengital.com/" target="_blank">
          <img
            :src="require('@/assets/SengitalLogo.png')"
            contain
            class="shrink mr-2"
            height="50"
            width="150"
          />
        </a>
        <div
          class="primary--text headline font-italic"
          style="font-size: 20px; align-self: center;"
        >
          <span class="font-weight-bold">AIOT</span>Lab
        </div>
      </div>
      <ul class="navbar-nav">
        <li class="nav-item active" v-for="(link, i) in button" :key="i">
          <a class="nav-link" :href="link">{{ link }} </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#" @click="login()">LOGIN</a>
        </li>
      </ul>
    </base-nav>
    <v-content class="ma-4" style="padding: 60px 0px 0px;">
      <Nuxt />
    </v-content>
    <content-footer></content-footer>
  </div>
</template>

<script>
import { BaseNav } from "@/components";
import ContentFooter from "@/components/Layout/ContentFooter.vue";
import SidebarShare from "@/components/Layout/SidebarSharePlugin";
export default {
  name: "nav-bar",
  components: {
    BaseNav,
    SidebarShare,
    ContentFooter,
  },
  data: () => ({
    sidebarBackground: "vue",
    button: ["HOME", "ABOUT", "CONTACT", "NEWS", "BLOG", "DASHBOARD", ""],
  }),
  mounted() {
    let docClasses = document.body.classList;
    docClasses.add("white-content");
  },
  methods: {
    login(){
      this.$router.push("/login")
    }
  }
};
</script>

<style scoped>
.navbar-nav {
  font-size: 20px;
  margin-left: auto;
}
.navbar.bg-white .navbar-nav a.nav-link:hover {
  color: rgb(120, 242, 246) !important;
}
</style>
