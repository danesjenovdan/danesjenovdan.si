<template>
  <div class="page page--secondary">
    <section class="content">
      <div class="container content-container">
        <nuxt/>
      </div>
    </section>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.page {
  display: flex;
  min-height: 100vh;
  outline: 1px solid gold;

  .content {
    flex: 1;
    margin-left: 0;
    outline: 1px solid magenta;

    .content-container {
      padding-left: $content-mobile-padding;
      padding-right: $content-mobile-padding;
      height: 100%;
      display: flex;
      flex-direction: column;
      // justify-content: center;

      @include media-breakpoint-up(md) {
        padding-left: 3rem;
        padding-right: 3rem;
      }
    }
  }
}
</style>
