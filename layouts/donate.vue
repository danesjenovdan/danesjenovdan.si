<template>
  <div :class="['page', `page--${pageColor}`]">
    <section class="content">
      <div class="container-fluid content-container">
        <nuxt />
        <div>
          <page-footer :color="pageColor" />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import PageFooter from '~/components/PageFooter/PageFooter.vue';

export default {
  components: {
    PageFooter,
  },
  computed: {
    pageColor() {
      // https://github.com/nuxt/nuxt.js/issues/722#issuecomment-301762247
      return this.$route.matched.map((r) => {
        return r.components.default.options
          ? r.components.default.options.pageColor
          : r.components.default.pageColor;
      })[0];
    },
  },
  watch: {
    $route() {
      this.$nuxt.$emit('toggle-menu', false);
    },
  },
};
</script>

<style lang="scss" scoped>
.page {
  display: flex;
  min-height: 100vh;

  background-color: #ffffff;

  .content {
    flex: 1;

    .content-container {
      padding-left: $content-mobile-padding;
      padding-right: $content-mobile-padding;
      max-width: 1320px;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;

      @include media-breakpoint-up(md) {
        padding-left: 3rem;
        padding-right: 3rem;
      }

      // @include media-breakpoint-up(lg) {
      //   padding-left: 5rem;
      //   padding-right: 5rem;
      // }
    }
  }
}
</style>
