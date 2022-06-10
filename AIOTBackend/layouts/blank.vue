<template>
  <div class="my-auto">
    <Nuxt />
  </div>
</template>

<script>
export default {
  name: "blank",
  mounted() {
    let docClasses = document.body.classList;
    docClasses.add("white-content");
  },
};
</script>

<style scoped>
</style>
