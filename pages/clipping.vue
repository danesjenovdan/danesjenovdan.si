<template>
  <div>
    <page-title :title="$t('menu.clipping')" :text="$t('clipping.description')" color="warning"/>
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';

export default {
  nuxtI18n: {
    paths: {
      sl: '/pojavljanja',
      en: '/clipping',
    },
  },
  components: {
    PageTitle,
  },
  data() {
    return {};
  },
  head() {
    return {
      title: this.$t('menu.clipping'),
    };
  },
};
</script>

<style lang="scss" scoped>
</style>
