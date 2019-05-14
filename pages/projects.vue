<template>
  <div>
    <page-title
      :title="$t('menu.projects')"
      :text="$t('projects.description')"
      color="secondary"
    />
    <filter-bar :items="filters"/>
    <div class="wrapping-flex-tiles">
      <div class="flex-tile">
        <project-tile/>
      </div>
      <div class="flex-tile">
        <project-tile/>
      </div>
      <div class="flex-tile">
        <project-tile/>
      </div>
      <div class="flex-tile">
        <project-tile/>
      </div>
      <div class="flex-tile">
        <project-tile/>
      </div>
      <div class="flex-tile"/>
      <div class="flex-tile"/>
      <div class="flex-tile"/>
      <div class="flex-tile"/>
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
      en: '/projects',
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
      title: this.$t('menu.projects'),
    };
  },
};
</script>

<style lang="scss" scoped>
.wrapping-flex-tiles {
  @include wrapping-flex-tiles($width: 320px);
}
</style>
