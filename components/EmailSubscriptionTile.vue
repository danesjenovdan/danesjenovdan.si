<template>
  <div :class="['email-subscription-tile', `section--${color}`]">
    <div class="row">
      <div class="left-col">
        <div :class="['icon', `icon-sub-${icon}`]" />
        <h2>{{ title }}</h2>
      </div>
      <div class="right-col">
        <p>{{ description }}</p>
        <div :class="['switch-container', `switch-container--${color}`]">
          <div v-if="loading" class="loader-container">
            <div class="lds-dual-ring" />
          </div>
          <div v-else class="text">{{ checked ? labelOn : labelOff }}</div>
          <div class="custom-control custom-switch">
            <input
              :id="uid"
              type="checkbox"
              class="custom-control-input"
              :checked="checked"
              @change="$emit('change', $event.target.checked)"
            />
            <label :for="uid" class="custom-control-label" />
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
      uid: null,
    };
  },
  mounted() {
    // for some reason ssr breaks this, so we do it in "mounted"
    this.uid = uniqueId('switch-');
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
      padding: 1.5rem 0;
    }

    @include media-breakpoint-up(xxl) {
      flex-basis: 0%;
    }
  }

  .left-col {
    padding-bottom: 1.75rem;
    margin-bottom: 1.5rem;
    border-bottom: 1px solid #686d6e;

    .icon {
      width: 7rem;
      height: 7rem;
      margin: 0 auto;
      margin-bottom: 1rem;
    }

    h2 {
      font-size: 2.5rem;
      font-weight: 600;
      text-align: center;
    }
  }

  .right-col {
    p {
      font-size: 1.15rem;
      font-weight: 300;
      line-height: 1.5;
    }

    .switch-container {
      margin-top: 1.5rem;
      padding: 1rem;
      display: flex;

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
}
</style>
