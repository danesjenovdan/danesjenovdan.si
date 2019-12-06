<template>
  <div>
    <page-title
      :title="$t('menu.agrument')"
      :text="$t('agrument.description')"
    />
    <agrument-article :post="posts[0]" />
    <div class="row mobile-no-gap">
      <div class="col-12 mb-3 mb-md-5">
        <agrument-subscribe-bar />
      </div>
    </div>
    <agrument-article
      v-for="post in posts.slice(1)"
      :key="post.id"
      v-waypoint="{
        active: true,
        callback: onArticleWaypoint(post),
        options: {
          rootMargin: '-35%',
          threshold: 0,
        },
      }"
      :post="post"
    />
    <div
      v-waypoint="{
        active: true,
        callback: onWaypoint,
        options: {
          rootMargin: '100%',
          threshold: 0,
        },
      }"
    />
  </div>
</template>

<script>
import { uniqBy } from 'lodash';
import PageTitle from '~/components/PageTitle.vue';
import AgrumentArticle from '~/components/AgrumentArticle.vue';
import AgrumentSubscribeBar from '~/components/AgrumentSubscribeBar.vue';
import dateMixin from '~/mixins/date.js';

export default {
  components: {
    PageTitle,
    AgrumentArticle,
    AgrumentSubscribeBar,
  },
  mixins: [dateMixin],
  async asyncData({ $axios, params, error }) {
    const agrumentResponse = await $axios.$get(
      'https://agrument.danesjenovdan.si/api/v2/posts?limit=5',
    );
    const posts = [...agrumentResponse.data];
    const nextPageLink = agrumentResponse.links.next;
    return {
      posts,
      nextPageLink,
    };
  },
  methods: {
    async fetchNextPage() {
      if (this.nextPageLink) {
        const nextPosts = await this.$axios.$get(this.nextPageLink);
        this.posts = uniqBy([...this.posts, ...nextPosts.data], 'id');
        this.nextPageLink = nextPosts.links.next;
      }
    },
    onWaypoint({ going, direction }) {
      if (
        going === this.$waypointMap.GOING_IN &&
        direction === this.$waypointMap.DIRECTION_TOP
      ) {
        this.fetchNextPage();
      }
    },
    onArticleWaypoint(post) {
      return ({ going, direction, el }) => {
        if (!direction) {
          // ignore initial page load
          return;
        }
        if (going === this.$waypointMap.GOING_IN) {
          const path = this.localePath({
            name: 'agrument-date',
            params: { date: this.toSloUrlDate(post.datetime) },
          });
          if (typeof window !== 'undefined') {
            window.history.replaceState(window.history.state, null, path);
          }
        }
      };
    },
  },
  head() {
    return {
      title: this.$t('menu.agrument'),
    };
  },
};
</script>
