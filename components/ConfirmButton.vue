<template>
  <dynamic-link
    v-bind="$attrs"
    :to="to"
    :class="[
      'confirm-button',
      `confirm-button--${color}`,
      {
        'confirm-button--block': block,
        'confirm-button--arrow': arrow,
        'confirm-button--hearts': hearts,
        disabled: disabled,
      },
    ]"
    :disabled="disabled"
    v-on="$listeners"
  >
    <div v-if="arrow" class="arrow">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="30 18 110.9 40"
        fill="#fff"
      >
        <path
          d="M140.9 38a3 3 0 00-.9-2l-16-17c-1-1-3.1-1.4-4.3-.3-1.2 1-1.2 3.2 0 4.4L131 35H30v6h101l-11.3 12c-1 1-1.2 3.2 0 4.3 1.2 1 3.3.8 4.3-.2l16-17c.6-.6.9-1.3.9-2.1z"
        />
      </svg>
    </div>
    <span v-text="text" class="text" />
    <div v-if="hearts" class="hearts">
      <div v-for="i in 3" :key="i" class="heart">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="8 0 92 100"
          fill="#fff"
        >
          <path
            d="M32.3 15c-5.3 0-10.5 2.2-14.4 6.4a22.5 22.5 0 000 30.3L47.8 84a3 3 0 004.4 0l30-32.2a22.5 22.5 0 000-30.4c-8-8.4-21-8.4-28.9 0L50 25l-3.3-3.6A20 20 0 0032.3 15zm0 5.9c3.6 0 7.1 1.5 10 4.6l5.5 6a3 3 0 004.4 0l5.5-6a13.2 13.2 0 0120 0c5.7 6.1 5.7 16 0 22.2L50 77.5 22.3 47.7a16.5 16.5 0 010-22.2c2.8-3 6.4-4.6 10-4.6z"
          />
        </svg>
      </div>
    </div>
  </dynamic-link>
</template>

<script>
import DynamicLink from '~/components/DynamicLink.vue';

export default {
  components: {
    DynamicLink,
  },
  props: {
    to: {
      type: String,
      default: '',
    },
    text: {
      type: String,
      required: true,
    },
    color: {
      type: String,
      default: 'primary',
    },
    block: {
      type: Boolean,
      default: false,
    },
    arrow: {
      type: Boolean,
      default: false,
    },
    hearts: {
      type: Boolean,
      default: false,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style lang="scss" scoped>
.confirm-button {
  display: inline-flex;
  align-items: center;
  padding: 1.3rem 3.2rem;
  font-size: 1.2rem;
  font-style: italic;
  font-weight: 600;
  letter-spacing: 0.125em;
  line-height: 1;
  color: #fff;
  text-decoration: none;
  background-color: $color-green;
  transition: background-color 0.15s;
  text-transform: uppercase;
  position: relative;
  overflow: hidden;

  .text {
    flex: 1;
    position: relative;
    top: -0.05em;
  }

  .arrow {
    margin: -1em 0.5rem -1em -3.5rem;
    display: flex;
    height: 1.125em;

    svg {
      height: 100%;
    }
  }

  .hearts {
    margin: -1em -2.5rem -1em 0.5rem;

    .heart {
      height: 1.75em;
      display: inline-block;

      svg {
        height: 100%;
      }
    }
  }

  &.disabled,
  &:disabled {
    pointer-events: none;
    cursor: not-allowed;
    opacity: 0.7;
  }

  &.confirm-button--arrow {
    padding-right: 2rem;
  }

  &.confirm-button--hearts {
    padding-right: 3.2rem;
  }

  &.confirm-button--block {
    width: 100%;
  }

  @each $color-name, $color in $theme-colors {
    &--#{$color-name} {
      background-color: $color;

      // &:hover {
      //   background-color: rgba($color, 0.15);
      // }
    }
  }
}
</style>
