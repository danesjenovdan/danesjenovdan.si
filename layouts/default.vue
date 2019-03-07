<template>
  <div class="page">
    <side-menu/>
    <section class="content">
      <nuxt/>
    </section>
  </div>
</template>

<script>
import SideMenu from '~/components/SideMenu/SideMenu';

export default {
  components: {
    SideMenu,
  },
};
</script>

<style lang="scss" scoped>
@import '~/assets/scss/_variables.scss';

.page {
  display: flex;

  .content {
    flex: 1;
    margin-left: 0;

    @include media-breakpoint-up(md) {
      margin-left: $side-menu-width;
    }
  }
}
</style>
