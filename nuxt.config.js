import scssCustomFunctions from './plugins/scss-functions.js';

export default {
  mode: 'universal',
  /*
   ** Server configuration
   */
  server: {
    port: 3001, // default: 3000
  },
  /*
   ** Headers of the page
   */
  head: {
    titleTemplate: (titleChunk) => {
      return titleChunk
        ? `${titleChunk} - Danes je nov dan`
        : 'Danes je nov dan';
    },
    meta: [
      {
        charset: 'utf-8',
      },
      {
        name: 'viewport',
        content: 'width=device-width, initial-scale=1',
      },
      {
        name: 'theme-color',
        content: '#ffffff',
      },
      {
        hid: 'description',
        name: 'description',
        content:
          'Negujemo kritično misel. Postavljamo druga vprašanja. Hekamo nov dan. Skrbimo za varen, vključujoč in sodoben splet. In svet. Verjamemo v skupnost. Naše merilo je veselje do življenja.',
      },
      {
        hid: 'fb:app_id',
        property: 'fb:app_id',
        content: '301375193309601',
      },
      {
        hid: 'og:site_name',
        property: 'og:site_name',
        content: 'Danes je nov dan',
      },
      {
        hid: 'og:type',
        property: 'og:type',
        content: 'website',
      },
      {
        hid: 'og:title',
        property: 'og:title',
        content: 'Danes je nov dan',
      },
      {
        hid: 'og:description',
        property: 'og:description',
        content:
          'Negujemo kritično misel. Postavljamo druga vprašanja. Hekamo nov dan. Skrbimo za varen, vključujoč in sodoben splet. In svet. Verjamemo v skupnost. Naše merilo je veselje do življenja.',
      },
      {
        hid: 'og:image',
        property: 'og:image',
        content: 'https://danesjenovdan.si/djnd-og.png',
      },
      {
        hid: 'twitter:creator',
        name: 'twitter:creator',
        content: '@danesjenovdan',
      },
      {
        hid: 'twitter:card',
        name: 'twitter:card',
        content: 'summary_large_image',
      },
      {
        hid: 'twitter:title',
        name: 'twitter:title',
        content: 'Danes je nov dan',
      },
      {
        hid: 'twitter:description',
        name: 'twitter:description',
        content:
          'Negujemo kritično misel. Postavljamo druga vprašanja. Hekamo nov dan. Skrbimo za varen, vključujoč in sodoben splet. In svet. Verjamemo v skupnost. Naše merilo je veselje do življenja.',
      },
      {
        hid: 'twitter:image',
        name: 'twitter:image',
        content: 'https://danesjenovdan.si/djnd-og.png',
      },
    ],
    link: [
      {
        rel: 'icon',
        type: 'image/x-icon',
        href: '/favicon.ico',
      },
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
    // script: [{
    //     src: 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js'
    //   },
    //   {
    //     src: 'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.4.1/js/bootstrap.min.js',
    //   },
    // ],
  },
  /*
   ** Customize the progress-bar color
   */
  loading: {
    color: '#fff',
  },
  /*
   ** Global CSS
   */
  css: ['~/assets/scss/main.scss'],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [
    {
      src: '~/plugins/vue-waypoint.js',
      mode: 'client',
    },
    {
      src: '~/plugins/vue-avatar-cropper.js',
      mode: 'client',
    },
    {
      src: '~/plugins/matomo.js',
      ssr: false,
    },
  ],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
    '@nuxtjs/eslint-module',
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
    '@nuxtjs/style-resources',
    [
      'nuxt-i18n',
      {
        locales: [
          {
            code: 'sl',
            iso: 'sl-SI',
            file: 'sl-SI.json',
            name: 'Slovenščina',
          },
          { code: 'en', iso: 'en-US', file: 'en-US.json', name: 'English' },
        ],
        defaultLocale: 'sl',
        encodePaths: false,
        baseUrl: 'http://nov.djnd.si',
        langDir: 'lang/',
        lazy: true,
      },
    ],
  ],
  /*
   ** Nuxt Style Resources
   ** See https://github.com/nuxt-community/style-resources-module
   */
  styleResources: {
    scss: ['~/assets/scss/_variables.scss'],
  },
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {},
  /*
   ** Build configuration
   */
  build: {
    extractCSS: true,
    /*
     ** You can extend webpack config here
     */
    extend(config, ctx) {
      // inject variables import to all scss modules
      const scssRule = config.module.rules.find(
        (e) => e.test.toString() === '/\\.scss$/i',
      );
      const scssUses = scssRule.oneOf
        ? scssRule.oneOf.map((r) => r.use)
        : [scssRule.use];
      scssUses.forEach((use) => {
        const sassLoader = use.find((e) => e.loader === 'sass-loader');
        if (sassLoader) {
          sassLoader.options = sassLoader.options || {};
          sassLoader.options.sassOptions = sassLoader.options.sassOptions || {};
          sassLoader.options.sassOptions.functions = scssCustomFunctions;
        }
      });
    },
  },
};
