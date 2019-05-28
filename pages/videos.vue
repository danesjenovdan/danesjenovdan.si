<template>
  <div>
    <page-title :title="$t('menu.videos')" :text="$t('videos.description')" color="warning"/>
    <div ref="bigVideo" class="big-video-container d-none d-lg-block">
      <div class="embed-responsive embed-responsive-16by9">
        <div
          class="embed-responsive-item background-image"
          :style="{'background-image': `url(${bigVideo.image})`}"
        />
        <div v-if="bigVideo" class="embed-responsive-item">
          <iframe
            :src="embedUrl(bigVideo.url)"
            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
            :class="{ loaded: iframeLoaded }"
            @load="onIframeLoad"
          />
        </div>
      </div>
      VIDEO TITLE {{ bigVideo }}
      <div class="row my-3"/>
    </div>
    <filter-bar v-model="filters" everything-id="all"/>
    <div v-if="videos && videos.length" class="wrapping-flex-tiles">
      <div v-for="video in filteredVideos" :key="`${video.url}`" class="flex-tile">
        <preview-tile
          color="warning"
          :image="video.image"
          :title="video.title"
          :byline="toSloDate(video.date)"
          :url="localePath({ name: 'videos', query: { video: video.url } })"
        />
      </div>
      <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile"/>
    </div>
  </div>
</template>

<script>
import { intersection } from 'lodash';
import PageTitle from '~/components/PageTitle.vue';
import PreviewTile from '~/components/PreviewTile.vue';
import FilterBar from '~/components/FilterBar.vue';
import dateMixin from '~/mixins/date.js';
import videoMixin from '~/mixins/video.js';

export default {
  pageColor: 'warning',
  nuxtI18n: {
    paths: {
      sl: '/videogalerija',
      en: '/videos',
    },
  },
  components: {
    PageTitle,
    PreviewTile,
    FilterBar,
  },
  mixins: [dateMixin, videoMixin],
  data() {
    return {
      iframeLoaded: false,
      filters: [
        { id: 'all', label: 'Vsi', active: true },
        { id: 'tmp1', label: 'Lolz', active: false },
        { id: 'tmp2', label: 'Whatever', active: false },
        // TODO: actual video filters
      ],
    };
  },
  computed: {
    activeFilters() {
      return this.filters.filter(f => f.active).map(f => f.id);
    },
    filteredVideos() {
      if (
        !this.activeFilters.length ||
        (this.activeFilters.length === 1 && this.activeFilters[0] === 'all')
      ) {
        return this.videos;
      }
      return this.videos.filter(
        video => video.tags && intersection(video.tags, this.activeFilters).length,
      );
    },
  },
  watch: {
    '$route.query'() {
      const videoObj = this.videos.find(v => v.url === this.$route.query.video);
      this.bigVideo = videoObj || (this.videos.length && this.videos[0]);
      this.iframeLoaded = false;
      this.$refs.bigVideo.scrollIntoView();
    },
  },
  async asyncData({ $axios, params, query, error }) {
    const videoRes = await $axios.$get(
      'https://djnapi.djnd.si/djnd.si/videos/?ordering=-date&size=500',
    );
    const videoObj = videoRes.results.find(v => v.url === query.video);
    return {
      bigVideo: videoObj || (videoRes.results.length && videoRes.results[0]),
      videos: videoRes.results,
    };
  },
  methods: {
    onIframeLoad() {
      this.iframeLoaded = true;
    },
  },
  head() {
    return {
      title: this.$t('menu.videos'),
    };
  },
};
</script>

<style lang="scss" scoped>
.background-image {
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

iframe {
  opacity: 0;

  &.loaded {
    opacity: 1;
  }
}

.wrapping-flex-tiles {
  @include wrapping-flex-tiles($width: 300px, $width-xl: 345px);
}
</style>
