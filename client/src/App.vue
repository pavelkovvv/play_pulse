<template>
  <v-app>
    <app-bar-header @showNavBar="this.showNavBar = $event" />
    <navigation-bar :show-nav-bar="showNavBar" />
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import AppBarHeader from "@/components/header/AppBarHeader.vue";
import NavigationBar from "@/components/navigationBar/NavigationBar.vue";

export default {
  name: "App",
  components: { AppBarHeader, NavigationBar },
  data() {
    return {
      showNavBar: false,
    };
  },
};
</script>

<style scoped></style>
