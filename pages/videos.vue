<template>
  <div>
    <page-title
      :title="$t('menu.videos')"
      :text="$t('videos.description')"
      color="warning"
    />
    <div ref="bigVideo" class="big-video">
      <div class="embed-responsive embed-responsive-16by9">
        <div
          :style="{ 'background-image': `url(${bigVideo.image})` }"
          class="embed-responsive-item background-image"
        />
        <div v-if="bigVideo" class="embed-responsive-item">
          <iframe
            :src="embedUrl(bigVideo.url, autoplay)"
            :class="['big-video__iframe', { loaded: iframeLoaded }]"
            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
            @load="onIframeLoad"
          />
        </div>
      </div>
      <div class="row big-video__info">
        <div class="col-12 col-lg-5">
          <div class="big-video__title-col">
            <h2 v-text="bigVideo.title" />
            <div v-if="bigVideo.date" class="big-video__byline">
              <i v-text="toSloDate(bigVideo.date)" />
            </div>
          </div>
        </div>
        <div class="col-12 col-lg-7">
          <div class="big-video__text-col">
            <div v-if="bigVideo.desc" class="big-video__text">
              <p v-text="bigVideo.desc" />
            </div>
          </div>
        </div>
      </div>
    </div>
    <filter-bar v-model="filters" everything-id="all" color="warning" />
    <div v-if="videos && videos.length" class="wrapping-flex-tiles">
      <div
        v-for="video in filteredVideos"
        :key="`${video.url}`"
        class="flex-tile"
      >
        <preview-tile
          :image="video.image"
          :title="video.title"
          :byline="toSloDate(video.date)"
          :url="localePath({ name: 'videos', query: { video: video.url } })"
          color="warning"
        />
      </div>
      <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile" />
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
  async asyncData({ $axios, params, query, error }) {
    const videoRes = await $axios.$get(
      'https://djnapi.djnd.si/djnd.si/videos/?ordering=-date&size=500',
    );
    const videoObj = videoRes.results.find((v) => v.url === query.video);
    return {
      bigVideo: videoObj || (videoRes.results.length && videoRes.results[0]),
      videos: videoRes.results,
    };
  },
  data() {
    return {
      iframeLoaded: false,
      filters: [
        { id: 'all', label: 'Vsi', active: true },
        { id: 'dogodek', label: 'Dogodek', active: false },
        { id: 'inspiracija', label: 'Inspiracija', active: false },
        { id: 'provokacija', label: 'Provokacija', active: false },
        { id: 'razlaga', label: 'Razlaga', active: false },
        // TODO: i18n labels
      ],
      autoplay: false,
    };
  },
  computed: {
    activeFilters() {
      return this.filters.filter((f) => f.active).map((f) => f.id);
    },
    filteredVideos() {
      if (
        !this.activeFilters.length ||
        (this.activeFilters.length === 1 && this.activeFilters[0] === 'all')
      ) {
        return this.videos;
      }
      return this.videos.filter(
        (video) =>
          video.tags && intersection(video.tags, this.activeFilters).length,
      );
    },
  },
  watch: {
    '$route.query'() {
      const videoObj = this.videos.find(
        (v) => v.url === this.$route.query.video,
      );
      this.bigVideo = videoObj || (this.videos.length && this.videos[0]);
      this.iframeLoaded = false;
      this.$refs.bigVideo.scrollIntoView();
      this.autoplay = true;
    },
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
.big-video {
  .embed-responsive {
    @include media-breakpoint-up(lg) {
      width: 75%;
      margin: 0 auto;
    }

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
  }

  .big-video__info {
    margin-bottom: 2rem;

    @include media-breakpoint-up(lg) {
      margin-top: 1rem;
    }

    .big-video__title-col {
      background-color: #fff;
      padding: 1.25rem 1rem;

      @include media-breakpoint-up(lg) {
        background-color: transparent;
        margin-top: 1rem;
        float: right;
        min-width: 400px;
      }

      h2 {
        font-size: 1.85rem;
        font-weight: 600;

        @include media-breakpoint-up(lg) {
          font-size: 3rem;
        }
      }
    }

    .big-video__text-col {
      background-color: #fff;
      padding: 0 1rem 1rem;
      position: relative;
      z-index: -1;

      @include media-breakpoint-up(lg) {
        $overlap: 15rem;
        padding: 2rem 2.5rem;
        margin-left: -$overlap;
        padding-left: $overlap;
      }

      p {
        font-size: 1.15rem;
        font-weight: 200;
        margin: 0;
      }
    }
  }
}

.wrapping-flex-tiles {
  @include wrapping-flex-tiles($width: 300px, $width-xl: 345px);
}
</style>
