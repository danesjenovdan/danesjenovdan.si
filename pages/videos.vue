<template>
  <div>
    <page-title :title="$t('menu.videos')" :text="$t('videos.description')" color="warning"/>
    <div class="big-video-container d-none d-lg-block">
      <div class="embed-responsive embed-responsive-16by9">
        <div class="embed-responsive-item">
          <iframe
            src="https://www.youtube.com/embed/yilFJTdo8u0"
            frameborder="0"
            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
          />
        </div>
      </div>
      VIDEO TITLE
      <div class="row my-3"/>
    </div>
    <filter-bar :items="filters"/>
    <div class="row my-3"/>
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';
import FilterBar from '~/components/FilterBar.vue';

export default {
  nuxtI18n: {
    paths: {
      sl: '/videogalerija',
      en: '/videos',
    },
  },
  components: {
    PageTitle,
    FilterBar,
  },
  data() {
    return {
      filters: [
        { key: 'all', label: 'Vsi', active: true },
        { key: 'tmp1', label: 'Lolz', active: false },
        { key: 'tmp2', label: 'Whatever', active: false },
      ],
    };
  },
  head() {
    return {
      title: this.$t('menu.videos'),
    };
  },
};
</script>

<style lang="scss" scoped>
</style>
