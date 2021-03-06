<template>
  <div class="clipping-filter">
    <div class="filters">
      <div class="icon">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="24 27 52 46"
          fill="currentColor"
        >
          <path
            d="M38 39.4c-3.3 0-6-2.7-6-5.9 0-3.3 2.7-5.9 6-5.9s6 2.7 6 5.9-2.7 5.9-6 5.9zm0-8.9c-1.7 0-3 1.3-3 2.9 0 1.6 1.3 2.9 3 2.9s3-1.3 3-2.9c0-1.6-1.3-2.9-3-2.9z"
          />
          <path
            d="M33.5 34.8H26c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5h7.5c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5zm40.5 0H42.5c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5H74c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5zm-9 21.1c-3.3 0-6-2.7-6-5.9 0-3.3 2.7-5.9 6-5.9s6 2.7 6 5.9c0 3.3-2.7 5.9-6 5.9zm0-8.8c-1.7 0-3 1.3-3 2.9 0 1.6 1.3 2.9 3 2.9s3-1.3 3-2.9c0-1.6-1.3-2.9-3-2.9z"
          />
          <path
            d="M60.5 51.4H26c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5h34.5c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5zm13.5 0h-4.5c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5H74c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5zM45.9 72.5c-3.3 0-6-2.7-6-5.9s2.7-5.9 6-5.9 6 2.7 6 5.9-2.7 5.9-6 5.9zm0-8.8c-1.7 0-3 1.3-3 2.9s1.3 2.9 3 2.9 3-1.3 3-2.9-1.4-2.9-3-2.9z"
          />
          <path
            d="M41.4 68H26c-.8 0-1.5-.7-1.5-1.5S25.2 65 26 65h15.4c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5zM74 68H50.4c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5H74c.8 0 1.5.7 1.5 1.5S74.8 68 74 68z"
          />
        </svg>
      </div>
      <filter-checkboxes
        v-model="typeFilters"
        :title="$t('clipping.tags.type.title')"
      />
      <filter-checkboxes
        v-model="formatFilters"
        :title="$t('clipping.tags.format.title')"
      />
      <filter-checkboxes
        v-model="languageFilters"
        :title="$t('clipping.tags.language.title')"
      />
    </div>
  </div>
</template>

<script>
import stable from 'stable';
import FilterCheckboxes from '~/components/FilterCheckboxes.vue';

export default {
  components: {
    FilterCheckboxes,
  },
  props: {
    filters: {
      type: Object,
      required: true,
    },
  },
  data() {
    const comparator = (a, b) => a.label.localeCompare(b.label, 'sl');

    const typeFilters = stable(
      (this.filters.types || []).map((tagName) => ({
        id: tagName,
        label: this.$te(`clipping.tags.type.${tagName}`)
          ? this.$t(`clipping.tags.type.${tagName}`)
          : tagName,
        active: false,
      })),
      comparator,
    );

    const formatFilters = stable(
      (this.filters.formats || []).map((tagName) => ({
        id: tagName,
        label: this.$te(`clipping.tags.format.${tagName}`)
          ? this.$t(`clipping.tags.format.${tagName}`)
          : tagName,
        active: false,
      })),
      comparator,
    );

    const languageFilters = stable(
      (this.filters.languages || []).map((tagName) => ({
        id: tagName,
        label: this.$te(`clipping.tags.language.${tagName}`)
          ? this.$t(`clipping.tags.language.${tagName}`)
          : tagName,
        active: false,
      })),
      comparator,
    );

    const tagFilters = stable(
      (this.filters.tags || []).map((tagName) => ({
        id: tagName,
        label: this.$te(`clipping.tags.tag.${tagName}`)
          ? this.$t(`clipping.tags.tag.${tagName}`)
          : tagName,
        active: false,
      })),
      comparator,
    );

    return {
      typeFilters,
      formatFilters,
      languageFilters,
      tagFilters,
    };
  },
  computed: {
    activeTypeFilters() {
      return this.typeFilters.filter((f) => f.active).map((f) => f.id);
    },
    activeFormatFilters() {
      return this.formatFilters.filter((f) => f.active).map((f) => f.id);
    },
    activeLanguageFilters() {
      return this.languageFilters.filter((f) => f.active).map((f) => f.id);
    },
    activeTagFilters() {
      return this.tagFilters.filter((f) => f.active).map((f) => f.id);
    },
    queryString() {
      const query = {
        types: this.activeTypeFilters.map(encodeURIComponent).join(','),
        formats: this.activeFormatFilters.map(encodeURIComponent).join(','),
        languages: this.activeLanguageFilters.map(encodeURIComponent).join(','),
        tags: this.activeTagFilters.map(encodeURIComponent).join(','),
      };
      return `${Object.keys(query)
        .reduce((a, k) => {
          if (query[k]) {
            a.push(`${k}=${query[k]}`);
          }
          return a;
        }, [])
        .join('&')}`;
    },
  },
  watch: {
    queryString(newQS) {
      this.$emit('qs-change', newQS);
    },
  },
  created() {
    this.$emit('qs-change', this.queryString);
  },
};
</script>

<style lang="scss" scoped>
.clipping-filter {
  background-color: #fff;
  padding: 1rem;
  padding-bottom: 0.25rem;

  @include media-breakpoint-up(md) {
    padding: 1.25rem;
    padding-bottom: 0.25rem;
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
