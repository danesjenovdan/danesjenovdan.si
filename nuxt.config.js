const pkg = require('./package');

module.exports = {
  mode: 'universal',

  /*
  ** Headers of the page
  */
  head: {
    title: pkg.name,
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
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
  plugins: [],

  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    // Doc: https://bootstrap-vue.js.org/docs/
    'bootstrap-vue/nuxt',
    '@nuxtjs/pwa',
    [
      'nuxt-i18n',
      {
        locales: [
          { code: 'sl', iso: 'sl-SI', file: 'sl-SI.json', name: 'Slovenščina' },
          { code: 'en', iso: 'en-US', file: 'en-US.js', name: 'English' },
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
  ** Bootstrap Vue module configuration
  */
  bootstrapVue: {
    // bootstrapCSS: true, // or `css`
    // bootstrapVueCSS: true, // or `bvCSS`
  },

  /*
  ** Build configuration
  */
  build: {
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
        }
      });
    },
  },
};
