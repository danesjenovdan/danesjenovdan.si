<template>
  <div class="product">
    <div class="product__container">
      <h1 v-text="$te(`shop.products.${product.id}.display_name`) ? $t(`shop.products.${product.id}.display_name`) : product.name"/>
      <div>{{ product }}</div>
    </div>
  </div>
</template>

<script>
export default {
  nuxtI18n: {
    paths: {
      sl: '/trgovina/:id/:slug?',
      en: '/shop/:id/:slug?',
    },
  },
  layout: 'checkout',
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
