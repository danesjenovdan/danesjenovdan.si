<template>
  <div class="page">
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

export default {
  components: {
    SideMenu,
  },
};
</script>

<style lang="scss" scoped>
.page {
  display: flex;

  .content {
    flex: 1;
    margin-left: 0;

    @include media-breakpoint-up(md) {
      margin-left: $side-menu-width;
    }

    .content-container {
      padding-left: 5rem;
      padding-right: 5rem;
    }
  }
}
</style>
