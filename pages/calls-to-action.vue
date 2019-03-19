<template>
  <div>
    <page-title
      :title="$t('menu.calls-to-action')"
      :text="$t('calls-to-action.description')"
      color="secondary"
    />
    <filter-bar :items="filters"/>
    <div class="row mt-4">
      <div class="col-12 col-md-4">
        <project-tile/>
      </div>
      <div class="col-12 col-md-4">
        <project-tile/>
      </div>
      <div class="col-12 col-md-4">
        <project-tile/>
      </div>
      <div class="col-12 col-md-4">
        <project-tile/>
      </div>
      <div class="col-12 col-md-4">
        <project-tile/>
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';
import FilterBar from '~/components/FilterBar.vue';
import ProjectTile from '~/components/ProjectTile.vue';

export default {
  nuxtI18n: {
    paths: {
      sl: '/pozivi',
      en: '/calls-to-action',
    },
  },
  components: {
    PageTitle,
    FilterBar,
    ProjectTile,
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
      title: this.$t('menu.calls-to-action'),
    };
  },
};
</script>

<style>
</style>
