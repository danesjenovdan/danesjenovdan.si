<template>
  <div>
    <page-title :title="$t('menu.shop')" :text="$t('shop.description')" color="secondary"/>
    <shopping-cart-bar :order-key="orderKey" :items="basketItems" @change-amount="changeAmount"/>
    <div class="product-tiles row">
      <div v-for="product in products" :key="`${product.id}`" class="col-12 col-lg-6">
        <product-tile
          color="secondary"
          :image="`/img/products/${product.id}.jpg`"
          :title="$te(`shop.products.${product.id}.display_name`) ? $t(`shop.products.${product.id}.display_name`) : product.name"
          :text="$t(`shop.products.${product.id}.short_description`)"
          :button-text="$t(`shop.products.${product.id}.button_text`)"
          :button-url="localePath({ name: 'shop-id', params: { id: product.id } })"
          @click.native="addToBasket($event, product.id)"
        />
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';
import ShoppingCartBar from '~/components/ShoppingCartBar.vue';
import ProductTile from '~/components/ProductTile.vue';

export default {
  pageColor: 'secondary',
  nuxtI18n: {
    paths: {
      sl: '/trgovina',
      en: '/shop',
    },
  },
  components: {
    PageTitle,
    ShoppingCartBar,
    ProductTile,
  },
  data() {
    return {
      orderKey: null,
      basketItems: null,
    };
  },
  async asyncData({ $axios }) {
    const products = await $axios.$get('https://podpri.djnd.si/api/shop/products/');
    return {
      products,
    };
  },
  async mounted() {
    if (typeof window !== 'undefined') {
      this.orderKey = await this.getOrderKey();
      this.basketItems = await this.getBasketItems();
    }
  },
  methods: {
    async getOrderKey() {
      const orderKey = window.localStorage.getItem('order_key') || null;
      if (!orderKey) {
        const newBasket = await this.$axios.$get('https://podpri.djnd.si/api/shop/basket/');
        window.localStorage.setItem('order_key', newBasket.order_key);
        return newBasket.order_key;
      }
      return orderKey;
    },
    async getBasketItems() {
      const basketItems = await this.$axios.$get(
        `https://podpri.djnd.si/api/shop/items/?order_key=${this.orderKey}`,
      );
      return basketItems;
    },
    async addToBasket(event, productId) {
      event.preventDefault();
      await this.$axios.$post(
        `https://podpri.djnd.si/api/shop/add_to_basket/?order_key=${this.orderKey}`,
        {
          product_id: productId,
          quantity: 1,
        },
      );
    },
    async changeAmount(itemId, newAmount) {
      if (newAmount <= 0) {
        await this.$axios.$delete(
          `https://podpri.djnd.si/api/shop/items/${itemId}/?order_key=${this.orderKey}`,
        );
      } else {
        await this.$axios.$put(
          `https://podpri.djnd.si/api/shop/items/${itemId}/?order_key=${this.orderKey}`,
          {
            quantity: newAmount,
          },
        );
      }
      this.basketItems = await this.getBasketItems();
    },
  },
  head() {
    return {
      title: this.$t('menu.shop'),
    };
  },
};
</script>

<style lang="scss" scoped>
.product-tiles {
  margin-top: 2rem;

  .product-tile {
    margin-bottom: 2rem;
  }
}
</style>
