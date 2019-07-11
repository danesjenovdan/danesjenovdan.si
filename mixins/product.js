export default {
  methods: {
    formatPrice(price) {
      return `${parseInt(price, 10)} €`;
    },
    getDisplayName(product) {
      return this.$te(`shop.products.${product.id}.display_name`)
        ? this.$t(`shop.products.${product.id}.display_name`)
        : product.name;
    },
  },
};
