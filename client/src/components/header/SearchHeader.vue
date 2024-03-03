<template>
  <div class="search">
    <v-text-field
      class="search-field"
      label="Поиск"
      prepend-inner-icon="mdi-magnify"
      density="compact"
      variant="outlined"
      rounded
      bg-color="rgba(0, 202, 111, 0.08)"
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

.search-field {
}

.v-input >>> .v-input__details {
  grid-area: initial !important;
  display: none !important;
}
</style>
