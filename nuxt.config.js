const pkg = require('./package.json');
const scssCustomFunctions = require('./plugins/scss-functions.js');

module.exports = {
  mode: 'universal',

  /*
  ** Headers of the page
  */
  head: {
    titleTemplate: titleChunk => {
      return titleChunk ? `${titleChunk} - Danes je nov dan` : 'Danes je nov dan';
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      // hid is used as unique identifier if you want to override a tag in components
      { hid: 'description', name: 'description', content: pkg.description },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: 'icon',
        type: 'image/png',
        sizes: '32x32',
        href: '/favicon_32.png',
      },
      {
        rel: 'stylesheet',
        href: 'https://use.typekit.net/aqx7lip.css',
      },
    ],
  },

  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },

  /*
  ** Global CSS
  */
  css: ['~/assets/scss/main.scss'],

  /*
  ** Plugins to load before mounting the App
  */
  plugins: [{ src: '~/plugins/vue-waypoint', ssr: false }],

  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
    [
      'nuxt-i18n',
      {
        locales: [
          { code: 'sl', iso: 'sl-SI', file: 'sl-SI.json', name: 'Slovenščina' },
          // { code: 'en', iso: 'en-US', file: 'en-US.js', name: 'English' },
        ],
        defaultLocale: 'sl',
        encodePaths: false,
        baseUrl: 'https://danesjenovdan.si',
        langDir: 'lang/',
        lazy: true,
      },
    ],
  ],
  /*
  ** Axios module configuration
  */
  axios: {
    // See https://github.com/nuxt-community/axios-module#options
  },
  /*
  ** Build configuration
  */
  build: {
    extractCSS: true,
    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
      // Run ESLint on save
      if (ctx.isDev && ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/,
        });
      }

      // inject variables import to all scss modules
      const scssRule = config.module.rules.find(e => e.test.toString() === '/\\.scss$/i');
      const scssUses = scssRule.oneOf ? scssRule.oneOf.map(r => r.use) : [scssRule.use];
      scssUses.forEach(use => {
        const sassLoader = use.find(e => e.loader === 'sass-loader');
        if (sassLoader) {
          sassLoader.options = sassLoader.options || {};
          sassLoader.options.data = `
            @import '~/assets/scss/_variables.scss';
          `;
          sassLoader.options.functions = scssCustomFunctions;
        }
      });
    },
  },
};
