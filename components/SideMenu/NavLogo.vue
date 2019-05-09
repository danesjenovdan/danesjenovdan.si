<template>
  <header class="logo d-none d-md-block">
    <div class="logo__mark">
      <nuxt-link :to="localePath('index')">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="73 69 300 300">
          <defs>
            <clipPath id="navlogoclip" transform="translate(65.03 61)">
              <circle cx="158.15" cy="157.81" r="150" fill="none"></circle>
            </clipPath>
          </defs>
          <g clip-path="url(#navlogoclip)">
            <path d="M-.005 292.286L127.993.004l64.762 28.361L64.757 320.647z" fill="#cfad54"></path>
            <path d="M64.765 320.632L192.764 28.351l64.762 28.361-127.999 292.281z" fill="#df786c"></path>
            <path d="M129.53 349.012l128-292.281 64.762 28.36-127.999 292.282z" fill="#6ca89f"></path>
            <path d="M194.292 377.363L322.291 85.082l64.762 28.361-127.999 292.282z" fill="#cfad54"></path>
            <path fill="#df786c" d="M259.053 405.733L387.052 113.45l64.762 28.361-127.999 292.282z"></path>
          </g>
        </svg>
      </nuxt-link>
    </div>
    <div class="logo__type">
      <nuxt-link :to="localePath('index')">{{ $t('danes-je-nov-dan') }}</nuxt-link>
    </div>
    <nuxt-link
      v-for="locale in availableLocales"
      :key="locale.code"
      :to="switchLocalePath(locale.code)"
    >{{ locale.name }}</nuxt-link>
  </header>
</template>

<script>
export default {
  name: 'NavLogo',
  computed: {
    availableLocales() {
      return this.$i18n.locales.filter(i => i.code !== this.$i18n.locale);
    },
  },
};
</script>

<style lang="scss" scoped>
.logo {
  .logo__mark {
    width: 77px;
    height: 77px;
    margin-bottom: 2rem;
  }

  .logo__type {
    font-weight: 700;
    font-size: 37px;
    text-transform: uppercase;
    line-height: 0.95;
    color: $color-green;
    margin-bottom: 2rem;

    a {
      color: inherit;
      text-decoration: none;
    }
  }
}
</style>
