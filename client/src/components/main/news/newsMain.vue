<template>
  <div>
    <v-carousel
      cycle
      height="400"
      hide-delimiter-background
      show-arrows="hover"
    >
      <v-carousel-item
        v-for="itemNews in news"
        :src="itemNews.src"
        cover
      ></v-carousel-item>
    </v-carousel>
  </div>
</template>

<script>
export default {
  name: "newsMain",
  data() {
    return {
      news: [
        {
          src: "https://img.goodfon.ru/wallpaper/nbig/0/93/cyberpunk-2077-katana-phantom-liberty-nait-siti.webp",
        },
        {
          src: "https://img.goodfon.ru/wallpaper/nbig/3/1a/igra-game-rockstar-games-gta-6-gta-vi-grand-theft-auto-vi.webp",
        },
        {
          src: "https://img.goodfon.ru/wallpaper/nbig/d/4e/marvels-spider-man-2-marvel-chelovek-pauk-2-insomniac-game-1.webp",
        },
      ],
    };
  },
};
</script>

<style scoped></style>
