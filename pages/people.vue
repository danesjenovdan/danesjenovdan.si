<template>
  <div>
    <page-title
      :title="$t('menu.people')"
      :text="$t('people.description')"
      color="secondary"
    />
    <filter-bar :items="filters"/>
    <div class="wrapping-flex-tiles">
      <div class="flex-tile">
        <person-tile/>
      </div>
      <div class="flex-tile">
        <person-tile/>
      </div>
      <div class="flex-tile">
        <person-tile/>
      </div>
      <div class="flex-tile">
        <person-tile/>
      </div>
      <div class="flex-tile">
        <person-tile/>
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
.wrapping-flex-tiles {
  @include wrapping-flex-tiles($width: 260px);
}
</style>
