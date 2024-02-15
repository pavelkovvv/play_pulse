// Plugins
import Components from 'unplugin-vue-components/vite'
import Vue from '@vitejs/plugin-vue'
import Vuetify, {transformAssetUrls} from 'vite-plugin-vuetify'
import ViteFonts from 'unplugin-fonts/vite'

// Utilities
import {defineConfig} from 'vite'
import {fileURLToPath, URL} from 'node:url'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        Vue({
            template: {transformAssetUrls}
        }),
        // https://github.com/vuetifyjs/vuetify-loader/tree/master/packages/vite-plugin#readme
        Vuetify(),
        Components(),
        ViteFonts({
            google: {
                families: [{
                    name: 'Roboto',
                    styles: 'wght@100;300;400;500;700;900',
                }],
            },
        }),
    ],
    define: {'process.env': {}},
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        },
        extensions: [
            '.js',
            '.json',
            '.jsx',
            '.mjs',
            '.ts',
            '.tsx',
            '.vue',
        ],
    },
    build: {
        outDir: fileURLToPath(new URL('../play_pulse/static/dist', import.meta.url)), // Абсолютный путь к папке static
        assetsDir: '', // Очистить assetsDir, чтобы не добавлять хэш в имена файлов
        emptyOutDir: true, // Очищать outDir перед каждой сборкой
        rollupOptions: {
            output: {
                entryFileNames: '[name].js', // Здесь [name] будет заменено на имя вашего входного файла
                chunkFileNames: '[name].js', // Здесь [name] будет заменено на имя чанка файла
                assetFileNames: '[name][extname]', // Здесь [name] будет заменено на имя файла ресурса
            },
        },
    },
    server: {
        port: 3000,
    },
    base: './',
})
