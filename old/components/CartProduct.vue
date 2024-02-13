<template>
  <div :class="['cart-product', { 'cart-product--large': large }]">
    <div class="row">
      <div class="col-6 cart-product__image-col">
        <div class="embed-responsive embed-responsive-1by1">
          <div class="embed-responsive-item d-flex align-items-center">
            <div
              :style="{ 'background-image': `url('${image}')` }"
              class="background-image"
            />
          </div>
        </div>
      </div>
      <div class="col-6 cart-product__desc-col">
        <div class="cart-product__title" v-text="title" />
        <div class="cart-product__variant-price">
          <div v-if="text" class="cart-product__variant" v-text="text" />
          <div v-else class="cart-product__variant">&nbsp;</div>
          <div class="cart-product__price">
            <span v-if="!showModify">
              <strong>{{ amount }}</strong> &times;
            </span>
            <strong>{{ formatPrice(price) }}</strong>
          </div>
        </div>
        <div v-if="showModify" class="cart-product__modify">
          <button
            class="modify-amount modify-amount--minus"
            @click="$emit('change-amount', amount - 1)"
          >
            &ndash;
          </button>
          <span class="amount" v-text="amount" />
          <button
            class="modify-amount modify-amount--plus"
            @click="$emit('change-amount', amount + 1)"
          >
            +
          </button>
          <button
            class="remove-product icon icon-trash--secondary"
            @click="$emit('change-amount', 0)"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import shopMixin from '~/mixins/shop.js';

export default {
  mixins: [shopMixin],
  props: {
    image: {
      type: String,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    text: {
      type: String,
      default: '',
    },
    price: {
      type: [Number, String],
      required: true,
    },
    amount: {
      type: Number,
      required: true,
    },
    showModify: {
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
.cart-product {
  .cart-product__image-col {
    .background-image {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-size: cover;
      background-repeat: no-repeat;
      background-position: center;
    }
  }

  .cart-product__desc-col {
    display: flex;
    flex-direction: column;
    padding-left: 0;

    .cart-product__title {
      font-size: 1.25rem;
      font-weight: 600;
      line-height: 1.1;
    }

    .cart-product__variant-price {
      display: flex;
      margin-top: 0.75rem;
      margin-bottom: 1rem;

      .cart-product__variant {
        font-weight: 300;
        line-height: 1;
        margin-right: auto;
      }

      .cart-product__price {
        font-weight: 300;
        font-style: italic;
        line-height: 1;

        strong {
          font-weight: 600;
        }
      }
    }

    .cart-product__modify {
      margin-top: auto;
      display: flex;
      align-items: center;

      button {
        background-color: transparent;
        border: 0;
        height: 1.75rem;
        width: 1.75rem;
      }

      .remove-product {
        background-size: 1.25rem;
      }

      .modify-amount {
        font-weight: 700;
        color: $color-red;
        border: 1px solid $color-red;
        text-align: center;

        &.modify-amount--plus {
          margin-right: auto;
        }
      }

      .amount {
        display: inline-block;
        text-align: center;
        line-height: 1;
        padding: 0.125rem 0.75rem;
        font-weight: 600;
      }

      input[type='number']::-webkit-outer-spin-button,
      input[type='number']::-webkit-inner-spin-button {
        -webkit-appearance: none;
        margin: 0;
      }

      input[type='number'] {
        -moz-appearance: textfield;
      }
    }
  }

  &.cart-product--large {
    @include media-breakpoint-up(md) {
      .cart-product__image-col {
        flex-basis: 40%;
        max-width: 40%;
      }

      .cart-product__desc-col {
        flex-basis: 60%;
        max-width: 60%;

        .cart-product__title {
          font-size: 1.75rem;
        }

        .cart-product__variant {
          font-size: 1.75rem;
        }

        .cart-product__price {
          font-size: 1.75rem;
        }
      }
    }
  }
}
</style>
