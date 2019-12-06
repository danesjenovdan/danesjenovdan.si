<template>
  <dynamic-link
    v-bind="$attrs"
    :to="to"
    :class="['more-button', `more-button--${color}`, { 'more-button--block': block, 'more-button--lg': large, disabled: disabled }]"
    :disabled="disabled"
    v-on="$listeners"
  >
    <span v-if="icon" :class="['icon', `icon-${icon}--${color}`]" />
    <span class="text" v-text="text" />
    <div class="arrow">
      <span :class="['icon', `icon-arrow--${color}`]" />
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
    large: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style lang="scss" scoped>
.more-button {
  display: inline-flex;
  align-items: center;
  padding: 0.75rem 1.75rem 0.75rem 1.5rem;
  border: 1px solid $color-green;
  font-size: 1.2rem;
  font-style: italic;
  font-weight: 600;
  letter-spacing: 0.125em;
  line-height: 1;
  color: inherit;
  text-decoration: none;
  transition: background-color 0.15s;

  .icon {
    display: block;
    height: 1em;
    width: 1em;
    margin-right: 1.25rem;
  }

  .text {
    flex: 1;
    position: relative;
    top: -0.05em;
  }

  .arrow {
    margin-left: 1rem;

    .icon {
      margin: 0;
      transform: rotate(-90deg);
      transition: transform 0.15s;
    }
  }

  &:hover {
    background-color: rgba($color-green, 0.15);

    .arrow {
      .icon {
        transform: rotate(-90deg) translateY(1rem);
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

  &.more-button--lg {
    font-size: 2rem;
  }

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
        .icon {
          transform: rotate(-90deg) translateX(45%) translateY(1rem);
        }
      }
    }
  }

  @each $color-name, $color in $theme-colors {
    &--#{$color-name} {
      border-color: $color;
      color: $color;

      &:hover {
        background-color: rgba($color, 0.15);
      }
    }
  }
}
</style>
