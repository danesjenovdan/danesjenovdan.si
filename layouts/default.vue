<template>
  <div class="page">
    <top-bar/>
    <side-menu/>
    <section class="content">
      <b-container fluid class="content-container">
        <nuxt/>
        <!-- <cta-box/> -->
        <page-footer/>
      </b-container>
    </section>
  </div>
</template>

<script>
import SideMenu from '~/components/SideMenu/SideMenu';
import TopBar from '~/components/SideMenu/TopBar';
import PageFooter from '~/components/PageFooter/PageFooter';

export default {
  components: {
    SideMenu,
    TopBar,
    PageFooter,
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

  .content {
    flex: 1;
    margin-left: 0;
    margin-top: calc(66px + 2.4rem);

    @include media-breakpoint-up(md) {
      margin-left: $side-menu-width;
      margin-top: 0;
    }

    .content-container {
      padding-left: $content-mobile-padding;
      padding-right: $content-mobile-padding;
      max-width: 1500px;
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
