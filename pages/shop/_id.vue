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
      <!-- <div>TODO: variants</div>
      <hr /> -->
      <more-button
        :text="'KUPI'"
        @click="addAndCheckout"
        block
        color="secondary"
        icon="heart"
      />
      <div class="add-to-basket">
        <nuxt-link to="#">
          Dodaj v voziček in še malo pobrskaj po policah
        </nuxt-link>
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
  data() {
    return {
      orderKey: null,
    };
  },
  async asyncData({ $axios, params }) {
    const products = await $axios.$get(
      'https://podpri.djnd.si/api/shop/products/',
    );
    return {
      product: products.find((p) => p.id === Number(params.id)),
      params,
    };
  },
  async mounted() {
    if (typeof window !== 'undefined') {
      this.orderKey = await this.getOrderKey();
    }
  },
  methods: {
    async addAndCheckout() {
      await this.addToBasket(this.orderKey, this.product.id, 1);
      this.$router.push(this.localePath('shop-checkout'));
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
