<template>
  <div>
    <page-title :title="$t('menu.clipping')" :text="$t('clipping.description')" color="warning"/>
    <clipping-filter :filters="filters" @qs-change="onQueryChange"/>
    <div v-if="loading">
      <div class="loader-container text-center pt-5">
        <div class="lds-dual-ring"/>
      </div>
    </div>
    <div v-else>
      <div v-for="clip of clips" :key="clip.order">{{ clip }}</div>
    </div>
  </div>
</template>

<script>
import { CancelToken, isCancel } from 'axios';
import PageTitle from '~/components/PageTitle.vue';
import ClippingFilter from '~/components/ClippingFilter.vue';

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
  },
  data() {
    return {
      loading: false,
      cancelSource: null,
    };
  },
  async asyncData({ $axios }) {
    const endpoint = 'https://djnapi.djnd.si/djnd.si/clips/';
    const queryString = '';
    const clips = await $axios.$get(`${endpoint}${queryString}`);
    return {
      endpoint,
      queryString,
      clips: clips.results,
      filters: clips.filters,
    };
  },
  methods: {
    onQueryChange(newQuery) {
      if (this.queryString !== newQuery) {
        this.queryString = newQuery;
        this.fetchClips();
      }
    },
    async fetchClips() {
      this.loading = true;
      try {
        if (this.cancelSource) {
          this.cancelSource.cancel();
        }
        this.cancelSource = CancelToken.source();
        const clips = await this.$axios.$get(`${this.endpoint}${this.queryString}`, {
          cancelToken: this.cancelSource.token,
        });
        this.clips = clips.results;
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

<style lang="scss" scoped>
</style>
