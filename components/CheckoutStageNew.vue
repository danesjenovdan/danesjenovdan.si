<template>
  <div
    :class="[
      'checkout-stage',
      `checkout-stage-${stage}`,
      { 'checkout-stage--no-header': noHeader },
    ]"
  >
    <div class="checkout-stage__container">
      <div class="checkout-stage__header">
        <slot name="header">
          <h1 class="checkout-stage__title">
            <slot name="title" />
          </h1>
        </slot>
      </div>
      <div class="checkout-stage__content">
        <slot name="content" />
      </div>
      <div class="checkout-stage__footer">
        <slot name="footer" />
      </div>
    </div>
    <div class="checkout-stage__terms">
      <nuxt-link
        v-t="'shop.terms'"
        target="_blank"
        :to="localePath('articles-terms')"
      ></nuxt-link>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    noHeader: {
      type: Boolean,
      default: false,
    },
    stage: {
      type: String,
      default: 'default',
    },
  },
};
</script>

<style lang="scss" scoped>
.checkout-stage {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  &.checkout-stage--no-header {
    .checkout-stage__header {
      display: none;
    }
  }

  .checkout-stage__container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    flex: 1;

    .checkout-stage__content {
      display: flex;
      flex-direction: column;
      // flex: 1;
      // margin-bottom: auto;
      min-height: 21rem;

      @include media-breakpoint-up(md) {
        // margin-bottom: 0;
      }
    }

    .checkout-stage__header,
    .checkout-stage__footer {
      margin: 1.5rem 0;

      @include media-breakpoint-up(md) {
        margin: 2rem 0;
      }

      &:empty {
        display: none;
      }
    }

    .checkout-stage__header {
      .checkout-stage__title {
        margin: 0;
        font-size: 1.75rem;
        text-align: center;
        font-weight: 600;

        @include media-breakpoint-up(md) {
          font-size: 3rem;
        }
      }
    }
  }

  .checkout-stage__terms {
    margin-bottom: 1rem;
    text-align: center;

    a {
      color: inherit;
      font-size: 1rem;
      font-weight: 300;
      font-style: italic;
      text-decoration: underline;

      @include media-breakpoint-up(md) {
        font-size: 1.25rem;
      }

      &:hover {
        text-decoration: none;
      }
    }
  }
}
.hudapobuda {
  h1 {
    font-family: $font-family-okolaks;
  }
  p,
  a {
    font-family: $font-family-comfortaa;
  }
}
</style>
