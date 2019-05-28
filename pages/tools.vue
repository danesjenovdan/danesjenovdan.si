<template>
  <div>
    <page-title :title="$t('menu.tools')" :text="$t('tools.description')" color="warning"/>
    <div class="row">
      <div class="col-12">
        <tool-tile/>
      </div>
      <div class="col-12">
        <tool-tile/>
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';
import ToolTile from '~/components/ToolTile.vue';

export default {
  pageColor: 'warning',
  nuxtI18n: {
    paths: {
      sl: '/orodja',
      en: '/tools',
    },
  },
  components: {
    PageTitle,
    ToolTile,
  },
  data() {
    return {
      filters: [
        { key: 'okolje', label: 'Okolje', active: false },
        { key: 'pravice', label: 'Človekove pravice', active: true },
        { key: 'demokracija', label: 'Demokracija', active: false },
        { key: 'lulz', label: 'For the lulz', active: false },
      ],
    };
  },
  head() {
    return {
      title: this.$t('menu.tools'),
    };
  },
};
</script>

<style lang="scss" scoped>
</style>
