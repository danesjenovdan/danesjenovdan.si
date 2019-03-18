<template>
  <div>
    <page-title :title="$t('menu.agrument')" :text="$t('agrument.description')"/>
    <agrument-article v-for="post in posts" :key="post.id" :post="post"/>
    <div v-waypoint="{ active: true, callback: onWaypoint, options: intersectionOptions }"/>
  </div>
</template>

<script>
import axios from 'axios';
import PageTitle from '~/components/PageTitle.vue';
import AgrumentArticle from '~/components/AgrumentArticle.vue';

export default {
  components: {
    PageTitle,
    AgrumentArticle,
  },
  data() {
    return {
      intersectionOptions: {
        rootMargin: '100%',
        threshold: 0,
      },
    };
  },
  async asyncData({ params, error }) {
    const latestPosts = await axios
      .get(`https://agrument.danesjenovdan.si/api/v2/posts?limit=5`)
      .then(res => res.data);
    const posts = [...latestPosts.data];
    const nextPageLink = latestPosts.links.next;
    return {
      posts,
      nextPageLink,
    };
  },
  methods: {
    async fetchNextPage() {
      if (this.nextPageLink) {
        const nextPosts = await axios.get(this.nextPageLink).then(res => res.data);
        this.posts.push(...nextPosts.data);
        this.nextPageLink = nextPosts.links.next;
      }
    },
    onWaypoint({ going, direction }) {
      if (going === this.$waypointMap.GOING_IN && direction === this.$waypointMap.DIRECTION_TOP) {
        this.fetchNextPage();
      }
    },
  },
  head() {
    return {
      title: this.$t('menu.agrument'),
    };
  },
};
</script>

<style lang="scss" scoped>
</style>
