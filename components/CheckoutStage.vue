<template>
  <div
    :class="[
      'checkout-stage',
      `checkout-stage-${stage}`,
      { 'checkout-stage--no-header': noHeader },
    ]"
  >
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
  justify-content: center;

  &.checkout-stage-payment {
    .checkout-stage__content {
      max-width: 450px;
      margin: auto;
    }
  }

  &.checkout-stage-default {
    .checkout-stage__content {
      max-width: 500px;
      margin: auto;
    }
  }

  &.checkout-stage--no-header {
    .checkout-stage__header {
      display: none;
    }
  }

  .checkout-stage__content {
    // display: flex;
    // flex-direction: column;
    // flex: 1;
    margin-bottom: auto;

    @include media-breakpoint-up(md) {
      margin-bottom: 0;
      min-height: 32rem;
    }
  }

  .checkout-stage__header,
  .checkout-stage__footer {
    margin: 1.5rem 0;

    @include media-breakpoint-up(md) {
      margin: 2.25rem 0;
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
</style>
