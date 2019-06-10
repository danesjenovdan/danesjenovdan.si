<template>
  <div class="checkout">
    <div v-if="error" class="alert alert-danger">{{ error }}</div>
    <div v-else-if="stage === 'summary'" class="checkout__summary">
      <h1 class="checkout__title">Povzetek naročila</h1>
      <template v-for="item in items">
        <!-- TODO: variant text -->
        <cart-product
          :key="`${item.id}`"
          :image="`/img/products/${item.article.id}.jpg`"
          :title="$te(`shop.products.${item.article.id}.display_name`) ? $t(`shop.products.${item.article.id}.display_name`) : item.article.name"
          text="TODO: variant text"
          :price="item.article.price"
          :amount="item.quantity"
        />
        <hr :key="`${item.id}-hr`">
      </template>
      <div class="cart-total">
        <span>Skupaj</span>
        <i>{{ totalPrice }} €</i>
      </div>
      <more-button
        key="next-summary"
        block
        color="secondary"
        icon="heart"
        :to="localePath('shop-checkout')"
        :text="'KUPI'"
        @click.native="continueToDelivery"
      />
    </div>
    <div v-else-if="stage === 'delivery'" class="checkout__delivery">
      <h1 class="checkout__title">Prevzem</h1>
      <form @submit.prevent="continueToPayment">
        <div class="custom-control custom-radio">
          <input
            id="delivery-pickup"
            v-model="delivery"
            type="radio"
            name="delivery"
            class="custom-control-input"
            value="pickup"
          >
          <label class="custom-control-label" for="delivery-pickup">Osebni prevzem</label>
        </div>
        <div class="custom-control custom-radio">
          <input
            id="delivery-post"
            v-model="delivery"
            type="radio"
            name="delivery"
            class="custom-control-input"
            value="post"
          >
          <label class="custom-control-label" for="delivery-post">Pošlji po pošti</label>
        </div>
        <template v-if="delivery">
          <div class="form-group">
            <input
              id="name"
              v-model="name"
              placeholder="Ime in priimek"
              class="form-control form-control-lg"
            >
          </div>
          <div class="form-group">
            <input
              id="email"
              v-model="email"
              type="email"
              placeholder="Email"
              class="form-control form-control-lg"
            >
          </div>
          <!-- TODO: preveri če rabimo naslov za izdajo računa tudi pri osebnem prevzemu? -->
          <template v-if="delivery === 'post'">
            <div class="form-group">
              <input
                id="address"
                v-model="address"
                placeholder="Naslov"
                class="form-control form-control-lg"
              >
            </div>
            <div class="form-group">
              <input
                id="address-post"
                v-model="addressPost"
                placeholder="Poštna številka in pošta"
                class="form-control form-control-lg"
              >
            </div>
          </template>
        </template>
        <!-- this is here so you can submit the form with the enter key -->
        <input type="submit" hidden>
      </form>
      <more-button
        key="next-delivery"
        block
        color="secondary"
        icon="heart"
        :to="localePath('shop-checkout')"
        :text="'KUPI'"
        :disabled="!canContinueToPayment || checkoutLoading"
        @click.native="continueToPayment"
      />
    </div>
    <div v-else-if="stage === 'payment'" class="checkout__payment">
      <h1 class="checkout__title">Plačilo</h1>
      <payment-switcher @change="onPaymentChange"/>
      <template v-if="payment === 'card'">
        <card-payment :token="token" @success="paymentSuccess"/>
      </template>
      <template v-if="payment === 'paypal'">
        <paypal-payment :token="token" :amount="totalPrice" @success="paymentSuccess"/>
      </template>
      <template v-if="payment === 'upn'">
        <upn-payment/>
      </template>
    </div>
    <div v-else-if="stage === 'thankyou'" class="checkout__thankyou">
      <div class="thankyou__content">
        <div>
          <div class="icon icon-confetti-popper--secondary"/>
        </div>
        <h1 class="checkout__title">Hvala!</h1>
        <div>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem vitae similique, ad quis iste veniam voluptates.</p>
        </div>
      </div>
      <div class="thankyou__close">
        <nuxt-link :to="localePath('shop')" class="close-button">ZAPRI</nuxt-link>
      </div>
    </div>
    <div v-if="stage !== 'thankyou'" class="terms">
      <nuxt-link to="#">Pogoji poslovanja</nuxt-link>
    </div>
  </div>
</template>

<script>
import MoreButton from '~/components/MoreButton.vue';
import CartProduct from '~/components/CartProduct.vue';
import PaymentSwitcher from '~/components/Payment/Switcher.vue';
import CardPayment from '~/components/Payment/Card.vue';
import PaypalPayment from '~/components/Payment/Paypal.vue';
import UpnPayment from '~/components/Payment/Upn.vue';

// https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email#Validation
const EMAIL_REGEX = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
const ADDRESS_POST_REGEX = /^\d{4}\s.+/;

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
    PaymentSwitcher,
    CardPayment,
    PaypalPayment,
    UpnPayment,
  },
  data() {
    return {
      stage: 'summary',
      delivery: null,
      name: null,
      email: null,
      address: null,
      addressPost: null,
      payment: null,
      orderKey: null,
      items: null,
      token: null,
      checkoutLoading: false,
      error: null,
    };
  },
  computed: {
    totalPrice() {
      if (!this.items || !this.items.length) {
        return 0;
      }
      return this.items.reduce((acc, cur) => acc + cur.quantity * cur.article.price, 0);
    },
    canContinueToPayment() {
      if (!this.delivery) {
        return false;
      }
      if (!this.name || !this.email) {
        return false;
      }
      if (!EMAIL_REGEX.test(this.email)) {
        return false;
      }
      if (this.delivery === 'post') {
        if (!this.address || !this.addressPost) {
          return false;
        }
        if (!ADDRESS_POST_REGEX.test(this.addressPost)) {
          return false;
        }
      }
      return true;
    },
  },
  async mounted() {
    if (typeof window !== 'undefined') {
      this.orderKey = await this.getOrderKey();
      this.items = await this.getBasketItems();
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
    continueToDelivery() {
      this.stage = 'delivery';
    },
    async continueToPayment() {
      // TODO: shake invalid/empty fields
      // TODO: check email and address fields with regex?
      if (!this.canContinueToPayment) {
        return;
      }

      this.checkoutLoading = true;
      const checkoutResponse = await this.$axios.$post(
        `https://podpri.djnd.si/api/shop/checkout/?order_key=${this.orderKey}`,
        {
          name: this.name,
          email: this.email,
          address: this.address || '',
          post: this.addressPost || '',
          delivery_method: this.delivery,
        },
      );
      this.token = checkoutResponse.token;
      this.checkoutLoading = false;

      this.stage = 'payment';
    },
    onPaymentChange(payment) {
      this.payment = payment;
    },
    async paymentSuccess({ nonce } = {}) {
      try {
        await this.$axios.$post(`https://podpri.djnd.si/api/shop/pay/?order_key=${this.orderKey}`, {
          payment_type: nonce ? 'braintree' : 'upn',
          nonce,
        });
        window.localStorage.setItem('order_key', null);
        this.stage = 'thankyou';
      } catch (error) {
        // eslint-disable-next-line no-console
        console.error(error);
        this.error = error;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.checkout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;

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

  .payment-switcher {
    margin-bottom: 2rem;
  }

  .checkout__thankyou {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    max-width: 250px;
    margin: 0 auto;

    .thankyou__content {
      display: flex;
      flex-direction: column;
      justify-content: center;
      flex: 1;

      .icon {
        margin: 0 auto;
        width: 120px;
        height: 120px;
      }

      h1 {
        text-transform: uppercase;
        margin-top: 1.5rem;
        margin-bottom: 2rem;
      }

      p {
        text-align: center;
        font-weight: 300;
        margin: 0 auto;
      }
    }

    .thankyou__close {
      margin-bottom: 3rem;

      .close-button {
        display: block;
        width: 100%;
        border: 1px solid $color-red;
        padding: 0.5rem 1.5rem;
        font-size: 1.2rem;
        font-style: italic;
        font-weight: 600;
        color: inherit;
        text-decoration: none;
        background: transparent;
        text-align: center;
      }
    }
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
