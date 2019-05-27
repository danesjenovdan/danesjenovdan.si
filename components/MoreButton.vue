<template>
  <nuxt-link
    :to="to"
    :class="['more-button', `more-button--${color}`, { 'more-button--block': block }]"
  >
    <span v-text="text"/>
    <span :class="['icon', `icon-arrow--${color}`]"/>
  </nuxt-link>
</template>

<script>
export default {
  props: {
    to: {
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
    block: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style lang="scss" scoped>
.more-button {
  display: inline-block;
  border: 1px solid $color-green;
  padding: 0.5rem 2rem 0.5rem 1.5rem;
  font-size: 1.2rem;
  font-style: italic;
  font-weight: 600;
  color: inherit;
  text-decoration: none;

  &.more-button--block {
    width: 100%;
    position: relative;

    .icon {
      position: absolute;
      right: 1.75rem;
      top: 50%;
      transform: rotate(-90deg) translateX(45%);
    }

    &:hover {
      .icon {
        transform: rotate(-90deg) translateX(45%) translateY(1rem);
      }
    }
  }

  .icon {
    height: 1.15em;
    width: 1.15em;
    margin-left: 0.25rem;
    transform: rotate(-90deg);
    position: relative;
    top: -0.1em;
    transition: transform 0.15s;
  }

  span {
    display: inline-block;
    vertical-align: bottom;
  }

  &:hover {
    background-color: rgba($color-green, 0.15);

    .icon {
      transform: rotate(-90deg) translateY(1rem);
    }
  }

  @each $color-name, $color in $theme-colors {
    &--#{$color-name} {
      border-color: $color;

      &:hover {
        background-color: rgba($color, 0.15);
      }
    }
  }
}
</style>
