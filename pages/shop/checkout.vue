<template>
  <div class="checkout">
    <div v-if="stage === 'summary'" class="checkout__summary">
      <h1 class="checkout__title">Povzetek naročila</h1>
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
        key="next-summary"
        block
        color="secondary"
        icon="heart"
        :to="localePath('shop-checkout')"
        :text="'KUPI'"
        @click.native="continueToDelivery"
      />
    </div>
    <div v-if="stage === 'delivery'" class="checkout__delivery">
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
        :disabled="!canContinueToPayment"
        @click.native="continueToPayment"
      />
    </div>
    <div v-if="stage === 'payment'" class="checkout__payment">
      <h1 class="checkout__title">Plačilo</h1>
      <payment-switcher @change="onPaymentChange"/>
      <template v-if="payment === 'card'">
        <card-payment/>
      </template>
      <template v-if="payment === 'paypal'">
        <paypal-payment/>
      </template>
      <template v-if="payment === 'upn'">
        <upn-payment/>
      </template>
    </div>
    <div class="terms">
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
    };
  },
  computed: {
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
  methods: {
    continueToDelivery() {
      this.stage = 'delivery';
    },
    continueToPayment() {
      console.log('yo!');
      // TODO: shake invalid/empty fields
      // TODO: check email and address fields with regex?
      if (!this.canContinueToPayment) {
        return;
      }
      this.stage = 'payment';
    },
    onPaymentChange(payment) {
      this.payment = payment;
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
