<template>
  <div class="product">
    <div class="product__container">
      <h1 v-text="getDisplayName(product)" />
      <h2 class="price">{{ formatPrice(product.price) }} €</h2>
      <div>{{ product }}</div>
    </div>
  </div>
</template>

<script>
import productMixin from '~/mixins/product.js';

export default {
  nuxtI18n: {
    paths: {
      sl: '/trgovina/:id/:slug?',
      en: '/shop/:id/:slug?',
    },
  },
  layout: 'checkout',
  mixins: [productMixin],
  async asyncData({ $axios, params }) {
    const products = await $axios.$get('https://podpri.djnd.si/api/shop/products/');
    return {
      product: products.find(p => p.id === Number(params.id)),
      params,
    };
  },
};
</script>

<style lang="scss" scoped>
.product {
  h1 {
    font-size: 1.85rem;
    text-align: center;
    font-weight: 600;
    margin: 3rem 0;
  }
}
</style>
