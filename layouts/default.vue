<template>
  <div class="page">
    <top-bar/>
    <side-menu/>
    <section class="content">
      <b-container fluid class="content-container">
        <nuxt/>
      </b-container>
    </section>
  </div>
</template>

<script>
import SideMenu from '~/components/SideMenu/SideMenu';
import TopBar from '~/components/SideMenu/TopBar';

export default {
  components: {
    SideMenu,
    TopBar,
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

  .content {
    flex: 1;
    margin-left: 0;
    margin-top: 104px;

    @include media-breakpoint-up(md) {
      margin-left: $side-menu-width;
      margin-top: 0;
    }

    .content-container {
      padding-left: $content-mobile-padding;
      padding-right: $content-mobile-padding;

      @include media-breakpoint-up(md) {
        padding-left: 3rem;
        padding-right: 3rem;
      }

      @include media-breakpoint-up(lg) {
        padding-left: 5rem;
        padding-right: 5rem;
      }
    }
  }
}
</style>
