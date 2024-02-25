<template>
  <v-container>
    <news-main />
  </v-container>
</template>

<script>
import NewsMain from "@/components/main/news/newsMain.vue";

export default {
  name: "Home",
  components: { NewsMain },
};
</script>

<style scoped></style>
