<template>
  <div v-show="itemAmount > 0" class="bg-white shopping-cart-bar">
    <div class="bar-container">
      <div
        v-click-outside="() => toggleCartPreview(null, false)"
        class="cart-preview-container"
      >
        <button type="button" class="cart" @click="toggleCartPreview">
          <div class="icon">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 100 100"
              fill="currentColor"
            >
              <path
                d="M8.016 10a3 3 0 1 0 0 6h9.562l10.313 48.656c.408 1.832 1.608 3.356 3.125 3.344h50c1.585.022 3.043-1.415 3.043-3s-1.458-3.022-3.043-3H33.453l-1.28-6h52.843c1.343-.01 2.612-1.033 2.906-2.344l7-30c.39-1.74-1.122-3.643-2.906-3.656H24.578l-1.625-7.625c-.283-1.332-1.575-2.376-2.937-2.375zm17.812 16h62.407L82.64 50H30.922zm15.188 44c-5.487 0-10 4.513-10 10s4.513 10 10 10 10-4.513 10-10-4.513-10-10-10zm30 0c-5.487 0-10 4.513-10 10s4.513 10 10 10 10-4.513 10-10-4.513-10-10-10zm-30 6c2.245 0 4 1.755 4 4s-1.755 4-4 4-4-1.755-4-4 1.755-4 4-4zm30 0c2.245 0 4 1.755 4 4s-1.755 4-4 4-4-1.755-4-4 1.755-4 4-4z"
              />
            </svg>
          </div>
          <div class="amount" v-text="itemAmount" />
        </button>
        <div v-if="cartPreviewShown" class="cart-preview">
          <div class="arrow" />
          <div class="cart-preview__content">
            <template v-for="item in items">
              <cart-product
                :key="item.id"
                :image="getDisplayImage(item.article)"
                :title="getDisplayName(item.article)"
                :price="item.article.price"
                :amount="item.quantity"
                :text="item.article.variant || ''"
                show-modify
                @change-amount="changeAmount(item.id, $event)"
              />
              <hr :key="`${item.id}-hr`" />
            </template>
            <div class="cart-total">
              <span>Skupaj</span>
              <i>{{ totalPrice }} €</i>
            </div>
            <more-button
              :to="localePath('shop-checkout')"
              :text="'Zaključi nakup'"
              block
              color="secondary"
            />
          </div>
        </div>
      </div>
      <div class="checkout">
        <more-button
          :to="localePath('shop-checkout')"
          :text="'Zaključi nakup'"
          small
          color="secondary"
        />
      </div>
    </div>
  </div>
</template>

<script>
import MoreButton from '~/components/MoreButton.vue';
import CartProduct from '~/components/CartProduct.vue';
import clickOutside from '~/mixins/clickOutside.js';
import shopMixin from '~/mixins/shop.js';

export default {
  components: {
    MoreButton,
    CartProduct,
  },
  mixins: [clickOutside, shopMixin],
  props: {
    orderKey: {
      type: String,
      default: null,
    },
    items: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      cartPreviewShown: false,
    };
  },
  computed: {
    itemAmount() {
      if (!this.items || !this.items.length) {
        return 0;
      }
      return this.items.reduce((acc, cur) => acc + cur.quantity, 0);
    },
    totalPrice() {
      if (!this.items || !this.items.length) {
        return 0;
      }
      return this.items.reduce(
        (acc, cur) => acc + cur.quantity * cur.article.price,
        0,
      );
    },
  },
  methods: {
    toggleCartPreview(event, value = !this.cartPreviewShown) {
      if (this.cartPreviewShown !== value) {
        this.cartPreviewShown = value;
      }
    },
    changeAmount(itemId, newAmount) {
      this.$emit('change-amount', itemId, newAmount);
    },
  },
};
</script>

<style lang="scss" scoped>
.shopping-cart-bar {
  margin-left: -$content-mobile-padding;
  margin-right: -$content-mobile-padding;
  padding-left: $content-mobile-padding;
  padding-right: $content-mobile-padding;
  position: relative;
  height: 3.2rem;

  @include media-breakpoint-up(md) {
    margin-left: 0;
    margin-right: 0;
    padding-left: 1rem;
    padding-right: 1rem;
  }

  .bar-container {
    display: flex;
    justify-content: space-between;
    padding: 0.8rem 0;

    @include media-breakpoint-up(md) {
      justify-content: flex-end;
    }

    .cart-preview-container {
      position: relative;

      .cart {
        display: flex;
        background-color: transparent;
        border: none;
        padding: 0.25rem 0.25rem;
        margin: -0.25rem 1.5rem -0.25rem 0;

        .icon {
          width: 2rem;
          height: 2rem;
          margin-top: -0.2rem;
          margin-bottom: -0.2rem;
          display: flex;
          align-items: center;
          flex-shrink: 0;
          color: $color-red;

          svg {
            width: 100%;
            height: 100%;
          }
        }

        .amount {
          margin: 0 0.5rem 0 0.75rem;
          font-weight: 600;
          font-size: 1.15rem;
          line-height: 1.2;
        }
      }

      .cart-preview {
        position: absolute;
        top: 2.7rem;
        left: 0;
        width: calc(100vw - #{$content-mobile-padding * 2});
        z-index: 10;

        @include media-breakpoint-up(md) {
          left: -40px;
          width: 320px;
        }

        .arrow {
          border: 14px solid transparent;
          border-bottom-color: #fff;
          border-top-width: 0;
          width: 0;
          height: 0;
          margin-left: 28px;
          position: relative;
          z-index: 11;

          @include media-breakpoint-up(md) {
            margin-left: 62px;
          }
        }

        .cart-preview__content {
          background-color: #fff;
          padding: 1.5rem;
          box-shadow: $box-shadow;

          .cart-total {
            text-align: right;
            background-color: rgba($color-red, 0.15);
            padding: 0.5rem 1rem;
            margin-bottom: 1rem;

            i {
              font-weight: 600;
              font-size: 1.25rem;
              margin-left: 0.25rem;
            }
          }
        }
      }
    }

    .checkout {
      margin-top: -0.35rem;
      margin-bottom: -0.35rem;
    }
  }
}
</style>
