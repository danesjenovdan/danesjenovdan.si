<template>
  <div>
    <page-title :title="$t('menu.clipping')" :text="$t('clipping.description')" color="warning"/>
    <clipping-filter/>
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';
import ClippingFilter from '~/components/ClippingFilter.vue';

export default {
  pageColor: 'warning',
  nuxtI18n: {
    paths: {
      sl: '/pojavljanja',
      en: '/clipping',
    },
  },
  components: {
    PageTitle,
    ClippingFilter,
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
