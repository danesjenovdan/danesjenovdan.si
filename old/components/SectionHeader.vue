<template>
  <!-- eslint-disable-next-line vue/require-component-is -->
  <component
    :is="to ? 'nuxt-link' : 'div'"
    :to="to"
    :class="['section-header', `section-header--${color}`]"
  >
    <span v-if="icon" :class="['icon', `icon-${icon}--${color}`]" />
    <span v-text="text" />
  </component>
</template>

<script>
export default {
  props: {
    to: {
      type: String,
      default: null,
    },
    text: {
      type: String,
      required: true,
    },
    color: {
      type: String,
      default: 'primary',
    },
    icon: {
      type: String,
      default: null,
    },
  },
};
</script>

<style lang="scss" scoped>
.section-header {
  display: inline-block;
  background-color: rgba($color-green, 0.15);
  font-size: 1.25rem;
  line-height: 1;
  font-weight: 600;
  font-style: italic;
  padding: 0.5rem 1.5rem;
  position: relative;
  margin: 1rem 0;
  text-decoration: none;
  color: inherit;

  &::before {
    position: absolute;
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
    display: block;
    content: '';
    border: 1px solid $color-green;
    border-width: 1px 0 1px 0;
    transition: transform 0.15s ease;
    transform: translate(1.5rem, 0.4rem);
  }

  &::after {
    top: auto;
    bottom: 0;
  }

  .icon {
    height: 1em;
    width: 1em;
    margin-right: 0.25rem;
  }

  span {
    display: inline-block;
    vertical-align: bottom;
    transform: translateY(35%);
    transition: all 0.15s ease;
  }

  @each $color-name, $color in $theme-colors {
    &--#{$color-name} {
      background-color: rgba($color, 0.15);

      &::before {
        border-color: $color;
      }
    }
  }
}

a.section-header:hover {
  &::before {
    transform: translate(0, 0);
  }

  span {
    transform: none;
  }
}
</style>
