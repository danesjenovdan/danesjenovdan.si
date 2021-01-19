<template>
  <div class="product">
    <div class="product__container row no-gutters">
      <div class="d-none d-md-block col-md-4">&nbsp;</div>
      <div class="col-12 col-md-8 product__name">
        <h1 v-t="`shop.products.${product.id}.title`" />
        <h2 class="price">{{ formatPrice(product.price) }}</h2>
      </div>
      <div class="col-12 col-md-4 product__images">
        <img v-for="img in getDisplayImages(product)" :key="img" :src="img" />
      </div>
      <div class="col-12 col-md-8 product__description">
        <p v-html="$t(`shop.products.${product.id}.description`)" />
        <hr />
        <div
          v-if="product.variants && product.variants.length"
          class="product__variant row"
        >
          <div class="col-12 col-md-3">
            <span class="variant__title">Velikost</span>
          </div>
          <div class="col d-flex align-items-center">
            <button
              v-for="v in sortedVariants"
              :key="v.id"
              :class="[
                'modify-variant',
                { active: variant && variant.id === v.id },
              ]"
              :disabled="v.stock <= 0"
              @click="changeVariant(v)"
            >
              {{ v.variant }}
            </button>
          </div>
        </div>
        <div class="product__variant row">
          <div class="col-12 col-md-3">
            <span v-t="'shop.quantity'" class="variant__title"></span>
          </div>
          <div class="col d-flex align-items-center">
            <button
              class="modify-amount modify-amount--minus"
              @click="changeAmount(amount - 1)"
            >
              &ndash;
            </button>
            <span class="amount" v-text="amount" />
            <button
              class="modify-amount modify-amount--plus"
              @click="changeAmount(amount + 1)"
            >
              +
            </button>
          </div>
        </div>
        <hr />
        <div class="row">
          <div class="col-12 col-lg-6">
            <more-button
              :text="$t('shop.buy')"
              block
              color="secondary"
              icon="heart"
              large
              :disabled="!variant"
              @click="addAndCheckout"
            />
          </div>
          <div class="col-12 col-lg-6 d-flex align-items-center">
            <div class="add-to-basket">
              <a href="#" @click.prevent="addAndBack">
                {{ $t('shop.addToCart') }}
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MoreButton from '~/components/MoreButton.vue';
import shopMixin from '~/mixins/shop.js';
import { catchError } from '~/helpers/async.js';

export default {
  pageColor: 'secondary',
  nuxtI18n: {
    paths: {
      sl: '/trgovina/:id/:slug?',
      en: '/shop/:id/:slug?',
    },
  },
  components: {
    MoreButton,
  },
  mixins: [shopMixin],
  layout: 'checkout',
  asyncData: catchError(async ({ $axios, params }) => {
    const product = await $axios.$get(
      `https://podpri.djnd.si/api/shop/products/${params.id}/`,
    );
    return {
      product,
      variant: product.variants && product.variants.length ? null : product,
    };
  }),
  data() {
    return {
      orderKey: null,
      amount: 1,
    };
  },
  computed: {
    sortedVariants() {
      const sizes = ['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL'];
      const variants = this.product.variants.slice() || [];
      return variants.sort((a, b) => {
        return (
          sizes.indexOf(a.variant.toUpperCase()) -
          sizes.indexOf(b.variant.toUpperCase())
        );
      });
    },
  },
  async mounted() {
    if (typeof window !== 'undefined') {
      this.orderKey = await this.getOrderKey();
    }
    if (!this.variant && this.sortedVariants.length) {
      this.variant = this.sortedVariants.find((v) => v.stock > 0);
    }
  },
  methods: {
    changeAmount(newAmount) {
      this.amount = newAmount;
      if (this.amount < 1) {
        this.amount = 1;
      }
      this.amount = Math.min(this.amount, this.variant.stock);
    },
    changeVariant(newVariant) {
      if (newVariant.stock > 0) {
        this.variant = newVariant;
        this.amount = Math.min(this.amount, this.variant.stock);
      }
    },
    async addAndCheckout() {
      if (this.variant) {
        if (this.amount > 0) {
          await this.addToBasket(this.orderKey, this.variant.id, this.amount);
        }
        this.$router.push(this.localePath('shop-checkout'));
      }
    },
    async addAndBack() {
      if (this.variant) {
        if (this.amount > 0) {
          await this.addToBasket(this.orderKey, this.variant.id, this.amount);
        }
        this.$router.push(this.localePath('shop'));
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.product {
  .product__container {
    @include media-breakpoint-up(md) {
      max-width: 960px;
      margin: 0 auto;
    }

    h1 {
      margin: 3rem 0 1rem;
      text-align: center;
      font-size: 1.85rem;
      font-weight: 600;

      @include media-breakpoint-up(md) {
        margin-bottom: 0;
        text-align: left;
        font-size: 2.5rem;
      }
    }

    h2 {
      margin: 1rem 0 2rem;
      text-align: center;
      font-size: 1.85rem;
      font-weight: 300;
      font-style: italic;

      @include media-breakpoint-up(md) {
        margin-top: 0;
        margin-bottom: 0;
        text-align: left;
        font-size: 2.5rem;
      }
    }

    img {
      width: 100%;
      max-width: 100%;
      margin-bottom: 2rem;

      @include media-breakpoint-up(md) {
        display: block;
        max-width: 370px;
        margin-left: auto;
        margin-right: auto;
      }
    }

    .product__name {
      @include media-breakpoint-up(md) {
        margin-left: -1.8rem;
        padding: 0 1.8rem 0 3.8rem;
      }
    }

    .product__images {
      @include media-breakpoint-up(md) {
        z-index: 1;
      }
    }

    .product__description {
      @include media-breakpoint-up(md) {
        margin-left: -1.8rem;
        margin-right: 0rem;
        margin-top: 1.8rem;
        padding: 1.8rem 2.3rem 1.8rem;
        padding-left: 3.8rem;
        background-color: #fff;
        z-index: 0;
      }
    }

    p {
      font-size: 1.2rem;
      font-weight: 300;
      line-height: 1.4;
      font-style: italic;

      @include media-breakpoint-up(md) {
        font-size: 1.5rem;
      }
    }

    hr {
      border-top-color: #686d6e;
      margin-top: 1.75rem;
      margin-bottom: 1.75rem;
    }

    .product__variant {
      margin-bottom: 1rem;

      .variant__title {
        display: inline-block;
        margin-bottom: 0.25rem;
        font-size: 1.25rem;
        font-weight: 600;

        @include media-breakpoint-up(md) {
          font-size: 1.5rem;
          margin-bottom: 0;
          margin-right: 1rem;
        }
      }

      button {
        background-color: transparent;
        border: 0;
        height: 1.75rem;
        width: 1.75rem;
        outline: none;
      }

      .modify-amount {
        font-weight: 700;
        color: $color-red;
        border: 1px solid $color-red;
        text-align: center;
      }

      .amount {
        display: inline-block;
        text-align: center;
        line-height: 1;
        padding: 0.125rem 0.75rem;
        font-weight: 600;
        min-width: 2.75rem;
      }

      input[type='number']::-webkit-outer-spin-button,
      input[type='number']::-webkit-inner-spin-button {
        -webkit-appearance: none;
        margin: 0;
      }

      input[type='number'] {
        -moz-appearance: textfield;
      }

      .modify-variant {
        margin-right: 0.5rem;
        border: 1px solid $color-red;
        border-radius: 50%;
        padding: 0.25rem;
        height: 2.25rem;
        width: 2.25rem;

        &.active {
          background-color: $color-red;
        }

        &.disabled,
        &[disabled] {
          filter: grayscale(1);
          cursor: not-allowed;
        }
      }
    }

    .add-to-basket {
      margin: 1.5rem 0;
      color: #333;

      @include media-breakpoint-up(lg) {
        margin: 0;
      }

      a {
        text-decoration: underline;
        color: inherit;
        font-style: italic;
        font-weight: 300;

        &:hover {
          text-decoration: none;
        }
      }
    }
  }
}
</style>

<style lang="scss">
.product__description {
  a {
    color: $secondary;
  }
}
</style>
