<template>
  <div>
    <page-title
      :title="$t('menu.projects')"
      :text="$t('projects.description')"
      color="secondary"
    />
    <filter-bar v-model="filters" everything-id="all" color="secondary" />
    <div v-if="projects && projects.length" class="wrapping-flex-tiles">
      <div
        v-for="project in filteredProjects"
        :key="`${project.url}`"
        class="flex-tile"
      >
        <project-tile
          :image="project.image"
          :title="project.title"
          :byline="toMonthYear(project.date)"
          :text="project.desc"
          :url="project.url"
        />
      </div>
      <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile" />
    </div>
  </div>
</template>

<script>
import { intersection } from 'lodash';
import PageTitle from '~/components/PageTitle.vue';
import FilterBar from '~/components/FilterBar.vue';
import ProjectTile from '~/components/ProjectTile.vue';
import dateMixin from '~/mixins/date.js';

export default {
  pageColor: 'secondary',
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
  mixins: [dateMixin],
  data() {
    return {
      filters: [
        {
          id: 'pravičnost',
          label: this.$t('projects.tags.pravičnost'),
          active: false,
        },
        { id: 'okolje', label: this.$t('projects.tags.okolje'), active: false },
        {
          id: 'demokracija',
          label: this.$t('projects.tags.demokracija'),
          active: false,
        },
        {
          id: 'internet',
          label: this.$t('projects.tags.internet'),
          active: false,
        },
        {
          id: 'sodelovanje',
          label: this.$t('projects.tags.sodelovanje'),
          active: false,
        },
        {
          id: 'peticija',
          label: this.$t('projects.tags.peticija'),
          active: false,
        },
        {
          id: 'kampanja',
          label: this.$t('projects.tags.kampanja'),
          active: false,
        },
        {
          id: 'dogodek',
          label: this.$t('projects.tags.dogodek'),
          active: false,
        },
        { id: 'branje', label: this.$t('projects.tags.branje'), active: false },
        // { id: 'igra', label: this.$t('projects.tags.igra'), active: false },
        // { id: 'knjiga', label: this.$t('projects.tags.knjiga'), active: false },
      ],
    };
  },
  computed: {
    activeFilters() {
      return this.filters.filter((f) => f.active).map((f) => f.id);
    },
    filteredProjects() {
      if (
        !this.activeFilters.length ||
        (this.activeFilters.length === 1 && this.activeFilters[0] === 'all')
      ) {
        return this.projects;
      }
      return this.projects.filter(
        (proj) =>
          proj.tags && intersection(proj.tags, this.activeFilters).length,
      );
    },
  },
  async asyncData({ $axios, params, error }) {
    const projectsResponse = await $axios.$get(
      'https://djnapi.djnd.si/djnd.si/projects/?ordering=-date&size=500',
    );
    return {
      projects: projectsResponse.results,
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
  @include wrapping-flex-tiles($width: 300px, $width-xl: 345px);
}
</style>
