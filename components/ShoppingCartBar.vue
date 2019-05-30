<template>
  <div class="bg-white shopping-cart-bar">
    <div class="bar-container">
      <div v-click-outside="() => toggleCartPreview(null, false)" class="cart-preview-container">
        <button type="button" class="cart" @click="toggleCartPreview">
          <div class="icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="currentColor">
              <path
                d="M8.016 10a3 3 0 1 0 0 6h9.562l10.313 48.656c.408 1.832 1.608 3.356 3.125 3.344h50c1.585.022 3.043-1.415 3.043-3s-1.458-3.022-3.043-3H33.453l-1.28-6h52.843c1.343-.01 2.612-1.033 2.906-2.344l7-30c.39-1.74-1.122-3.643-2.906-3.656H24.578l-1.625-7.625c-.283-1.332-1.575-2.376-2.937-2.375zm17.812 16h62.407L82.64 50H30.922zm15.188 44c-5.487 0-10 4.513-10 10s4.513 10 10 10 10-4.513 10-10-4.513-10-10-10zm30 0c-5.487 0-10 4.513-10 10s4.513 10 10 10 10-4.513 10-10-4.513-10-10-10zm-30 6c2.245 0 4 1.755 4 4s-1.755 4-4 4-4-1.755-4-4 1.755-4 4-4zm30 0c2.245 0 4 1.755 4 4s-1.755 4-4 4-4-1.755-4-4 1.755-4 4-4z"
              ></path>
            </svg>
          </div>
          <div class="amount">2</div>
        </button>
        <div v-if="cartPreviewShown" class="cart-preview">
          <div class="arrow"/>
          <div class="cart-preview__content">
            <cart-product
              image="https://djnapi.djnd.si/media/images/infopush/salcka.png"
              title="Druga DJND majica"
              text="luna, velikost S"
            />
            <hr>
            <cart-product
              image="https://djnapi.djnd.si/media/images/infopush/salcka.png"
              title="Druga DJND majica"
            />
            <hr>
            <div class="cart-total">
              <span>Skupaj</span>
              <i>50 €</i>
            </div>
            <more-button block color="secondary" :to="'#'" :text="'Zaključi nakup'"/>
          </div>
        </div>
      </div>
      <div class="checkout">
        <more-button color="secondary" :to="'#'" :text="'Zaključi nakup'"/>
      </div>
    </div>
  </div>
</template>

<script>
import MoreButton from '~/components/MoreButton.vue';
import CartProduct from '~/components/CartProduct.vue';

export default {
  components: {
    MoreButton,
    CartProduct,
  },
  directives: {
    clickOutside: {
      bind(el, binding) {
        const handler = e => {
          if (!el.contains(e.target) && el !== e.target) {
            binding.value(e);
          }
        };
        el.vueClickOutside = handler;
        document.addEventListener('click', handler);
      },
      unbind(el) {
        document.removeEventListener('click', el.vueClickOutside);
        el.vueClickOutside = null;
      },
    },
  },
  data() {
    return {
      cartPreviewShown: false,
    };
  },
  methods: {
    toggleCartPreview(event, value = !this.cartPreviewShown) {
      if (this.cartPreviewShown !== value) {
        this.cartPreviewShown = value;
      }
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
        left: -40px;
        width: 320px;
        z-index: 10;

        .arrow {
          border: 14px solid transparent;
          border-bottom-color: #fff;
          border-top-width: 0;
          width: 0;
          height: 0;
          margin-left: 62px;
          position: relative;
          z-index: 11;
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
      margin-top: -0.2rem;
      margin-bottom: -0.2rem;

      .more-button {
        font-size: 1rem;
        padding: 0.2rem 1.5rem 0.2rem 0.75rem;
      }
    }
  }
}
</style>
