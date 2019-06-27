<template>
  <div class="clipping-filter">
    <div class="filters">
      <div class="icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="24 27 52 46" fill="currentColor">
          <path
            d="M38 39.4c-3.3 0-6-2.7-6-5.9 0-3.3 2.7-5.9 6-5.9s6 2.7 6 5.9-2.7 5.9-6 5.9zm0-8.9c-1.7 0-3 1.3-3 2.9 0 1.6 1.3 2.9 3 2.9s3-1.3 3-2.9c0-1.6-1.3-2.9-3-2.9z"
          ></path>
          <path
            d="M33.5 34.8H26c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5h7.5c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5zm40.5 0H42.5c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5H74c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5zm-9 21.1c-3.3 0-6-2.7-6-5.9 0-3.3 2.7-5.9 6-5.9s6 2.7 6 5.9c0 3.3-2.7 5.9-6 5.9zm0-8.8c-1.7 0-3 1.3-3 2.9 0 1.6 1.3 2.9 3 2.9s3-1.3 3-2.9c0-1.6-1.3-2.9-3-2.9z"
          ></path>
          <path
            d="M60.5 51.4H26c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5h34.5c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5zm13.5 0h-4.5c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5H74c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5zM45.9 72.5c-3.3 0-6-2.7-6-5.9s2.7-5.9 6-5.9 6 2.7 6 5.9-2.7 5.9-6 5.9zm0-8.8c-1.7 0-3 1.3-3 2.9s1.3 2.9 3 2.9 3-1.3 3-2.9-1.4-2.9-3-2.9z"
          ></path>
          <path
            d="M41.4 68H26c-.8 0-1.5-.7-1.5-1.5S25.2 65 26 65h15.4c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5zM74 68H50.4c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5H74c.8 0 1.5.7 1.5 1.5S74.8 68 74 68z"
          ></path>
        </svg>
      </div>
      <filter-checkboxes v-model="typeFilters" title="Tip gostovanja"/>
      <filter-checkboxes v-model="formatFilters" title="Format"/>
      <filter-checkboxes v-model="languageFilters" title="Jezik"/>
      <filter-checkboxes v-model="tagFilters" title="Oznake"/>
    </div>
    <div>{{ filteredApiUrl }}</div>
  </div>
</template>

<script>
import FilterCheckboxes from '~/components/FilterCheckboxes.vue';

export default {
  components: {
    FilterCheckboxes,
  },
  data() {
    return {
      typeFilters: [
        { id: 'interview', label: 'intervju', active: false },
        { id: 'report', label: 'poročanje', active: false },
        { id: 'talk', label: 'predavanje', active: false },
        { id: 'rt', label: 'okrogla miza', active: false },
        { id: 'column', label: 'kolumna', active: false },
      ],
      formatFilters: [
        { id: 'text', label: 'besedilo', active: false },
        { id: 'audio', label: 'avdio', active: false },
        { id: 'video', label: 'video', active: false },
      ],
      languageFilters: [
        { id: 'sl', label: 'slovenščina', active: false },
        { id: 'hr', label: 'hrvaščina', active: false },
        { id: 'en', label: 'angleščina', active: false },
      ],
      tagFilters: [
        { id: 'parlameter', label: 'Parlameter', active: false },
        { id: 'copyright', label: 'Avtorsko pravo', active: false },
        { id: 'tedx', label: 'TedX', active: false },
        { id: 'studiocity', label: 'Studio City', active: false },
      ],
    };
  },
  computed: {
    activeTypeFilters() {
      return this.typeFilters.filter(f => f.active).map(f => f.id);
    },
    activeFormatFilters() {
      return this.formatFilters.filter(f => f.active).map(f => f.id);
    },
    activeLanguageFilters() {
      return this.languageFilters.filter(f => f.active).map(f => f.id);
    },
    activeTagFilters() {
      return this.tagFilters.filter(f => f.active).map(f => f.id);
    },
    filteredApiUrl() {
      const query = {
        types: this.activeTypeFilters.map(encodeURIComponent).join(','),
        formats: this.activeFormatFilters.map(encodeURIComponent).join(','),
        languages: this.activeLanguageFilters.map(encodeURIComponent).join(','),
        tags: this.activeTagFilters.map(encodeURIComponent).join(','),
      };
      const qs = `?${Object.keys(query)
        .reduce((a, k) => {
          if (query[k]) {
            a.push(`${k}=${query[k]}`);
          }
          return a;
        }, [])
        .join('&')}`;
      return `https://djnapi.djnd.si/djnd.si/clips/${qs}`;
    },
  },
};
</script>

<style lang="scss" scoped>
.clipping-filter {
  background-color: #fff;
  padding: 1rem;

  @include media-breakpoint-up(md) {
    padding: 1.25rem;
  }

  .filters {
    display: flex;
    flex-direction: column;
    position: relative;

    @include media-breakpoint-up(md) {
      flex-direction: row;
    }

    .icon {
      width: 1.5rem;
      height: 1.5rem;
      display: flex;
      align-items: center;
      flex-shrink: 0;
      color: $color-yellow;
      position: absolute;
      left: 0;
      top: 0;

      @include media-breakpoint-up(md) {
        position: static;
      }

      svg {
        width: 100%;
        height: 100%;
      }
    }
  }
}
</style>
