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
    'vue/singleline-html-element-content-newline': [
      'warn',
      {
        ignoreWhenNoAttributes: true,
        ignoreWhenEmpty: true,
        ignores: ['nuxt-link', 'pre', 'textarea', ...INLINE_ELEMENTS],
      },
    ],
    'vue/multiline-html-element-content-newline': [
      'warn',
      {
        ignoreWhenEmpty: true,
        ignores: ['nuxt-link', 'pre', 'textarea', ...INLINE_ELEMENTS],
        allowEmptyLines: false,
      },
    ],
  },
};
