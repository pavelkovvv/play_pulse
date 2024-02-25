<template>
  <v-navigation-drawer
    v-model="show"
    elevation="2"
    transition="slide-x-transition"
  >
    <v-list>
      <v-list-item title="Navigation drawer"></v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: "NavigationBar",
  props: {
    showNavBar: {
      required: true,
      type: Boolean,
    },
  },
  data() {
    return {
      show: this.showNavBar,
    };
  },
  watch: {
    showNavBar: {
      handler() {
        this.show = this.showNavBar;
      },
    },
  },
};
</script>

<style scoped></style>
