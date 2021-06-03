<template>
  <div class="home">
    <container class="top">
      <div class="scheme-group">
        <h1 style="padding-top: 10px"></h1>
        <div class="schemes-box">
          <VueSlickCarousel v-bind="cardCarouselSetting">
            <div v-for="n in getEvents" :key="n.id">
              <img
                :src="'https://cms.aiotlab.hk' + n.url"
                :alt="n.name"
                class="banner-img"
              />
            </div>
          </VueSlickCarousel>
        </div>
      </div>
    </container>
  </div>
</template>
<script>
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
import axios from "axios";
export default {
  layout: "navbar",
  components: { VueSlickCarousel },
  data() {
    return {
      cardCarouselSetting: {
        arrows: true,
        dots: true,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        speed: 4000,
        autoplaySpeed: 5000,
        responsive: [
          {
            breakpoint: 992,
            settings: {
              slidesToShow: 3,
            },
          },
          {
            breakpoint: 768,
            settings: {
              slidesToShow: 2,
            },
          },
          {
            breakpoint: 700,
            settings: {
              slidesToShow: 1,
            },
          },
        ],
      },
      events: [
        {
          id: 1,
          image: require("~/assets/banner1.jpg"),
        },
        {
          id: 2,
          image: require("~/assets/banner2.jpg"),
        },
        {
          id: 3,
          image: require("~/assets/banner3.jpg"),
        },
      ],
    };
  },
  computed: {
    getEvents() {
      return this.events;
    },
  },
  async created() {
    const result = await axios.get(
      this.$store.state.BASE_URL + "/aiot-webcontent"
    );
    if (result.error) {
      console.log(result.error);
    } else {
      this.events = result.data.home_banner;
      console.log(result.data.home_banner)
    }
  },
  mounted() {
    let docClasses = document.body.classList;
    docClasses.add("white-content");
  },
};
</script>
<style>
.banner-img {
  height: 700px;
  width: 100%;
  object-fit: contain;
}
.scheme-group {
  margin-bottom: 40px;
}
.intro-left {
  background-color: blue;
}
.intro-right {
  background-color: #1cbcb4;
}
.home {
  background-color: white !important;
}
</style>
