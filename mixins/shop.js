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
    async getOrderKey() {
      const orderKey = window.localStorage.getItem('order_key') || null;
      if (!orderKey) {
        const newBasket = await this.$axios.$get('https://podpri.djnd.si/api/shop/basket/');
        window.localStorage.setItem('order_key', newBasket.order_key);
        return newBasket.order_key;
      }
      return orderKey;
    },
    async getBasketItems(orderKey) {
      const basketItems = await this.$axios.$get(
        `https://podpri.djnd.si/api/shop/items/?order_key=${orderKey}`,
      );
      return basketItems;
    },
    async addToBasket(orderKey, productId, amount = 1) {
      await this.$axios.$post(
        `https://podpri.djnd.si/api/shop/add_to_basket/?order_key=${orderKey}`,
        {
          product_id: productId,
          quantity: amount,
        },
      );
    },
    async changeAmount(orderKey, itemId, newAmount) {
      if (newAmount <= 0) {
        await this.$axios.$delete(
          `https://podpri.djnd.si/api/shop/items/${itemId}/?order_key=${orderKey}`,
        );
      } else {
        await this.$axios.$put(
          `https://podpri.djnd.si/api/shop/items/${itemId}/?order_key=${orderKey}`,
          {
            quantity: newAmount,
          },
        );
      }
    },
  },
};
