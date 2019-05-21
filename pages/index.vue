<template>
  <div>
    <page-title :title="$t('hello')" :text="$t('landing.description')"/>
    <div class="row">
      <div class="col-12">
        <section-header :text="$t('menu.agrument')" icon="keyboard"/>
      </div>
    </div>
    <div v-if="agrumentPosts && agrumentPosts.length" class="mt-4">
      <promoted-tile
        :image="agrumentPosts[0].image_url"
        :title="agrumentPosts[0].title"
        :byline="toSloDate(agrumentPosts[0].datetime)"
        :text="agrumentPosts[0].description"
        :url="agrumentPosts[0].url"
      />
      <div class="wrapping-flex-tiles">
        <div
          v-for="agrumentPost in agrumentPosts.slice(1)"
          :key="`${agrumentPost.id}`"
          class="flex-tile"
        >
          <preview-tile
            :image="agrumentPost.image_url"
            :title="agrumentPost.title"
            :byline="toSloDate(agrumentPost.datetime)"
            :text="agrumentPost.description"
            :url="agrumentPost.url"
          />
        </div>
        <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile"/>
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <more-button :to="localePath('agrument')" :text="$t('agrument.more')"/>
    </div>
    <div class="row mobile-no-gap">
      <div class="col-12 my-5">
        <agrument-subscribe-bar/>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <section-header :text="$t('menu.clipping')" icon="keyboard"/>
      </div>
    </div>
    <div>
      <div v-if="clippings && clippings.length" class="wrapping-flex-tiles">
        <div v-for="clip in clippings.slice(0, 4)" :key="`${clip.order}`" class="flex-tile">
          <preview-tile
            :image="clip.image"
            :title="clip.title"
            :byline="`${clip.publisher}, ${toSloDate(clip.date)}`"
            :url="clip.url"
          />
        </div>
        <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile"/>
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <more-button :to="localePath('clipping')" :text="$t('clipping.more')"/>
    </div>
    <div class="row">
      <div class="col-12">
        <section-header :text="$t('menu.projects')" color="secondary" icon="keyboard"/>
      </div>
    </div>
    <div>
      <div v-if="projects && projects.length" class="wrapping-flex-tiles">
        <div v-for="project in projects.slice(0, 4)" :key="`${project.order}`" class="flex-tile">
          <project-tile
            :image="project.image"
            :title="project.title"
            :byline="toSloDate(project.date)"
            :text="project.desc"
            :url="project.url"
          />
        </div>
        <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile"/>
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <more-button :to="localePath('projects')" :text="$t('projects.more')" color="secondary"/>
    </div>
    <div class="row mobile-no-gap">
      <div class="col-12 my-5">
        <social-media-bar
          color="secondary"
          :text="$t('projects.social-bar.follow-us')"
          :icons="[
            { icon: 'facebook', url: 'https://facebook.com/danesjenovdan' },
            { icon: 'twitter', url: 'https://twitter.com/danesjenovdan' },
          ]"
        />
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <section-header :text="$t('menu.videos')" color="warning" icon="keyboard"/>
      </div>
    </div>
    <div v-if="videos && videos.length" class="mt-4">
      <promoted-tile
        color="warning"
        :image="videos[0].image"
        :title="videos[0].title"
        :byline="toSloDate(videos[0].date)"
        :text="videos[0].desc"
        :url="videos[0].url"
      />
      <div class="wrapping-flex-tiles">
        <div v-for="video in videos.slice(1, 5)" :key="`${video.order}`" class="flex-tile">
          <preview-tile
            color="warning"
            :image="video.image"
            :title="video.title"
            :byline="toSloDate(video.date)"
            :text="video.desc"
            :url="video.url"
          />
        </div>
        <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile"/>
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <more-button :to="localePath('videos')" :text="$t('videos.more')" color="warning"/>
    </div>
    <div class="row mobile-no-gap">
      <div class="col-12 my-5">
        <social-media-bar
          color="warning"
          :text="$t('videos.social-bar.follow-us')"
          :icons="[
            { icon: 'youtube', url: 'https://youtube.com/danesjenovdan' },
            { icon: 'vimeo', url: 'https://vimeo.com/danesjenovdan' },
          ]"
        />
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <section-header :text="$t('menu.tools')" color="warning" icon="keyboard"/>
      </div>
    </div>
    <div>
      <div class="wrapping-flex-tiles">
        <div class="flex-tile">
          <tool-preview-tile
            icon="tool-parlameter"
            :title="$t('tools.parlameter.title')"
            :text="$t('tools.parlameter.short_description')"
          />
        </div>
        <div class="flex-tile">
          <tool-preview-tile
            icon="tool-commentality"
            :title="$t('tools.commentality.title')"
            :text="$t('tools.commentality.short_description')"
          />
        </div>
        <div class="flex-tile">
          <tool-preview-tile
            icon="tool-consul"
            :title="$t('tools.consul.title')"
            :text="$t('tools.consul.short_description')"
          />
        </div>
        <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile"/>
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <more-button :to="localePath('tools')" :text="$t('tools.more')" color="warning"/>
    </div>
    <div class="row mobile-no-gap">
      <div class="col-12 my-5">
        <shop-bar/>
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';
import SectionHeader from '~/components/SectionHeader.vue';
import ProjectTile from '~/components/ProjectTile.vue';
import PromotedTile from '~/components/PromotedTile.vue';
import PreviewTile from '~/components/PreviewTile.vue';
import ToolPreviewTile from '~/components/ToolPreviewTile.vue';
import MoreButton from '~/components/MoreButton.vue';
import AgrumentSubscribeBar from '~/components/AgrumentSubscribeBar.vue';
import SocialMediaBar from '~/components/SocialMediaBar.vue';
import ShopBar from '~/components/ShopBar.vue';

export default {
  components: {
    PageTitle,
    SectionHeader,
    ProjectTile,
    PromotedTile,
    PreviewTile,
    ToolPreviewTile,
    MoreButton,
    AgrumentSubscribeBar,
    SocialMediaBar,
    ShopBar,
  },
  async asyncData({ $axios, params, error }) {
    // TODO: infopush
    const [
      agrumentResponse,
      clippingsResponse,
      projectsResponse,
      videosResponse,
    ] = await Promise.all([
      $axios.$get('https://agrument.danesjenovdan.si/api/v2/posts?limit=5'),
      $axios.$get('https://djnapi.djnd.si/djnd.si/clips/'),
      $axios.$get('https://djnapi.djnd.si/djnd.si/projects/'),
      $axios.$get('https://djnapi.djnd.si/djnd.si/videos/'),
    ]);
    const agrumentPosts = agrumentResponse.data;
    const clippings = clippingsResponse.results;
    const projects = projectsResponse.results;
    const videos = videosResponse.results;
    return {
      agrumentPosts,
      clippings,
      projects,
      videos,
    };
  },
  methods: {
    toSloDate(isoTime) {
      return String(isoTime)
        .split('T')[0]
        .split('-')
        .reverse()
        .join('. ');
    },
  },
};
</script>

<style lang="scss" scoped>
.wrapping-flex-tiles {
  @include wrapping-flex-tiles($width: 320px);
}
</style>
