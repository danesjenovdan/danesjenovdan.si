<template>
  <div class="payment-switcher">
    <nav class="nav nav-pills justify-content-center">
      <div class="nav-item">
        <button
          v-t="'shop.checkout.card'"
          :class="['nav-link', { active: active === 'card' }]"
          type="button"
          @click="changeActive('card')"
        ></button>
      </div>
      <div class="nav-item">
        <button
          v-t="'shop.checkout.paypal'"
          :class="['nav-link', { active: active === 'paypal' }]"
          type="button"
          @click="changeActive('paypal')"
        ></button>
      </div>
      <div v-if="!recurring" class="nav-item">
        <button
          v-t="'shop.checkout.upn'"
          :class="['nav-link', { active: active === 'upn' }]"
          type="button"
          @click="changeActive('upn')"
        ></button>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  props: {
    recurring: {
      type: Boolean,
      default: false,
    },
  },
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
.payment-switcher {
  margin-bottom: 1.5rem;

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
}
</style>
