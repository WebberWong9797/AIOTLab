<template>
  <footer class="footer">
    <div class="container-fluid">
      <ul class="nav">
        <li class="nav-item">
          <a href="home" rel="noopener" class="nav-link">
            Home
          </a>
        </li>
        <li class="nav-item">
          <a href="about" target="_blank" rel="noopener" class="nav-link">
            About Us
          </a>
        </li>
        <li class="nav-item">
          <a href="/blog" target="_blank" rel="noopener" class="nav-link">
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
};
</script>
<style></style>
