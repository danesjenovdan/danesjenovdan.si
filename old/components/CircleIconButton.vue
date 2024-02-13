<template>
  <a
    :href="href"
    :class="['circle-icon-button', `circle-icon-button--${color}`]"
    target="_blank"
    rel="noopener noreferrer"
  >
    <div :class="['icon', `icon-${icon}`]"></div>
  </a>
</template>

<script>
export default {
  props: {
    color: {
      type: String,
      default: 'primary',
    },
    icon: {
      type: String,
      required: true,
    },
    href: {
      type: String,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.circle-icon-button {
  display: inline-block;
  width: 3.5rem;
  height: 3.5rem;
  border-radius: 50%;
  background-color: $color-green;
  border: none;
  margin: 0 0.5rem;
  transition: transform 0.15s;
  position: relative;
  overflow: hidden;

  .icon {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    transition: transform 0.15s, opacity 0.15s;
  }

  &:hover {
    transform: scale(1.05);

    .icon {
      transform: scale(1.1);
      opacity: 0.85;
    }
  }

  @each $color-name, $color in $theme-colors {
    &--#{$color-name} {
      background-color: $color;
    }
  }
}
</style>
