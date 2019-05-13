<template>
  <div>
    <page-title
      :title="$t('menu.people')"
      :text="$t('people.description')"
      color="secondary"
    />
    <filter-bar :items="filters"/>
    <div class="grid-container mt-4">
      <div class="grid-item">
        <person-tile/>
      </div>
      <div class="grid-item">
        <person-tile/>
      </div>
      <div class="grid-item">
        <person-tile/>
      </div>
      <div class="grid-item">
        <person-tile/>
      </div>
      <div class="grid-item">
        <person-tile/>
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';
import FilterBar from '~/components/FilterBar.vue';
import PersonTile from '~/components/PersonTile.vue';

export default {
  nuxtI18n: {
    paths: {
      sl: '/posadka',
      en: '/people',
    },
  },
  components: {
    PageTitle,
    FilterBar,
    PersonTile,
  },
  data() {
    return {
      filters: [
        { key: 'all', label: 'Vsi', active: true },
        { key: 'council', label: 'Svet zavoda', active: false },
        { key: 'science', label: 'Znanstveni svet zavoda', active: false },
      ],
    };
  },
  head() {
    return {
      title: this.$t('menu.people'),
    };
  },
};
</script>

<style lang="scss" scoped>
.grid-container {
  display: grid;
  grid-gap: 1.75rem;

  @include media-breakpoint-up(sm) {
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  }
}
</style>
