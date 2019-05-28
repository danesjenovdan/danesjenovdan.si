<template>
  <div :class="['page', `page--${pageColor}`]">
    <top-bar/>
    <side-menu/>
    <section class="content">
      <b-container fluid class="content-container">
        <nuxt/>
        <div>
          <div class="row mobile-no-gap">
            <div class="col-12 mt-5">
              <support-bar :color="pageColor"/>
            </div>
          </div>
          <page-footer :color="pageColor"/>
        </div>
      </b-container>
    </section>
  </div>
</template>

<script>
import SideMenu from '~/components/SideMenu/SideMenu.vue';
import TopBar from '~/components/SideMenu/TopBar.vue';
import SupportBar from '~/components/SupportBar.vue';
import PageFooter from '~/components/PageFooter/PageFooter.vue';

export default {
  components: {
    SideMenu,
    TopBar,
    SupportBar,
    PageFooter,
  },
  computed: {
    pageColor() {
      // https://github.com/nuxt/nuxt.js/issues/722#issuecomment-301762247
      return this.$route.matched.map(r => {
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
