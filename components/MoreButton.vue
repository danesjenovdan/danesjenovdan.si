<template>
  <component
    :is="isExternalUrl ? 'a' : 'nuxt-link'"
    :href="to"
    :to="to"
    :target="isExternalUrl ? '_blank' : null"
    :rel="isExternalUrl ? 'noopener noreferrer' : null"
    :class="['more-button', `more-button--${color}`, { 'more-button--block': block, disabled: disabled }]"
    :disabled="disabled"
  >
    <span v-if="icon" :class="['icon', `icon-${icon}--${color}`]"/>
    <span v-text="text"/>
    <span :class="['arrow', 'icon', `icon-arrow--${color}`]"/>
  </component>
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
    icon: {
      type: String,
      default: null,
    },
    block: {
      type: Boolean,
      default: false,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    isExternalUrl() {
      return this.to && /^https?:\/\//.test(this.to);
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

    .arrow {
      position: absolute;
      right: 1.75rem;
      top: 50%;
      transform: rotate(-90deg) translateX(45%);
    }

    &:hover {
      .arrow {
        transform: rotate(-90deg) translateX(45%) translateY(1rem);
      }
    }
  }

  .icon {
    height: 1.5em;
    width: 1.5em;
    margin-right: 0.25rem;
  }

  .arrow {
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

    .arrow {
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

  &.disabled,
  &:disabled {
    pointer-events: none;
    cursor: not-allowed;
    filter: grayscale(1);
    background-color: #ccc;
  }
}
</style>
