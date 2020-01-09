<template>
  <div class="product">
    <div class="product__container">
      <h1 v-text="getDisplayName(product)" />
      <h2 class="price">{{ formatPrice(product.price) }}</h2>
      <template v-if="$te(`shop.products.${product.id}.images`)">
        <img
          v-for="img in $t(`shop.products.${product.id}.images`)"
          :key="img"
          :src="img"
        />
      </template>
      <template v-else>
        <img :src="`/img/products/${product.id}.jpg`" />
      </template>
      <p v-t="`shop.products.${product.id}.description`" />
      <hr />
      <!-- <div>TODO: variants</div> -->
      <div class="product__variant">
        <h3 class="variant__title">Količina</h3>
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
      <hr />
      <more-button
        :text="'KUPI'"
        block
        color="secondary"
        icon="heart"
        @click="addAndCheckout"
      />
      <div class="add-to-basket">
        <a href="#" @click.prevent="addAndBack">
          Dodaj v voziček in še malo pobrskaj po policah
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import MoreButton from '~/components/MoreButton.vue';
import shopMixin from '~/mixins/shop.js';

export default {
  nuxtI18n: {
    paths: {
      sl: '/trgovina/:id/:slug?',
      en: '/shop/:id/:slug?',
    },
  },
  layout: 'checkout',
  components: {
    MoreButton,
  },
  mixins: [shopMixin],
  async asyncData({ $axios, params }) {
    const products = await $axios.$get(
      'https://podpri.djnd.si/api/shop/products/',
    );
    return {
      product: products.find((p) => p.id === Number(params.id)),
      params,
    };
  },
  data() {
    return {
      orderKey: null,
      amount: 1,
    };
  },
  async mounted() {
    if (typeof window !== 'undefined') {
      this.orderKey = await this.getOrderKey();
    }
  },
  methods: {
    changeAmount(newAmount) {
      this.amount = newAmount;
      if (this.amount < 1) {
        this.amount = 1;
      }
    },
    async addAndCheckout() {
      if (this.amount > 0) {
        await this.addToBasket(this.orderKey, this.product.id, this.amount);
      }
      this.$router.push(this.localePath('shop-checkout'));
    },
    async addAndBack() {
      if (this.amount > 0) {
        await this.addToBasket(this.orderKey, this.product.id, this.amount);
      }
      this.$router.push(this.localePath('shop'));
    },
  },
};
</script>

<style lang="scss" scoped>
.product {
  .product__container {
    @include media-breakpoint-up(md) {
      max-width: 540px;
      margin: 0 auto;
    }

    h1 {
      margin: 3rem 0 1rem;
      text-align: center;
      font-size: 1.85rem;
      font-weight: 600;
    }

    h2 {
      margin: 1rem 0 2rem;
      text-align: center;
      font-size: 1.85rem;
      font-weight: 300;
      font-style: italic;
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

    p {
      font-size: 1.2rem;
      font-weight: 300;
      font-style: italic;
    }

    hr {
      border-top-color: #686d6e;
      margin-top: 1.75rem;
      margin-bottom: 1.75rem;
    }

    .product__variant {
      .variant__title {
        font-size: 1.25rem;
      }

      button {
        background-color: transparent;
        border: 0;
        height: 1.75rem;
        width: 1.75rem;
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

    .add-to-basket {
      margin: 2rem 0 1rem;
      color: #333;
      text-align: center;

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
