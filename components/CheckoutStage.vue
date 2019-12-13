<template>
  <div class="checkout-stage">
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

<style lang="scss" scoped>
.checkout-stage {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;

  .checkout-stage__content {
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
