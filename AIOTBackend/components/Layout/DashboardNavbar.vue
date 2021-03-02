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

    <ul class="navbar-nav" :class="$rtl.isRTL ? 'mr-auto' : 'ml-auto'">
      <div v-if="this.$store.getters.getuserInfo.loggedIn">
        <base-dropdown
          tag="li"
          :menu-on-right="!$rtl.isRTL"
          title-tag="a"
          title-classes="nav-link"
          class="nav-item"
        >
          <template slot="title">
            <div class="notification d-none d-lg-block d-xl-block"></div>
            <i class="tim-icons icon-sound-wave"></i>
            <p class="d-lg-none">New Notifications</p>
          </template>
          <li class="nav-link">
            <a href="#" class="nav-item dropdown-item"
              >Mike John responded to your email</a
            >
          </li>
          <li class="nav-link">
            <a href="#" class="nav-item dropdown-item">You have 5 more tasks</a>
          </li>
          <li class="nav-link">
            <a href="#" class="nav-item dropdown-item"
              >Your friend Michael is in town</a
            >
          </li>
          <li class="nav-link">
            <a href="#" class="nav-item dropdown-item">Another notification</a>
          </li>
          <li class="nav-link">
            <a href="#" class="nav-item dropdown-item">Another one</a>
          </li>
        </base-dropdown>
        <base-dropdown
          tag="li"
          :menu-on-right="!$rtl.isRTL"
          title-tag="a"
          class="nav-item"
          title-classes="nav-link"
          menu-classes="dropdown-navbar"
        >
          <template slot="title">
            <div class="photo"><img src="" /></div>
            <b class="caret d-none d-lg-block d-xl-block"></b>
            <p class="d-lg-none">Log out</p>
          </template>
          <li class="nav-link">
            <a href="#" class="nav-item dropdown-item">Profile</a>
          </li>
          <li class="nav-link">
            <a href="#" class="nav-item dropdown-item">Settings</a>
          </li>
          <div class="dropdown-divider"></div>
          <li class="nav-link">
            <a href="#" class="nav-item dropdown-item" @click="logout()"
              >Log out</a
            >
          </li>
        </base-dropdown>
      </div>
      <div v-else>
        <div class="search-bar input-group" @click="logModalVisible = true">
          <button class="btn btn-link" id="search-button">
            <i class="tim-icons icon-button-power"></i>
            <span>Login</span>
          </button>
          <!-- You can choose types of search input -->
        </div>
        <modal
          :show.sync="logModalVisible"
          class=""
          id="searchModal"
          :centered="false"
          :show-close="true"
          ><b-row>
            <base-input
              v-model="Identifier"
              type="text"
              class="logDetails"
              label="Identifier(Username / Email): "
            ></base-input>
          </b-row>
          <b-row>
            <base-input
              v-model="password"
              type="password"
              class="logDetails"
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
        </modal>
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
    async login() {
      let x = await this.$strapi.login({
        identifier: this.Identifier,
        password: this.password,
      });
      try {
        this.errmsg = x.e.message;
      } catch (e) {
        this.$router.push("/home");
      }

      console.log(x);
    },
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
