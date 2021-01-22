<template>
  <div>
    <page-title
      :title="$t('menu.agrument')"
      :text="$t('agrument.description')"
    />
    <div
      v-waypoint="{
        active: true,
        callback: onTopWaypoint,
        options: {
          rootMargin: '15%',
          threshold: 0,
        },
      }"
    />
    <agrument-article
      v-waypoint="{
        active: true,
        callback: onArticleWaypoint(posts[0]),
        options: {
          rootMargin: '-35%',
          threshold: 0,
        },
      }"
      :post="posts[0]"
    />
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
  validate({ params }) {
    if (params.date == null) {
      return true;
    }
    return /^\d{1,2}\.\d{1,2}\.\d{4}$/g.test(params.date);
  },
  async asyncData({ $axios, params, error }) {
    const apiUrl = 'https://napake.djnd.si/api/v2/posts';
    const apiParams = {
      limit: 5,
      start_date: params.date,
    };
    const agrumentResponse = await $axios.$get(apiUrl, {
      params: apiParams,
    });
    const posts = [...agrumentResponse.data];
    const nextPageLink = agrumentResponse.links.next;
    return {
      posts,
      nextPageLink,
      activePost: posts[0],
    };
  },
  head() {
    if (!this.activePost) {
      return {
        title: this.$t('menu.agrument'),
      };
    }
    // create canonical url for og tag, trim trailing slash from path
    const path = this.$route.path.replace(/^(.+?)\/*?$/, '$1');
    const canonicalUrl = `https://danesjenovdan.si${path}`;
    return {
      title: `${this.activePost.title} - ${this.$t('menu.agrument')}`,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: this.activePost.description,
        },
        {
          hid: 'og:type',
          property: 'og:type',
          content: 'article',
        },
        {
          hid: 'og:title',
          property: 'og:title',
          content: this.activePost.title,
        },
        {
          hid: 'og:description',
          property: 'og:description',
          content: this.activePost.description,
        },
        {
          hid: 'og:image',
          property: 'og:image',
          content: this.activePost.image_url.replace(
            'agrument.danesjenovdan.si',
            'napake.djnd.si',
          ),
        },
        {
          hid: 'og:url',
          property: 'og:url',
          content: canonicalUrl,
        },
        {
          hid: 'twitter:creator',
          name: 'twitter:creator',
          content: '@danesjenovdan',
        },
        {
          hid: 'twitter:card',
          name: 'twitter:card',
          content: 'summary_large_image',
        },
        {
          hid: 'twitter:title',
          name: 'twitter:title',
          content: this.activePost.title,
        },
        {
          hid: 'twitter:description',
          name: 'twitter:description',
          content: this.activePost.description,
        },
        {
          hid: 'twitter:image',
          name: 'twitter:image',
          content: this.activePost.image_url,
        },
      ],
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
    onTopWaypoint({ going, direction }) {
      if (
        going === this.$waypointMap.GOING_IN &&
        direction === this.$waypointMap.DIRECTION_BOTTOM
      ) {
        const path = this.localePath('agrument-date');
        this.activePost = this.posts[0];
        if (typeof window !== 'undefined') {
          window.history.replaceState(window.history.state, null, path);
        }
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
          this.activePost = post;
          if (typeof window !== 'undefined') {
            window.history.replaceState(window.history.state, null, path);
          }
        }
      };
    },
  },
};
</script>
