<template>
  <div>
    <page-title :title="$t('menu.shop')" :text="$t('shop.description')" color="secondary"/>
    <shopping-cart-bar/>
    <div class="mt-4">
      <product-tile
        color="secondary"
        image="https://djnapi.djnd.si/media/images/infopush/salcka.png"
        title="tilte"
        text="text"
        url="http://google.com"
        button-text="Privošči si jo!"
        button-url="https://google.com"
      />
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
    return {};
  },
  head() {
    return {
      title: this.$t('menu.shop'),
    };
  },
};
</script>

<style lang="scss" scoped>
</style>
