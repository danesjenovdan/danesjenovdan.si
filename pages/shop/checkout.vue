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

    <template v-if="stage === 'summary'">
      <div class="checkout__summary">
        <checkout-stage>
          <template slot="title">{{ $t('shop.summary') }}</template>
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
                    :title="$t(`shop.products.${item.article.id}.title`)"
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
                <span v-t="'shop.amountToPay'"></span>
                <i>{{ totalPrice }} €</i>
              </div>
            </template>
          </template>
          <template slot="footer">
            <div class="confirm-button-container">
              <confirm-button
                key="next-summary"
                :disabled="!canContinueToNextStage"
                :text="$t('shop.buy')"
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

    <template v-else-if="stage === 'delivery'">
      <div class="checkout__delivery">
        <checkout-stage>
          <template slot="title">{{ $t('shop.checkout.data') }}</template>
          <template slot="content">
            <form @submit.prevent="continueToPayment">
              <template v-if="delivery">
                <div class="form-group">
                  <input
                    id="name"
                    v-model="name"
                    :placeholder="$t('shop.checkout.name')"
                    class="form-control form-control-lg"
                  />
                </div>
                <div class="form-group">
                  <input
                    id="last-name"
                    v-model="lastName"
                    :placeholder="$t('shop.checkout.lastName')"
                    class="form-control form-control-lg"
                  />
                </div>
                <template v-if="delivery === 'post'">
                  <div class="form-group">
                    <input
                      id="address"
                      v-model="address"
                      :placeholder="$t('shop.checkout.streetAndNum')"
                      class="form-control form-control-lg"
                    />
                  </div>
                  <div class="form-group">
                    <input
                      id="address-post"
                      v-model="addressPost"
                      :placeholder="$t('shop.checkout.postAndNum')"
                      class="form-control form-control-lg"
                    />
                  </div>
                </template>
                <div class="form-group">
                  <input
                    id="email"
                    v-model="email"
                    type="email"
                    :placeholder="$t('shop.checkout.email')"
                    class="form-control form-control-lg"
                  />
                </div>
              </template>
              <div class="custom-control custom-checkbox">
                <input
                  id="info-newsletter"
                  v-model="newsletter"
                  type="checkbox"
                  class="custom-control-input"
                />
                <label
                  class="custom-control-label"
                  for="info-newsletter"
                  v-t="'shop.checkout.newsletter'"
                ></label>
              </div>
              <!-- this is here so you can submit the form with the enter key -->
              <input type="submit" hidden />
            </form>
          </template>
          <template slot="footer">
            <div class="confirm-button-container">
              <confirm-button
                key="next-delivery"
                :disabled="!canContinueToPayment"
                :loading="checkoutLoading"
                :text="$t('shop.checkout.continue')"
                color="secondary"
                arrow
                hearts
                block
                @click.native="continueToPayment"
              />
            </div>
            <div class="bottom-back-link">
              <dynamic-link
                @click="stage = 'summary'"
                v-t="'shop.checkout.back'"
              ></dynamic-link>
            </div>
          </template>
        </checkout-stage>
      </div>
    </template>

    <template v-else-if="stage === 'payment'">
      <div class="checkout__payment">
        <checkout-stage>
          <template slot="title"> Plačilo </template>
          <template slot="content">
            <div class="payment-container">
              <payment-switcher @change="onPaymentChange" />
              <div v-if="checkoutLoading" class="payment-loader">
                <div class="lds-dual-ring" />
              </div>
              <template v-if="payment === 'card'">
                <div
                  :class="['payment', { 'payment--loading': checkoutLoading }]"
                >
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
                <div
                  :class="['payment', { 'payment--loading': checkoutLoading }]"
                >
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
                  @ready="onUPNPaymentReady"
                  @success="paymentSuccess"
                />
              </template>
            </div>
            <div class="cart-total">
              <span v-t="'shop.amountToPay'"></span>
              <i>{{ totalPrice }} €</i>
            </div>
          </template>
          <template slot="footer">
            <div class="confirm-button-container">
              <confirm-button
                key="next-payment"
                :disabled="!canContinueToNextStage"
                :loading="paymentInProgress"
                :text="$t('shop.checkout.continue')"
                color="secondary"
                arrow
                hearts
                block
                @click.native="continueToNextStage"
              />
            </div>
            <div class="bottom-back-link">
              <dynamic-link
                @click="stage = 'delivery'"
                v-t="'shop.checkout.back'"
              ></dynamic-link>
            </div>
          </template>
        </checkout-stage>
      </div>
    </template>

    <div v-else-if="stage === 'thankyou'" class="checkout__thankyou">
      <div class="thankyou__content">
        <h1 v-t="'shop.thanks.title'"></h1>
        <div>
          <div class="icon icon-confetti-popper--secondary" />
        </div>
        <div>
          <p v-t="'shop.thanks.paragraph'"></p>
        </div>
        <div class="thankyou__close">
          <nuxt-link
            :to="localePath('shop')"
            class="close-button"
            v-t="'shop.checkout.close'"
          ></nuxt-link>
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
import DynamicLink from '~/components/DynamicLink.vue';

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
    DynamicLink,
  },
  mixins: [shopMixin],
  data() {
    return {
      stage: 'summary',
      summaryLoading: true,
      checkoutLoading: false,
      delivery: 'post',
      name: null,
      lastName: null,
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
      newsletter: false,
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
      if (!this.name || !this.lastName || !this.email) {
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
            name: `${this.name} ${this.lastName}`,
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
    onUPNPaymentReady({ pay } = {}) {
      this.checkoutLoading = false;
      this.paymentInfoValid = true;
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
      this.paymentInProgress = true;
      try {
        await this.$axios.$post(
          `https://podpri.djnd.si/api/shop/pay/?order_key=${this.orderKey}`,
          {
            payment_type: nonce ? 'braintree' : 'upn',
            nonce,
          },
        );
        window.localStorage.removeItem('order_key');
        this.paymentInProgress = false;
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
  .checkout__thankyou,
  .checkout__payment,
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
    margin-top: auto;
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

  .bottom-back-link {
    margin-top: 1rem;
    text-align: center;

    @include media-breakpoint-up(md) {
      font-size: 1.25rem;
      margin-top: 1.25rem;
    }

    a {
      color: inherit;
      font-style: italic;
      text-decoration: underline;
      font-weight: 600;
    }
  }

  .payment-container {
    flex: 1;
    max-width: 540px;
    margin: 0 auto 1rem;
    display: flex;
    flex-direction: column;

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
      margin: auto 0;

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
  .custom-checkbox {
    margin-bottom: 1rem;

    .custom-control-label {
      font-size: 1rem;
      line-height: 1.1;
      min-height: 2rem;
      display: flex;
      align-items: center;
    }
  }
}
</style>
