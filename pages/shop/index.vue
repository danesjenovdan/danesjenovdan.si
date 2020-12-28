<template>
  <div>
    <page-title
      :title="$t('menu.shop')"
      :text="$t('shop.description')"
      color="secondary"
    />
    <shopping-cart-bar
      :order-key="orderKey"
      :items="basketItems"
      @change-amount="onChangeAmount"
    />
    <div class="product-tiles row">
      <div
        v-for="product in stockedProducts"
        :key="`${product.id}`"
        class="col-12 col-lg-6"
      >
        <product-tile
          :image="getDisplayImage(product)"
          :title="$t(`shop.products.${product.id}.title`)"
          :text="$t(`shop.products.${product.id}.short_description`)"
          :button-text="$t(`shop.products.${product.id}.button_text`)"
          :button-url="
            localePath({
              name: 'shop-id',
              params: {
                id: product.id,
                slug: slugify(getDisplayName(product)),
              },
            })
          "
          color="secondary"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { slugify } from '~/helpers/slugify.js';
import shopMixin from '~/mixins/shop.js';
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
  mixins: [shopMixin],
  async asyncData({ $axios }) {
    let products = await $axios.$get(
      'https://podpri.djnd.si/api/shop/products/',
    );
    products = products.sort((a, b) => b.id - a.id);
    return {
      products,
    };
  },
  data() {
    return {
      orderKey: null,
      basketItems: null,
    };
  },
  head() {
    return {
      title: this.$t('menu.shop'),
    };
  },
  computed: {
    stockedProducts() {
      return this.products.filter((p) => p.stock > 0);
    },
  },
  async mounted() {
    if (typeof window !== 'undefined') {
      this.orderKey = await this.getOrderKey();
      this.basketItems = await this.getBasketItems(this.orderKey);
    }
  },
  methods: {
    slugify,
    async onChangeAmount(itemId, newAmount) {
      await this.changeAmount(this.orderKey, itemId, newAmount);
      this.basketItems = await this.getBasketItems(this.orderKey);
    },
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
