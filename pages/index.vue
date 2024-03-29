<template>
  <div>
    <page-title
      :title="$t('danes-je-nov-dan')"
      :text="$t('landing.description')"
    />
    <div v-if="infopush && infopush.visible">
      <info-push
        :image="infopush.image"
        :alt="infopush.alt"
        :title="infopush.title"
        :text="infopush.desc"
        :button-text="infopush.cta_text"
        :button-url="infopush.cta_url"
      />
    </div>
    <div v-if="$i18n.locale !== 'en' && !agrumentPosts" class="row">
      <div class="col-12">
        <section-header
          text="Agrument ima trenutno tehnične težave. Upamo, da jih čim prej razrešimo."
          icon="section-agrument"
        />
      </div>
    </div>
    <template v-if="$i18n.locale !== 'en' && agrumentPosts">
      <div class="row">
        <div class="col-12">
          <section-header
            :to="localePath('agrument-date')"
            :text="$t('menu.agrument')"
            icon="section-agrument"
          />
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
            v-for="agrumentPost in agrumentPosts.slice(1, 4)"
            :key="`${agrumentPost.id}`"
            class="flex-tile"
          >
            <preview-tile
              :alt="agrumentPost.alt"
              :image="agrumentPost.image_url"
              :title="agrumentPost.title"
              :byline="toSloDate(agrumentPost.datetime)"
              :text="agrumentPost.description"
              :url="agrumentPost.url"
            />
          </div>
          <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile" />
        </div>
      </div>
      <div class="d-flex justify-content-center">
        <more-button
          :to="localePath('agrument-date')"
          :text="$t('agrument.more')"
        />
      </div>
      <div class="row mobile-no-gap">
        <div class="col-12 my-5">
          <agrument-subscribe-bar />
        </div>
      </div>
    </template>
    <div class="row">
      <div class="col-12">
        <section-header
          :to="localePath('projects')"
          :text="$t('menu.projects')"
          color="secondary"
          icon="section-projects"
        />
      </div>
    </div>
    <div>
      <div v-if="projects && projects.length" class="wrapping-flex-tiles">
        <div
          v-for="project in projects.slice(0, 3)"
          :key="`${project.url}`"
          class="flex-tile"
        >
          <project-tile
            :image="project.image"
            :alt="project.alt"
            :title="project.title"
            :byline="toMonthYear(project.date)"
            :text="project.desc"
            :url="project.url || '/'"
          />
        </div>
        <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile" />
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <more-button
        :to="localePath('projects')"
        :text="$t('projects.more')"
        color="secondary"
      />
    </div>
    <div class="row mobile-no-gap">
      <div class="col-12 my-5">
        <shop-bar v-if="$i18n.locale !== 'en'" />
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <section-header
          :to="localePath('clipping')"
          :text="$t('menu.clipping')"
          color="warning"
          icon="section-clipping"
        />
      </div>
    </div>
    <div>
      <div v-if="clippings && clippings.length" class="wrapping-flex-tiles">
        <div
          v-for="clip in clippings.slice(0, 3)"
          :key="`${clip.url}`"
          class="flex-tile"
        >
          <preview-tile
            :alt="clip.alt"
            :image="clip.image"
            :title="clip.title"
            :byline="`${clip.publisher}, ${toSloDate(clip.date)}`"
            :url="clip.url"
          />
        </div>
        <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile" />
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <more-button
        :to="localePath('clipping')"
        :text="$t('clipping.more')"
        color="warning"
      />
    </div>
    <div class="row mobile-no-gap">
      <div class="col-12 my-5">
        <social-media-bar
          :text="$t('projects.social-bar.follow-us')"
          :icons="[
            { icon: 'facebook', url: 'https://facebook.com/danesjenovdan' },
            { icon: 'twitter', url: 'https://twitter.com/danesjenovdan' },
            {
              icon: 'instagram',
              url: 'https://www.instagram.com/danesjenovdan',
            },
          ]"
          color="secondary"
        />
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <section-header
          :to="localePath('videos')"
          :text="$t('menu.videos')"
          color="warning"
          icon="section-videos"
        />
      </div>
    </div>
    <div v-if="videos && videos.length" class="mt-4">
      <promoted-tile
        :image="videos[0].image"
        :title="videos[0].title"
        :byline="toSloDate(videos[0].date)"
        :text="videos[0].desc"
        :url="localePath({ name: 'videos', query: { video: videos[0].url } })"
        :video="videos[0].url"
        color="warning"
      />
      <div class="wrapping-flex-tiles">
        <div
          v-for="video in videos.slice(1, 4)"
          :key="`${video.url}`"
          class="flex-tile"
        >
          <preview-tile
            :alt="video.alt"
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
    <div class="d-flex justify-content-center">
      <more-button
        :to="localePath('videos')"
        :text="$t('videos.more')"
        color="warning"
      />
    </div>
    <div class="row mobile-no-gap">
      <div class="col-12 my-5">
        <social-media-bar
          :text="$t('videos.social-bar.follow-us')"
          :icons="[
            {
              icon: 'youtube',
              url: 'https://www.youtube.com/channel/UCWMqx3p_QtWjdDRq58Hfh_w',
            },
            { icon: 'vimeo', url: 'https://vimeo.com/user26914674' },
          ]"
          color="warning"
        />
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <section-header
          :to="localePath('tools')"
          :text="$t('menu.tools')"
          color="warning"
          icon="section-tools"
        />
      </div>
    </div>
    <div>
      <div class="wrapping-flex-tiles">
        <div class="flex-tile">
          <tool-preview-tile
            :title="$t('tools.tools.newsgradient.title')"
            :text="$t('tools.tools.newsgradient.description')"
            icon="newsgradient"
          />
        </div>
        <div class="flex-tile">
          <tool-preview-tile
            :title="$t('tools.tools.parlameter.title')"
            :text="$t('tools.tools.parlameter.description')"
            icon="parlameter"
          />
        </div>
        <div class="flex-tile">
          <tool-preview-tile
            :title="$t('tools.tools.consul.title')"
            :text="$t('tools.tools.consul.description')"
            icon="consul"
          />
        </div>
        <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile" />
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <more-button
        :to="localePath('tools')"
        :text="$t('tools.more')"
        color="warning"
      />
    </div>
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';
import InfoPush from '~/components/InfoPush.vue';
import SectionHeader from '~/components/SectionHeader.vue';
import ProjectTile from '~/components/ProjectTile.vue';
import PromotedTile from '~/components/PromotedTile.vue';
import PreviewTile from '~/components/PreviewTile.vue';
import ToolPreviewTile from '~/components/ToolPreviewTile.vue';
import MoreButton from '~/components/MoreButton.vue';
import AgrumentSubscribeBar from '~/components/AgrumentSubscribeBar.vue';
import SocialMediaBar from '~/components/SocialMediaBar.vue';
import ShopBar from '~/components/ShopBar.vue';
import dateMixin from '~/mixins/date.js';

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
    InfoPush,
  },
  mixins: [dateMixin],
  async asyncData({ app, $axios, params, error }) {
    const lang = `lang=${app.i18n.locale}`;
    const order = `ordering=-date`;
    const [
      agrumentResponse,
      clippingsResponse,
      projectsResponse,
      videosResponse,
      infopushResponse,
    ] = await Promise.all([
      $axios.$get(`https://napake.djnd.si/api/v2/posts?limit=5`),
      $axios.$get(`https://djnapi.djnd.si/djnd.si/clips/?${lang}&${order}`),
      $axios.$get(`https://djnapi.djnd.si/djnd.si/projects/?${lang}&${order}`),
      $axios.$get(`https://djnapi.djnd.si/djnd.si/videos/?${lang}&${order}`),
      $axios.$get(`https://djnapi.djnd.si/djnd.si/infopushes/?${lang}`),
    ]);
    return {
      agrumentPosts: agrumentResponse.data.map((post) => {
        const manipulatedPost = post;
        manipulatedPost.url = post.url.replace(
          'agrument.danesjenovdan.si',
          'danesjenovdan.si/agrument',
        );
        manipulatedPost.image_url = post.image_url.replace(
          'agrument.danesjenovdan.si',
          'napake.djnd.si',
        );
        return manipulatedPost;
      }),
      clippings: clippingsResponse.results,
      projects: projectsResponse.results,
      videos: videosResponse.results,
      infopush: infopushResponse.results[0],
    };
  },
};
</script>

<style lang="scss" scoped>
.wrapping-flex-tiles {
  @include wrapping-flex-tiles($width: 300px, $width-xl: 345px);
}
</style>
