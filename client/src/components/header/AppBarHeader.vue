<template>
  <v-app-bar :elevation="3">
    <template v-slot:prepend>
      <v-app-bar-nav-icon @click="clickMenu()"></v-app-bar-nav-icon>
      <navigation-block-header />
    </template>
    <template v-slot:default>
      <search-header />
    </template>
    <template v-slot:append>
      <user-block-header />
    </template>
  </v-app-bar>
</template>

<script>
import NavigationBlockHeader from "@/components/header/NavigationBlockHeader.vue";
import UserBlockHeader from "@/components/header/UserBlockHeader.vue";
import SearchHeader from "@/components/header/SearchHeader.vue";

export default {
  name: "AppBarHeader",
  components: { SearchHeader, UserBlockHeader, NavigationBlockHeader },
  data() {
    return {
      showNavBar: false,
    };
  },
  methods: {
    clickMenu() {
      this.showNavBar = !this.showNavBar;
      this.$emit("showNavBar", this.showNavBar);
    },
  },
};
</script>

<style scoped></style>
