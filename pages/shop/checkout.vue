<template>
  <div class="checkout">
    <h1 class="checkout__title">Povzetek naročila</h1>
    <div v-if="stage === 'summary'" class="checkout__summary">
      <cart-product
        image="https://djnapi.djnd.si/media/images/infopush/salcka.png"
        title="Druga DJND majica"
        text="luna, velikost S"
        :price="25"
        :amount="1"
      />
      <hr>
      <cart-product
        image="https://djnapi.djnd.si/media/images/infopush/salcka.png"
        title="Druga DJND majica"
        :price="25"
        :amount="1"
      />
      <hr>
      <div class="cart-total">
        <span>Skupaj</span>
        <i>50 €</i>
      </div>
      <more-button
        block
        color="secondary"
        icon="heart"
        :to="localePath('shop-checkout')"
        :text="'KUPI'"
        @click.native="nextStep"
      />
    </div>
    <div class="terms">
      <nuxt-link to="#">Pogoji poslovanja</nuxt-link>
    </div>
  </div>
</template>

<script>
import MoreButton from '~/components/MoreButton.vue';
import CartProduct from '~/components/CartProduct.vue';

export default {
  nuxtI18n: {
    paths: {
      sl: '/trgovina/blagajna',
      en: '/shop/checkout',
    },
  },
  layout: 'checkout',
  components: {
    MoreButton,
    CartProduct,
  },
  data() {
    return {
      stage: 'summary',
    };
  },
  methods: {
    nextStep(event) {
      event.preventDefault();
      console.log(this.stage);
      if (this.stage === 'summary') {
        //
      }
    },
  },
};
</script>

<style lang="scss" scoped>
h1 {
  font-size: 1.85rem;
  text-align: center;
  font-weight: 600;
  margin: 3rem 0;
}

.cart-total {
  text-align: right;
  background-color: rgba($color-red, 0.15);
  padding: 0.5rem 1rem;
  margin-bottom: 1rem;

  i {
    font-weight: 600;
    font-size: 1.25rem;
    margin-left: 0.25rem;
  }
}

.terms {
  text-align: center;
  margin: 2.5rem 0 1rem;
  color: #333;

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
</style>
