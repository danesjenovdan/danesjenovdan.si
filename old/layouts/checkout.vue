<template>
  <div :class="['page', `page--${pageColor}`]">
    <section class="content">
      <div class="container content-container">
        <nuxt />
      </div>
    </section>
  </div>
</template>

<script>
export default {
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
};
</script>

<style lang="scss" scoped>
.page {
  display: flex;
  min-height: 100vh;
  background-color: #fff;

  .content {
    flex: 1;
    margin-left: 0;

    .content-container {
      padding-left: 0;
      padding-right: 0;
      height: 100%;
      display: flex;
      flex-direction: column;
      // justify-content: center;

      @include media-breakpoint-up(md) {
        // padding-left: 3rem;
        // padding-right: 3rem;
        max-width: 1600px;
      }
    }
  }
}
</style>
