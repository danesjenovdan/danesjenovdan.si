<template>
  <div :class="['email-subscription-tile', `section--${color}`]">
    <div class="row">
      <div class="left-col">
        <div class="header">
          <div :class="['icon', `icon-sub-${icon}`]" />
          <h2>{{ title }}</h2>
        </div>
        <div
          :class="[
            'd-none',
            'd-lg-flex',
            'switch-container',
            `switch-container--${color}`,
          ]"
        >
          <div v-if="loading" class="loader-container">
            <div class="lds-dual-ring" />
          </div>
          <div v-else class="text">{{ checked ? labelOn : labelOff }}</div>
          <div class="custom-control custom-switch">
            <input
              :id="uid1"
              :checked="checked"
              type="checkbox"
              class="custom-control-input"
              @change="$emit('change', $event.target.checked)"
            />
            <label :for="uid1" class="custom-control-label" />
          </div>
        </div>
      </div>
      <div class="right-col">
        <p class="description">{{ description }}</p>
        <slot />
        <div
          :class="[
            'd-flex',
            'd-lg-none',
            'switch-container',
            `switch-container--${color}`,
          ]"
        >
          <div v-if="loading" class="loader-container">
            <div class="lds-dual-ring" />
          </div>
          <div v-else class="text">{{ checked ? labelOn : labelOff }}</div>
          <div class="custom-control custom-switch">
            <input
              :id="uid2"
              :checked="checked"
              type="checkbox"
              class="custom-control-input"
              @change="$emit('change', $event.target.checked)"
            />
            <label :for="uid2" class="custom-control-label" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { uniqueId } from 'lodash';

export default {
  model: {
    prop: 'checked',
    event: 'change',
  },
  props: {
    title: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
    icon: {
      type: String,
      default: null,
    },
    labelOff: {
      type: String,
      default: '',
    },
    labelOn: {
      type: String,
      default: '',
    },
    color: {
      type: String,
      default: 'primary',
    },
    loading: {
      type: Boolean,
      default: false,
    },
    checked: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      uid1: null,
      uid2: null,
    };
  },
  mounted() {
    // for some reason ssr breaks this, so we do it in "mounted"
    this.uid1 = uniqueId('switch-');
    this.uid2 = uniqueId('switch-');
  },
};
</script>

<style lang="scss" scoped>
.email-subscription-tile {
  padding: 2.5rem 2rem 1.5rem;
  margin-bottom: 2rem;
  position: relative;
  background-color: #fff;

  @include media-breakpoint-up(lg) {
    padding: 2.5rem 4rem;
  }

  .left-col,
  .right-col {
    flex: 1 1 100%;
    max-width: initial;
    padding: 0;

    @include media-breakpoint-up(lg) {
      padding: 1rem 0;
      flex-basis: 0%;
    }
  }

  .left-col {
    padding-bottom: 1.75rem;
    margin-bottom: 1.5rem;
    border-bottom: 1px solid #686d6e;
    display: flex;
    flex-direction: column;

    @include media-breakpoint-up(lg) {
      padding: 1rem 0;
      border-bottom: 0;
      margin-bottom: 0;
      min-height: 250px;
    }

    .header {
      @include media-breakpoint-up(lg) {
        display: flex;
        margin: auto 0;
        align-items: center;
      }

      .icon {
        width: 6rem;
        height: 6rem;
        margin: 0 auto;
        margin-bottom: 1rem;

        @include media-breakpoint-up(lg) {
          margin: 0 1.5rem 0 0;
          flex: 0 0 6rem;
        }
      }

      h2 {
        font-size: 2.5rem;
        font-weight: 600;
        text-align: center;

        @include media-breakpoint-up(lg) {
          text-align: left;
        }
      }
    }
  }

  .right-col {
    @include media-breakpoint-up(lg) {
      border-left: 1px solid #686d6e;
      margin-left: 2rem;
      padding-left: 2rem;
    }

    .description {
      font-size: 1.15rem;
      font-weight: 300;
      line-height: 1.5;
      margin: 0;
    }
  }

  .switch-container {
    margin-top: 1rem;
    padding: 1rem;
    display: flex;
    margin-top: 1.5rem;

    @each $color-name, $color in $theme-colors {
      &--#{$color-name} {
        background-color: rgba($color, 0.15);
      }
    }

    .loader-container {
      flex: 1;
      height: 2rem;
      line-height: 2rem;

      .lds-dual-ring {
        &,
        &::after {
          width: 2rem;
          height: 2rem;
        }
      }
    }

    .text {
      flex: 1;
      line-height: 2rem;
      font-size: 1.5rem;
      font-weight: 600;
      font-style: italic;
    }

    .custom-switch {
      margin-right: -0.75rem;
      margin-bottom: 0;
    }
  }
}
</style>
