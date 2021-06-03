<template>
  <footer class="footer">
    <div class="container-fluid">
      <ul class="nav">
        <li class="nav-item">
          <a href="#" rel="noopener" class="nav-link" @click="white('home')">
            Home
          </a>
        </li>
        <li class="nav-item">
          <a href="#" rel="noopener" class="nav-link" @click="white('about')">
            About Us
          </a>
        </li>
        <li class="nav-item">
          <a href="#" rel="noopener" class="nav-link" @click="white('blog')">
            Blog
          </a>
        </li>
      </ul>
      <div class="copyright">
        &copy; {{ year }}, made with <i class="tim-icons icon-heart-2"></i> by

        <a style="font-weight: bold;">WebberWong</a>
        for AIOT Lab
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  data() {
    return {
      year: new Date().getFullYear(),
    };
  },
  methods: {
    white(id) {
      let docClasses = document.body.classList;
      docClasses.add("white-content");
      this.$router.push(id)
    },
  },
};
</script>
<style></style>
