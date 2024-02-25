<template>
  <div class="d-flex justify-start">
    <template v-for="button in navigationButtons">
      <v-btn rounded variant="text">
        {{ button.name }}
      </v-btn>
    </template>
  </div>
</template>

<script>
export default {
  name: "NavigationBlockHeader",
  data() {
    return {
      navigationButtons: [
        {
          id: 1,
          name: "Главная",
        },
        {
          id: 2,
          name: "Игры",
        },
        {
          id: 3,
          name: "Жанры",
        },
        {
          id: 4,
          name: "Студии",
        },
      ],
    };
  },
};
</script>

<style scoped></style>
