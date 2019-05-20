<template>
  <div class="social-bar bg-white">
    <div class="bar-container">
      <strong v-text="text"/>
      <div class="buttons my-xl-2">
        <circle-icon-button
          v-for="icon in icons"
          :key="`${icon.icon}`"
          :color="color"
          :icon="icon.icon"
          :href="icon.url"
        />
      </div>
    </div>
  </div>
</template>

<script>
import CircleIconButton from '~/components/CircleIconButton.vue';

export default {
  components: {
    CircleIconButton,
  },
  props: {
    color: {
      type: String,
      default: 'primary',
    },
    text: {
      type: String,
      required: true,
    },
    icons: {
      type: Array,
      default: () => [],
    },
  },
};
</script>

<style lang="scss" scoped>
.social-bar {
  padding: 1rem $content-mobile-padding 1.2rem;

  @include media-breakpoint-up(xl) {
    padding: 0.75rem 3rem;
  }

  .bar-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-direction: column;

    @include media-breakpoint-up(xl) {
      flex-direction: row;
      justify-content: center;
    }

    strong,
    .buttons {
      text-align: center;
    }

    strong {
      max-width: 270px;

      @include media-breakpoint-up(xl) {
        max-width: initial;
        margin-right: 1rem;
      }
    }

    .buttons {
      display: flex;
      margin-top: 1.5rem;

      @include media-breakpoint-up(xl) {
        margin-top: 0;
      }
    }
  }
}
</style>
