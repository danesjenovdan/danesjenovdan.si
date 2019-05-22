<template>
  <component
    :is="to ? 'nuxt-link' : 'div'"
    :to="to"
    :class="['section-header', `section-header--${color}`]"
  >
    <span v-if="icon" :class="['icon', `icon-${icon}--${color}`]"/>
    <span v-text="text"/>
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

  &::before,
  &::after {
    position: absolute;
    left: 1.5rem;
    top: 0.4rem;
    display: block;
    content: '';
    background-color: $color-green;
    width: 100%;
    height: 1px;
    transition: all 0.15s ease;
  }

  &::after {
    top: auto;
    bottom: -0.4rem;
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

      &::before,
      &::after {
        background-color: $color;
      }
    }
  }
}

a.section-header:hover {
  &::before,
  &::after {
    top: 0;
    left: 0;
  }

  &::after {
    top: auto;
    bottom: 0;
  }

  span {
    transform: none;
  }
}
</style>
