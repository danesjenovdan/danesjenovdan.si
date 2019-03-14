<template>
  <header class="row">
    <div class="col-md-4">
      <h1 v-text="title"/>
      <hr :class="`border-${color}`">
    </div>
    <div class="col-md-8">
      <p class="lead" v-text="text"/>
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

  @include media-breakpoint-up(md) {
    padding: 5rem 0 4rem;
  }

  h1 {
    font-size: 3.5rem;
    font-weight: 200;
    letter-spacing: 1.2px;
  }

  hr {
    border-top-width: 18px;
    border-top-color: $color-red;
  }

  p.lead {
    max-width: 630px;
    line-height: 1.3;
    margin-top: 0.7rem;
  }
}
</style>
