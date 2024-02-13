<template>
  <header class="row">
    <div class="col-xl-4">
      <h1 v-text="title" />
      <hr :class="`border-${color}`" />
    </div>
    <div class="col-xl-8">
      <p class="lead" v-text="text" />
    </div>
  </header>
</template>

<script>
export default {
  name: 'PageTitle',
  props: {
    title: {
      type: String,
      required: true,
    },
    text: {
      type: String,
      required: true,
    },
    color: {
      type: String,
      default: 'primary',
    },
  },
};
</script>

<style lang="scss" scoped>
header {
  padding: 1.2rem 0 0.5rem;
  // margin-left: -$content-mobile-padding;
  // margin-right: -$content-mobile-padding;

  @include media-breakpoint-up(md) {
    padding: 3rem 0 2rem;
  }

  @include media-breakpoint-up(xl) {
    padding: 5rem 0 2rem;
  }

  h1 {
    font-size: 2.5rem;
    font-weight: 200;
    letter-spacing: 0.8px;

    @include media-breakpoint-up(xl) {
      font-size: 3.5rem;
      letter-spacing: 1.2px;
    }
  }

  hr {
    border-top-width: 18px;
    border-top-color: $color-red;
    max-width: 630px;
    margin-left: 0;
  }

  p.lead {
    max-width: 630px;
    line-height: 1.3;
    margin-top: 0.7rem;
    margin-bottom: 1rem;

    @include media-breakpoint-up(xl) {
      margin-bottom: 3rem;
    }
  }
}
</style>
