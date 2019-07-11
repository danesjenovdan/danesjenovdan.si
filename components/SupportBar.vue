<template>
  <div class="support-bar">
    <div class="bar-container">
      <more-button :to="localePath('shop')" text="Podpri nas!" :color="color" icon="heart" />
      <more-button
        :to="localePath('shop')"
        text="Pridruži se nam!"
        :color="color"
        icon="friendship"
      />
    </div>
  </div>
</template>

<script>
import MoreButton from '~/components/MoreButton.vue';

export default {
  components: {
    MoreButton,
  },
  props: {
    color: {
      type: String,
      default: 'primary',
    },
  },
};
</script>


<style lang="scss" scoped>
.support-bar {
  padding: 1rem $content-mobile-padding;
  overflow: hidden;
  background-color: #f6f6f6;

  @include media-breakpoint-up(xl) {
    padding: 0.75rem 3rem;
  }

  .bar-container {
    display: flex;
    flex-direction: column;

    @include media-breakpoint-up(lg) {
      flex-direction: row;
      justify-content: center;
    }

    .more-button {
      margin: 0.5rem 0;
      width: 100%;

      @include media-breakpoint-up(lg) {
        width: auto;
        margin: 0.5rem 0.5rem;
      }
    }
  }
}
</style>
