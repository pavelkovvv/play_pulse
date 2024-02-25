<template>
  <div class="search">
    <v-text-field
      label="Поиск"
      prepend-inner-icon="mdi-magnify"
      density="compact"
      variant="outlined"
    ></v-text-field>
  </div>
</template>

<script>
export default {
  name: "SearchHeader",
};
</script>

<style scoped>
.search {
  width: 30%;
}

.v-input >>> .v-input__details {
  grid-area: initial !important;
}

.v-text-field {
  border-radius: 10px !important;
}
</style>
