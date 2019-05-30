<template>
  <div class="cart-product">
    <div class="row">
      <div class="col-5">
        <div class="embed-responsive embed-responsive-1by1">
          <div class="embed-responsive-item d-flex align-items-center">
            <div class="background-image" :style="{'background-image': `url('${image}')`}"/>
          </div>
        </div>
      </div>
      <div class="col-7 cart-product__desc-col">
        <div class="cart-product__title" v-text="title"/>
        <div class="cart-product__price">25 €</div>
        <div v-if="text" class="cart-product__variation" v-text="text"/>
        <div v-else class="cart-product__variation">&nbsp;</div>
        <div class="cart-product__modify">
          <button class="remove-product icon icon-trash--secondary"/>
          <button class="modify-amount modify-amount--minus">&ndash;</button>
          <input type="number" min="1" class="amount form-control">
          <button class="modify-amount modify-amount--plus">+</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
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
      font-weight: 600;
      font-style: italic;
      line-height: 1;
      margin-top: 0.6rem;
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
      }

      .remove-product {
        width: 1.75rem;
        height: 1.75rem;
        background-size: 1.25rem;
      }

      .modify-amount {
        font-weight: 700;
        color: $color-red;
        width: 1.4em;

        &.modify-amount--minus {
          margin-left: 1rem;
        }
      }

      .amount {
        display: inline-block;
        width: 40px;
        text-align: center;
        line-height: 1;
        height: 1.75rem;
        padding: 0.125rem 0.5rem;
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
