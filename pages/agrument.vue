<template>
  <div>
    <page-title :title="$t('menu.agrument')" :text="$t('agrument.description')"/>
    <agrument-article v-for="post in posts" :key="post.id" :post="post"/>
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
  async asyncData({ params, error }) {
    const latestPost = await axios
      .get(`https://agrument.danesjenovdan.si/api/agrument`)
      .then(res => res.data.post);
    const date = new Date(latestPost.date).toISOString().split('T')[0];
    const secondPost = await axios
      .get(`https://agrument.danesjenovdan.si/api/agrument?date=${date}&direction=older`)
      .then(res => res.data.post);
    const posts = [latestPost, secondPost];
    return {
      posts,
    };
  },
};
</script>

<style lang="scss" scoped>
</style>
