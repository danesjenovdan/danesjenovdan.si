<template>
  <div class="payment-switcher">
    <nav class="nav nav-pills justify-content-center">
      <div class="nav-item">
        <button
          type="button"
          :class="['nav-link', { active: active === 'card' }]"
          @click="changeActive('card')"
        >Kartica</button>
      </div>
      <div class="nav-item">
        <button
          type="button"
          :class="['nav-link', { active: active === 'paypal' }]"
          @click="changeActive('paypal')"
        >PayPal</button>
      </div>
      <div class="nav-item">
        <button
          type="button"
          :class="['nav-link', { active: active === 'upn' }]"
          @click="changeActive('upn')"
        >Položnica</button>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  data() {
    return {
      active: 'card',
    };
  },
  mounted() {
    this.$emit('change', this.active);
  },
  methods: {
    changeActive(newActive) {
      this.active = newActive;
      this.$emit('change', newActive);
    },
  },
};
</script>

<style lang="scss" scoped>
.nav {
  margin: 0 #{-$content-mobile-padding};

  .nav-item {
    position: relative;
    margin: 0 0.5rem;

    &:not(:first-child)::before {
      content: '';
      background-color: #333;
      display: block;
      width: 1px;
      position: absolute;
      top: -0.25rem;
      bottom: -0.25rem;
      left: -0.5rem;
    }

    .nav-link {
      border-radius: 4px;
      border: 0;
      background: transparent;
      color: #333;
      text-transform: uppercase;
      font-weight: 300;

      &.active {
        background-color: rgba($color-red, 0.3);
      }

      &:focus {
        box-shadow: none;
      }
    }
  }
}
</style>
