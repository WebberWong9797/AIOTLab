<template>
  <base-nav
    v-model="showMenu"
    class="navbar-absolute top-navbar"
    type="white"
    :transparent="true"
  >
    <div slot="brand" class="navbar-wrapper">
      <div
        class="navbar-toggle d-inline"
        :class="{ toggled: $sidebar.showSidebar }"
      >
        <button type="button" class="navbar-toggler" @click="toggleSidebar">
          <span class="navbar-toggler-bar bar1"></span>
          <span class="navbar-toggler-bar bar2"></span>
          <span class="navbar-toggler-bar bar3"></span>
        </button>
      </div>
      <a class="navbar-brand ml-xl-3 ml-5" href="#pablo">{{ routeName }}</a>
    </div>
    <span class="d-lg-none">{{this.$strapi.user.username}}</span>
    <ul class="navbar-nav" :class="$rtl.isRTL ? 'mr-auto' : 'ml-auto'">
      <div v-if="this.$strapi.user">
        
        <base-dropdown
          tag="li"
          :menu-on-right="!$rtl.isRTL"
          title-tag="a"
          class="nav-item"
          title-classes="nav-link"
          menu-classes="dropdown-navbar"
        >
          <template slot="title">{{this.$strapi.user.username}}
            <div class="photo"><img :src="this.$store.getters.getuserInfo.avatar" /></div>
            <b class="caret d-none d-lg-block d-xl-block"></b>
          </template>
          <!--<li class="nav-link">
            <span href="#" class="nav-item dropdown-item">Hello </span>
          </li>
          <div class="dropdown-divider"></div>-->
          <li class="nav-link">
            <a href="#" class="nav-item dropdown-item" @click="logout()"
              >Log out</a
            >
          </li>
        </base-dropdown>
      </div>
    </ul>
  </base-nav>
</template>
<script>
import { CollapseTransition } from "vue2-transitions";
import { BaseNav, Modal } from "@/components";
//import axios from "axios";

export default {
  components: {
    CollapseTransition,
    BaseNav,
    Modal,
  },
  async mounted(){
    //console.log(this.$strapi.user)
    if(this.$strapi.user!==null){
      let result = await this.$strapi.find('users', {
        username: this.$strapi.user.username
      });
      //console.log("result: ", result)
      this.$store.commit('userInfo', result[0])
    }
  },
  computed: {
    routeName() {
      const { path } = this.$route;
      let parts = path.split("/");
      if (parts == ",") {
        return "Dashboard";
      }
      return parts.map((p) => this.capitalizeFirstLetter(p)).join(" ");
    },
    isRTL() {
      return this.$rtl.isRTL;
    },
  },
  data() {
    return {
      activeNotifications: false,
      showMenu: false,
      logModalVisible: false,
      Identifier: "",
      password: "",
      errmsg: "",
    };
  },
  methods: {
    capitalizeFirstLetter(string) {
      if (!string || typeof string !== "string") {
        return "";
      }
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    closeDropDown() {
      this.activeNotifications = false;
    },
    toggleSidebar() {
      this.$sidebar.displaySidebar(!this.$sidebar.showSidebar);
    },
    toggleMenu() {
      this.showMenu = !this.showMenu;
    },
    logout() {
      this.$strapi.logout();
      this.$router.push("/home");
    },
    profile(){
      this.$router.push("/user");
    }
  },
};
</script>
<style scoped>
.top-navbar {
  top: 0px;
}
.logDetails {
  margin: 10px 10%;
  width: 100%;
}
.errmsg {
  color: red;
}
</style>
