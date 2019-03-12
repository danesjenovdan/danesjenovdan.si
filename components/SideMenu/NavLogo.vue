<template>
  <header class="logo">
    <div class="logo__mark">
      <nuxt-link :to="localePath('index')">
        <img src="~/static/img/logo-circle.png" alt="djnd logo mark" class="img-fluid">
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
@import '~/assets/scss/_variables.scss';

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
