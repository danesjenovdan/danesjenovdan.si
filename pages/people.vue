<template>
  <div>
    <page-title
      :title="$t('menu.people')"
      :text="$t('people.description')"
      color="secondary"
    />
    <filter-bar v-model="filters" single color="secondary" />
    <div class="wrapping-flex-tiles">
      <div v-for="person in filteredPeople" :key="person.id" class="flex-tile">
        <person-tile :person="person" />
      </div>
      <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile" />
    </div>
    <volunteer />
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';
import FilterBar from '~/components/FilterBar.vue';
import PersonTile from '~/components/PersonTile.vue';
import Volunteer from '~/components/Volunteer.vue';
import peopleJson from '~/assets/people.json';

export default {
  pageColor: 'secondary',
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
    Volunteer,
  },
  data() {
    const sortedPeople = [...peopleJson.people].sort((a, b) => {
      const lastA = a.name.slice(a.name.lastIndexOf(' ') + 1);
      const lastB = b.name.slice(b.name.lastIndexOf(' ') + 1);
      return lastA.toLowerCase().localeCompare(lastB.toLowerCase(), 'sl');
    });
    return {
      filters: [
        { id: 'all', label: this.$t('people.tags.all'), active: true },
        { id: 'council', label: this.$t('people.tags.council'), active: false },
        { id: 'science', label: this.$t('people.tags.science'), active: false },
      ],
      people: sortedPeople,
    };
  },
  head() {
    return {
      title: this.$t('menu.people'),
    };
  },
  computed: {
    activeFilter() {
      return this.filters.filter((f) => f.active).map((f) => f.id)[0];
    },
    filteredPeople() {
      if (!this.activeFilter || this.activeFilter === 'all') {
        return this.people;
      }
      return this.people.filter(
        (person) => person.tags && person.tags.includes(this.activeFilter),
      );
    },
  },
};
</script>

<style lang="scss" scoped>
.wrapping-flex-tiles {
  @include wrapping-flex-tiles($width: 260px);
}
</style>
