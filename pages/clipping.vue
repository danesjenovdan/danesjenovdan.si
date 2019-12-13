<template>
  <div>
    <page-title
      :title="$t('menu.clipping')"
      :text="$t('clipping.description')"
      color="warning"
    />
    <clipping-filter :filters="filters" @qs-change="onQueryChange" />
    <div v-if="loading">
      <div class="loader-container text-center pt-5">
        <div class="lds-dual-ring" />
      </div>
    </div>
    <div v-else class="mt-4 mt-xl-5">
      <clip-tile v-for="clip of clips" :key="clip.order" :clip="clip" />
      <pagination
        v-if="count > perPage"
        :page="page"
        :count="count"
        :per-page="perPage"
        @change="onPageChange"
      />
    </div>
  </div>
</template>

<script>
import { CancelToken, isCancel } from 'axios';
import PageTitle from '~/components/PageTitle.vue';
import ClippingFilter from '~/components/ClippingFilter.vue';
import ClipTile from '~/components/ClipTile.vue';
import Pagination from '~/components/Pagination.vue';

const PAGE_SIZE = 10;
const INITIAL_PAGE = 1;

export default {
  pageColor: 'warning',
  nuxtI18n: {
    paths: {
      sl: '/pojavljanja',
      en: '/clipping',
    },
  },
  components: {
    PageTitle,
    ClippingFilter,
    ClipTile,
    Pagination,
  },
  data() {
    return {
      loading: false,
      cancelSource: null,
    };
  },
  computed: {
    queryString() {
      return `?${[this.filterQuery, this.pageQuery].join('&')}&ordering=-date`;
    },
  },
  async asyncData({ $axios }) {
    const endpoint = 'https://djnapi.djnd.si/djnd.si/clips/';
    const filterQuery = '';
    const pageQuery = `page=${INITIAL_PAGE}&size=${PAGE_SIZE}`;
    const clips = await $axios.$get(
      `${endpoint}?${[filterQuery, pageQuery].join('&')}&ordering=-date`,
    );
    return {
      endpoint,
      filterQuery,
      pageQuery,
      filters: clips.filters,
      clips: clips.results,
      count: clips.count,
      page: 1,
      perPage: PAGE_SIZE,
    };
  },
  methods: {
    onQueryChange(newQuery) {
      if (this.filterQuery !== newQuery) {
        this.filterQuery = newQuery;
        this.onPageChange(1);
      }
    },
    onPageChange(newPage) {
      this.page = newPage;
      this.pageQuery = `page=${newPage}&size=${this.perPage}`;
      this.fetchClips();
    },
    async fetchClips() {
      this.loading = true;
      try {
        if (this.cancelSource) {
          this.cancelSource.cancel();
        }
        this.cancelSource = CancelToken.source();
        const clips = await this.$axios.$get(
          `${this.endpoint}${this.queryString}`,
          {
            cancelToken: this.cancelSource.token,
          },
        );
        this.clips = clips.results;
        this.count = clips.count;
      } catch (error) {
        if (!isCancel(error)) {
          // eslint-disable-next-line no-console
          console.error(error);
          this.error = error.message;
        }
      }
      this.cancelSource = null;
      this.loading = false;
    },
  },
  head() {
    return {
      title: this.$t('menu.clipping'),
    };
  },
};
</script>

<style lang="scss" scoped></style>
