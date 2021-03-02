<template>
  <b-container id="blog" class="pa-0" fluid tag="section">
    <b-img
      :src="require('~/assets/luke-matthews-T4PTfNwgbEM-unsplash.jpg')"
      v-bind="$attrs"
      class="text-center white--text align-center"
      height="40vh"
    >
      <h1 class="display-2">AIOT Blog</h1>
    </b-img>

    <b-responsive class="mx-auto" max-width="1280">
      <b-container>
        <b-tabs
          v-if="showTabs"
          background-color="transparent"
          centered
          hide-slider
        >
          <b-tab
            v-for="(tab, i) in uniqueCat"
            :key="i"
            @click="getCategory(tab)"
          >
            {{ tab }}
          </b-tab>
        </b-tabs>
        <b-row>
          <b-col
            v-for="(post, i) in posts"
            :key="i"
            class="d-flex"
            cols="12"
            md="4"
          >
            <mdb-card class="blogcard">
              <mdb-card-image
                class="blogimg"
                :src="post.src"
                alt="no image"
              ></mdb-card-image>
              <mdb-card-body>
                <mdb-card-title>{{ post.title }}</mdb-card-title>
                <mdb-card-text class="blogbody">{{ post.blurb }}</mdb-card-text>
                <span>Tags : </span><br />
                <b-button color="#252525" dark class="btn-sm">{{
                  post.category
                }}</b-button>
              </mdb-card-body>
            </mdb-card>
          </b-col>
        </b-row>
      </b-container>
    </b-responsive>
  </b-container>
</template>

<script>
import axios from "axios";
import {
  mdbContainer,
  mdbRow,
  mdbCol,
  mdbCard,
  mdbCardImage,
  mdbCardHeader,
  mdbCardBody,
  mdbCardTitle,
  mdbCardText,
  mdbCardFooter,
  mdbCardUp,
  mdbCardAvatar,
  mdbCardGroup,
  mdbBtn,
  mdbView,
  mdbMask,
  mdbIcon,
} from "mdbvue";
export default {
  name: "Blog",
  layout: "navbar",
  components: {
    mdbContainer,
    mdbRow,
    mdbCol,
    mdbCard,
    mdbCardImage,
    mdbCardHeader,
    mdbCardBody,
    mdbCardTitle,
    mdbCardText,
    mdbCardFooter,
    mdbCardUp,
    mdbCardAvatar,
    mdbCardGroup,
    mdbBtn,
    mdbView,
    mdbMask,
    mdbIcon,
  },
  data() {
    return {
      showTabs: false,
      select: "",
      uniqueCat: [],
      posts: [],
      team: ["All", "Admin", "IT", "AHAS", "BLESS", "LoRa"],
      photo: "",
    };
  },
  mounted() {
    fetch("https://cms.aiotlab.hk/projects")
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        const category = [];

        for (let i = 0; i < data.length; i++) {
          category.push(data[i].Category);
          let url = "";
          if (data[i].photo.length !== 0)
            url = this.$store.state.BASE_URL + data[i].photo[0].url;
          else
            url =
              "https://cms.aiotlab.hk/uploads/small_no_image_b495419a66.png?2144.96499998495";
          const blog = {
            id: data[i].id,
            category: data[i].Category,
            date: data[i].updated_at,
            blurb: data[i].description,
            src: url,
            title: data[i].title,
          };
          console.log(blog);
          this.posts.push(blog);
        }
        this.uniqueCat = category.filter((a, b) => category.indexOf(a) === b);
        this.uniqueCat.unshift("ALL");
        console.log(this.uniqueCat);
      });
  },
  methods: {
    async getCategory(item) {
      console.log(item);
      this.posts = [];
      let cat = "";
      if (item === "ALL") cat = "/projects";
      else cat = "/projects/?Category=" + item;
      const result = await axios.get(this.$store.state.BASE_URL + cat);
      if (result.error) {
        console.log(result.error);
      } else {
        console.log(result);
        for (let i = 0; i < result.data.length; i++) {
          let url = "";
          if (result.data[i].photo.length !== 0)
            url = result.data[i].photo[0].url;
          else url = "";
          const blog = {
            id: result.data[i].id,
            category: result.data[i].Category,
            date: result.data[i].updated_at,
            blurb: result.data[i].description,
            src: this.$store.state.BASE_URL + url,
            title: result.data[i].title,
          };
          console.log(blog);
          this.posts.push(blog);
        }
      }
    },
    async projectSubmit(item) {
      const result = await axios.get(
        this.$store.state.BASE_URL + "/projects/" + item
      );
      if (result.error) {
        console.log(result.error);
      } else {
        console.log(result);
        this.$store.commit("projectInfo", result);
        this.$router.push("/BlogDetails");
      }
    },
  },
};
</script>
<style scoped>
.b-card {
  width: -webkit-fill-available;
  max-height: 410px;
  overflow: hidden;
  text-overflow: ellipsis;
}
p.blogbody.card-text {
  max-height: 60px;
  text-overflow: ellipsis;
  overflow: hidden;
}
</style>
