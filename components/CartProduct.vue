<template>
  <div class="cart-product">
    <div class="row">
      <div class="col-5">
        <div class="embed-responsive embed-responsive-1by1">
          <div class="embed-responsive-item d-flex align-items-center">
            <div
              :style="{ 'background-image': `url('${image}')` }"
              class="background-image"
            />
          </div>
        </div>
      </div>
      <div class="col-7 cart-product__desc-col">
        <div v-text="title" class="cart-product__title" />
        <div class="cart-product__price">
          <span v-if="!showModify">
            <strong>{{ amount }}</strong> &times;
          </span>
          <strong>{{ formatPrice(price) }}</strong>
        </div>
        <div v-if="text" v-text="text" class="cart-product__variation" />
        <div v-else class="cart-product__variation">&nbsp;</div>
        <div v-if="showModify" class="cart-product__modify">
          <button
            @click="$emit('change-amount', 0)"
            class="remove-product icon icon-trash--secondary"
          />
          <button
            @click="$emit('change-amount', amount - 1)"
            class="modify-amount modify-amount--minus"
          >
            &ndash;
          </button>
          <span v-text="amount" class="amount" />
          <button
            @click="$emit('change-amount', amount + 1)"
            class="modify-amount modify-amount--plus"
          >
            +
          </button>
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
  },
};
</script>

<style lang="scss" scoped>
.cart-product {
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

  .cart-product__desc-col {
    padding-left: 0;

    .cart-product__title {
      font-size: 1.25rem;
      font-weight: 600;
      line-height: 1.1;
    }

    .cart-product__price {
      font-weight: 300;
      font-style: italic;
      line-height: 1;
      margin-top: 0.6rem;

      strong {
        font-weight: 600;
      }
    }

    .cart-product__variation {
      font-weight: 300;
      line-height: 1;
      margin-top: 0.75rem;
    }

    .cart-product__modify {
      margin-top: 1rem;
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

        &.modify-amount--minus {
          margin-left: 1.5rem;
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
}
</style>
