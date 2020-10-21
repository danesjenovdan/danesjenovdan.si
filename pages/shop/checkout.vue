<template>
  <div class="checkout">
    <div v-if="error" class="alert alert-danger text-center mt-2">
      <p>
        Zgodila se je napaka, ki je naš strežnik ni mogel rešiti.<br />
        Zaračunali ti nismo ničesar, ves denar je še vedno na tvoji kartici.
        Predlagamo, da osvežiš stran in poskusiš ponovno. Če ne bo šlo, nam piši
        na
        <a href="mailto:vsi@danesjenovdan.si" class="text-danger"
          >vsi@danesjenovdan.si</a
        >
        in ti bomo poskusili pomagati.
      </p>
      <p class="small font-weight-bold mb-0">
        Error: {{ error.status || error.code }} ({{
          error.message || (error.data && error.data.msg)
        }})
      </p>
    </div>

    <template v-else-if="stage === 'summary'">
      <div class="checkout__summary">
        <checkout-stage>
          <template slot="title">
            Povzetek naročila
          </template>
          <template slot="content">
            <template v-if="summaryLoading">
              <div class="loader-container">
                <div class="lds-dual-ring" />
              </div>
            </template>
            <template v-else-if="items && items.length">
              <div class="cart-items">
                <template v-for="(item, i) in items">
                  <cart-product
                    :key="item.id"
                    :image="getDisplayImage(item.article)"
                    :title="getDisplayName(item.article)"
                    :price="item.article.price"
                    :amount="item.quantity"
                    :text="item.article.variant || ''"
                    show-modify
                    large
                    @change-amount="onChangeAmount(item.id, $event)"
                  />
                  <hr v-if="i !== items.length - 1" :key="`${item.id}-hr`" />
                </template>
              </div>
              <div class="cart-total">
                <span>Znesek za plačilo</span>
                <i>{{ totalPrice }} €</i>
              </div>
            </template>
          </template>
          <template slot="footer">
            <div class="confirm-button-container">
              <confirm-button
                key="next-summary"
                :disabled="!canContinueToNextStage"
                text="Kupi"
                color="secondary"
                arrow
                hearts
                block
                @click.native="continueToNextStage"
              />
            </div>
          </template>
        </checkout-stage>
      </div>
    </template>

    <checkout-stage v-else-if="stage === 'delivery'">
      <template slot="title">
        Prevzem
      </template>
      <template slot="content">
        <div class="checkout__summary">
          <form @submit.prevent="continueToPayment">
            <div class="custom-control custom-radio">
              <input
                id="delivery-pickup"
                v-model="delivery"
                type="radio"
                name="delivery"
                class="custom-control-input"
                value="pickup"
              />
              <label class="custom-control-label" for="delivery-pickup"
                >Osebni prevzem</label
              >
            </div>
            <div class="custom-control custom-radio">
              <input
                id="delivery-post"
                v-model="delivery"
                type="radio"
                name="delivery"
                class="custom-control-input"
                value="post"
              />
              <label class="custom-control-label" for="delivery-post"
                >Pošlji po pošti</label
              >
            </div>
            <template v-if="delivery">
              <div class="form-group">
                <input
                  id="name"
                  v-model="name"
                  placeholder="Ime in priimek"
                  class="form-control form-control-lg"
                />
              </div>
              <div class="form-group">
                <input
                  id="email"
                  v-model="email"
                  type="email"
                  placeholder="Email"
                  class="form-control form-control-lg"
                />
              </div>
              <!-- TODO: preveri če rabimo naslov za izdajo računa tudi pri osebnem prevzemu? -->
              <template v-if="delivery === 'post'">
                <div class="form-group">
                  <input
                    id="address"
                    v-model="address"
                    placeholder="Naslov"
                    class="form-control form-control-lg"
                  />
                </div>
                <div class="form-group">
                  <input
                    id="address-post"
                    v-model="addressPost"
                    placeholder="Poštna številka in pošta"
                    class="form-control form-control-lg"
                  />
                </div>
              </template>
            </template>
            <!-- this is here so you can submit the form with the enter key -->
            <input type="submit" hidden />
          </form>
        </div>
      </template>
      <template slot="footer">
        <div class="confirm-button-container">
          <confirm-button
            key="next-delivery"
            :disabled="!canContinueToPayment"
            :loading="checkoutLoading"
            text="Kupi"
            color="secondary"
            arrow
            @click.native="continueToPayment"
          />
        </div>
      </template>
    </checkout-stage>

    <checkout-stage v-if="stage === 'payment'">
      <template slot="title">
        Plačilo
      </template>
      <template slot="content">
        <div class="payment-container">
          <payment-switcher @change="onPaymentChange" />
          <div v-if="checkoutLoading" class="payment-loader">
            <div class="lds-dual-ring" />
          </div>
          <template v-if="payment === 'card'">
            <div :class="['payment', { 'payment--loading': checkoutLoading }]">
              <card-payment
                :token="token"
                @ready="onPaymentReady"
                @error="onPaymentError"
                @validity-change="paymentInfoValid = $event"
                @payment-start="paymentInProgress = true"
                @success="paymentSuccess"
              />
            </div>
          </template>
          <template v-if="payment === 'paypal'">
            <div :class="['payment', { 'payment--loading': checkoutLoading }]">
              <paypal-payment
                :token="token"
                :amount="totalPrice"
                @ready="onPaymentReady"
                @error="onPaymentError"
                @payment-start="paymentInProgress = true"
                @success="paymentSuccess"
              />
            </div>
          </template>
          <template v-if="payment === 'upn'">
            <upn-payment
              :amount="totalPrice"
              @ready="onPaymentReady"
              @success="paymentSuccess"
            />
          </template>
        </div>
      </template>
      <template slot="footer">
        <div class="confirm-button-container">
          <confirm-button
            key="next-payment"
            :disabled="!canContinueToNextStage"
            :loading="paymentInProgress"
            text="Plačaj"
            color="secondary"
            arrow
            hearts
            @click.native="continueToNextStage"
          />
        </div>
      </template>
    </checkout-stage>

    <div v-else-if="stage === 'thankyou'" class="checkout__thankyou">
      <div class="thankyou__content">
        <h1>
          Hvala!
        </h1>
        <div>
          <div class="icon icon-confetti-popper--secondary" />
        </div>
        <div>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem vitae
            similique, ad quis iste veniam voluptates.
          </p>
        </div>
        <div class="thankyou__close">
          <nuxt-link :to="localePath('shop')" class="close-button"
            >ZAPRI</nuxt-link
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import shopMixin from '~/mixins/shop.js';
import CartProduct from '~/components/CartProduct.vue';
import PaymentSwitcher from '~/components/Payment/Switcher.vue';
import CardPayment from '~/components/Payment/Card.vue';
import PaypalPayment from '~/components/Payment/Paypal.vue';
import UpnPayment from '~/components/Payment/Upn.vue';
import CheckoutStage from '~/components/CheckoutStage.vue';
import ConfirmButton from '~/components/ConfirmButton.vue';

// https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email#Validation
const EMAIL_REGEX = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
const ADDRESS_POST_REGEX = /^\d{4}\s.+/;

export default {
  pageColor: 'secondary',
  nuxtI18n: {
    paths: {
      sl: '/trgovina/blagajna',
      en: '/shop/checkout',
    },
  },
  layout: 'checkout',
  components: {
    CartProduct,
    PaymentSwitcher,
    CardPayment,
    PaypalPayment,
    UpnPayment,
    CheckoutStage,
    ConfirmButton,
  },
  mixins: [shopMixin],
  data() {
    return {
      stage: 'summary',
      summaryLoading: true,
      checkoutLoading: false,
      delivery: null,
      name: null,
      email: null,
      address: null,
      addressPost: null,
      payFunction: undefined,
      paymentInfoValid: false,
      paymentInProgress: false,
      token: null,
      payment: null,
      orderKey: null,
      items: null,
      error: null,
    };
  },
  computed: {
    totalPrice() {
      if (!this.items || !this.items.length) {
        return 0;
      }
      return this.items.reduce(
        (acc, cur) => acc + cur.quantity * cur.article.price,
        0,
      );
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
    canContinueToNextStage() {
      if (this.stage === 'summary') {
        return this.items && this.items.length;
      } else if (this.stage === 'payment') {
        return this.payFunction && this.paymentInfoValid && !this.error;
      }
      return false;
    },
  },
  async mounted() {
    if (typeof window !== 'undefined') {
      this.summaryLoading = true;
      this.orderKey = await this.getOrderKey();
      this.items = await this.getBasketItems(this.orderKey);
      this.summaryLoading = false;
    }
  },
  methods: {
    async onChangeAmount(itemId, newAmount) {
      await this.changeAmount(this.orderKey, itemId, newAmount);
      this.items = await this.getBasketItems(this.orderKey);
    },
    async continueToPayment() {
      try {
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

        this.stage = 'payment';
      } catch (error) {
        // eslint-disable-next-line no-console
        console.error(error.response);
        this.error = error.response;
      }
    },
    continueToNextStage() {
      if (this.canContinueToNextStage) {
        if (this.stage === 'summary') {
          this.stage = 'delivery';
        } else if (this.stage === 'payment') {
          if (this.payFunction) {
            this.payFunction();
          }
        }
      }
    },
    onPaymentReady({ pay } = {}) {
      this.checkoutLoading = false;
      this.paymentInfoValid = false;
      this.payFunction = pay;
    },
    onPaymentError({ error }) {
      this.error = error;
      this.checkoutLoading = false;
      this.paymentInfoValid = false;
      this.payFunction = null;
    },
    onPaymentChange(payment) {
      this.error = null;
      this.checkoutLoading = true;
      this.paymentInfoValid = false;
      this.payment = payment;
    },
    async paymentSuccess({ nonce } = {}) {
      try {
        await this.$axios.$post(
          `https://podpri.djnd.si/api/shop/pay/?order_key=${this.orderKey}`,
          {
            payment_type: nonce ? 'braintree' : 'upn',
            nonce,
          },
        );
        window.localStorage.removeItem('order_key');
        this.stage = 'thankyou';
      } catch (error) {
        // eslint-disable-next-line no-console
        console.error(error.response);
        this.error = error.response;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.loader-container {
  display: flex;
  justify-content: center;
  margin: 3rem 0;

  &.load-container--small {
    margin: 1rem 0;
  }
}

.checkout {
  // .checkout__payment,
  .checkout__thankyou,
  .checkout__delivery,
  .checkout__summary {
    @include media-breakpoint-up(md) {
      width: 540px;
      margin: 0 auto;
    }
  }

  .cart-items {
    margin-bottom: 1rem;

    @include media-breakpoint-up(md) {
      margin-bottom: 2rem;
    }

    hr {
      border-top-color: #333;
      margin-top: 1rem;
      margin-bottom: 1rem;

      @include media-breakpoint-up(md) {
        margin-top: 2rem;
        margin-bottom: 2rem;
      }
    }
  }

  .cart-total {
    text-align: right;
    background-color: rgba($color-red, 0.15);
    padding: 0.75rem 1.5rem;
    margin-bottom: 1rem;
    line-height: 1.25rem;

    @include media-breakpoint-up(md) {
      line-height: 1.75rem;
    }

    span {
      font-size: 1rem;
      line-height: 1rem;
      font-weight: 300;

      @include media-breakpoint-up(md) {
        font-size: 1.25rem;
      }
    }

    i {
      font-weight: 600;
      font-size: 1.25rem;
      line-height: 1;
      margin-left: 0.5rem;

      @include media-breakpoint-up(md) {
        font-size: 1.75rem;
      }
    }
  }

  .confirm-button-container {
    text-align: center;
  }

  .payment-container {
    max-width: 540px;
    margin: 0 auto;

    .payment-loader {
      position: fixed;
      top: -1rem;
      left: -0.5rem;
      bottom: -0.5rem;
      right: -0.5rem;
      z-index: 999999;
      background: rgba(#333, 0.5);
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .payment {
      &.payment--loading {
        opacity: 0;
      }
    }
  }

  .checkout__thankyou {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    .thankyou__content {
      display: flex;
      flex-direction: column;
      justify-content: center;
      flex: 1;

      .icon {
        margin: 0 auto 1.5rem;
        width: 120px;
        height: 120px;
      }

      h1 {
        text-transform: uppercase;
        margin-top: 1.5rem;
        margin-bottom: 2rem;
        text-align: center;
      }

      p {
        text-align: center;
        font-weight: 300;
        margin: 0 auto;
      }

      .thankyou__close {
        margin-top: 2rem;
        margin-bottom: 1.5rem;

        .close-button {
          display: block;
          width: 250px;
          margin: 0 auto;
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
}
</style>
