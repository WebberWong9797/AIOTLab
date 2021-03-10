<template>
  <b-container id="blog" class="pa-0" fluid tag="section">
    <h1 class="display-2">AIOT Blog</h1>

    <b-responsive class="mx-auto" max-width="1280">
      <b-container>
        <b-button @click="getCategory2('all')">Show ALL</b-button>
        <b-row>
          <b-col
            v-for="(post, i) in posts"
            :key="i"
            :style="post.show"
            cols="12"
            md="4"
          >
              <mdb-card class="blogcard">
                <img class="blogimg" :src="post.src" alt="no image" />
                <mdb-card-body>
                  <mdb-card-title>{{ post.title }}</mdb-card-title>
                  <mdb-card-text class="blogbody">{{
                    post.blurb
                  }}</mdb-card-text>
                  <span>Tags : </span><br />
                  <b-row
                    v-for="(tag, i) in post.tags"
                    :key="i"
                    class="d-flex"
                    cols="12"
                    md="4"
                  >
                    <b-button
                      color="#252525"
                      dark
                      class="btn-sm"
                      @click="getCategory2(tag.tag_name)"
                      >{{ tag ? tag.tag_name : "None" }}</b-button
                    >
                  </b-row>
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
  created() {
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
            category: data[i].Category === null ? "None" : data[i].Category,
            date: data[i].updated_at,
            blurb: data[i].description,
            src: url,
            title: data[i].title,
            tags: data[i].tags,
            show: 'display: flex;',
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
    async getCategory2(item) {
      console.log(item);
      //var post = this.posts
      if (item == "all") {
        for (let i = 0; i < this.posts.length; i++) this.posts[i].show = 'display: flex;';
      } else {
        for (let i = 0; i < this.posts.length; i++) {
          console.log(item);
          var obj = [];
          for (let j = 0; j < this.posts[i].tags.length; j++)
            obj.push(this.posts[i].tags[j].tag_name);
          if (obj.includes(item)) this.posts[i].show = 'display: flex;';
          else this.posts[i].show = 'display: none;';
        }
      }
    },
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
            tags: result.data[i].tags,
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
.rounded {
  border-radius: 8px !important;
  cursor: pointer;
}
.blogimg {
  height: 250px;
  width: auto;
}
.card-wrapper .card-rotating {
  height: auto;
}
.face.back {
  height: auto;
}
</style>
