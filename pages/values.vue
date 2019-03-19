<template>
  <div>
    <page-title :title="$t('menu.values')" :text="$t('values.description')" color="warning"/>
    <div class="row">
      <div class="col-12">
        <value-tile/>
      </div>
      <div class="col-12">
        <value-tile/>
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';
import ValueTile from '~/components/ValueTile.vue';

export default {
  nuxtI18n: {
    paths: {
      sl: '/vrednote',
      en: '/values',
    },
  },
  components: {
    PageTitle,
    ValueTile,
  },
  head() {
    return {
      title: this.$t('menu.values'),
    };
  },
};
</script>

<style lang="scss" scoped>
</style>
