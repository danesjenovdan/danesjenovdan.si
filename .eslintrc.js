const path = require('path');
const INLINE_ELEMENTS = require('eslint-plugin-vue/lib/utils/inline-non-void-elements.json');

module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
  },
  parserOptions: {
    parser: 'babel-eslint',
  },
  extends: ['@nuxtjs', 'plugin:prettier/recommended'],
  plugins: ['prettier'],
  // add your custom rules here
  rules: {
    'no-console': ['warn'],
    'vue/singleline-html-element-content-newline': ['off'],
    'vue/multiline-html-element-content-newline': ['off'],
    'vue/html-self-closing': ['warn', { html: { void: 'always' } }],
    'import/extensions': ['error', 'always', { ignorePackages: true }],
    'import/no-unresolved': ['error'],
    'import/no-extraneous-dependencies': [
      'error',
      { devDependencies: true, optionalDependencies: false, peerDependencies: false },
    ],
    quotes: ['error', 'single', { avoidEscape: true }],
  },
  settings: {
    'import/resolver': {
      alias: [['~', `${path.resolve(__dirname)}/`]],
    },
    // stop warnings about vue not being in the dependencies list since nuxt
    // will always have a version available in it's own dependency tree
    'import/core-modules': ['vue'],
  },
};
