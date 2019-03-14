<template>
  <div>
    <page-title :title="$t('menu.agrument')" :text="$t('agrument.description')"/>
    <agrument-article/>
    <agrument-article/>
    <agrument-article/>
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';
import AgrumentArticle from '~/components/AgrumentArticle.vue';

export default {
  components: {
    PageTitle,
    AgrumentArticle,
  },
  data() {
    return {};
  },
};
</script>

<style lang="scss" scoped>
</style>
