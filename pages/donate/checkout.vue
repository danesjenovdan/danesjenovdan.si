<template>
  <div class="checkout">
    <div v-if="error" class="alert alert-danger">{{ error }}</div>
    <div
      v-else-if="stage === 'select-donation'"
      class="checkout__select-donation"
    >
      <h1 class="checkout__title">Izberi višino donacije!</h1>
      <div v-for="i in 5" :key="i" class="donation-option">
        <div class="donation-option__content">
          <div class="donation-option__amount">
            10 €
          </div>
          <div class="donation-option__description">
            Mini presenečenje za maksi podporo!
          </div>
        </div>
        <div class="donation-option__icon">
          <div class="icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 95 95">
              <path
                d="M47.9 1.6a44.3 44.3 0 100 88.5 44.3 44.3 0 000-88.5z"
                fill="none"
                stroke="currentColor"
                stroke-width="6"
              />
              <path
                d="M72.9 35.7L40 68.7a1.4 1.4 0 01-2 0L18.6 49a1.4 1.4 0 010-2l6.8-6.8c.3-.2.6-.4 1-.4s.7.2 1 .5L39.2 52l25-25c.6-.6 1.4-.6 2 0l6.8 6.8a1.4 1.4 0 010 2z"
                fill="none"
                stroke="currentColor"
                stroke-width="6"
              />
            </svg>
          </div>
        </div>
      </div>
      <div class="donation-option">
        <div class="donation-option__content">
          <div class="donation-option__amount">
            <div class="custom-amount">
              <input id="custom-amount" type="text" class="form-control" />
              <label for="custom-amount">€</label>
            </div>
          </div>
          <div class="donation-option__description">
            Mini presenečenje za maksi podporo!
          </div>
        </div>
        <div class="donation-option__icon">
          <div class="icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 95 95">
              <path
                d="M47.9 1.6a44.3 44.3 0 100 88.5 44.3 44.3 0 000-88.5z"
                fill="none"
                stroke="currentColor"
                stroke-width="6"
              />
              <path
                d="M72.9 35.7L40 68.7a1.4 1.4 0 01-2 0L18.6 49a1.4 1.4 0 010-2l6.8-6.8c.3-.2.6-.4 1-.4s.7.2 1 .5L39.2 52l25-25c.6-.6 1.4-.6 2 0l6.8 6.8a1.4 1.4 0 010 2z"
                fill="none"
                stroke="currentColor"
                stroke-width="6"
              />
            </svg>
          </div>
        </div>
      </div>
      <div class="confirm-button-container">
        <confirm-button
          key="next-summary"
          :to="''"
          :text="'Podpri'"
          @click.native="continueToPayment"
          color="secondary"
          arrow
          hearts
        />
      </div>
    </div>
    <div v-if="stage !== 'thankyou'" class="terms">
      <nuxt-link to="#">Pogoji poslovanja</nuxt-link>
    </div>
  </div>
</template>

<script>
import shopMixin from '~/mixins/shop.js';
import ConfirmButton from '~/components/ConfirmButton.vue';
// import PaymentSwitcher from '~/components/Payment/Switcher.vue';
// import CardPayment from '~/components/Payment/Card.vue';
// import PaypalPayment from '~/components/Payment/Paypal.vue';
// import UpnPayment from '~/components/Payment/Upn.vue';

// https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email#Validation
// const EMAIL_REGEX = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
// const ADDRESS_POST_REGEX = /^\d{4}\s.+/;

export default {
  nuxtI18n: {
    paths: {
      sl: '/doniraj/blagajna',
      en: '/donate/checkout',
    },
  },
  layout: 'checkout',
  pageColor: 'secondary',
  components: {
    ConfirmButton,
    // PaymentSwitcher,
    // CardPayment,
    // PaypalPayment,
    // UpnPayment,
  },
  mixins: [shopMixin],
  data() {
    return {
      stage: 'select-donation',
      checkoutLoading: false,
      delivery: null,
      name: null,
      email: null,
      address: null,
      addressPost: null,
      payment: null,
      orderKey: null,
      items: null,
      token: null,
      error: null,
    };
  },
  methods: {
    continueToPayment() {
      this.stage = 'payment';
    },
    onPaymentChange(payment) {
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
        console.error(error);
        this.error = error;
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

  .confirm-button-container {
    text-align: center;
  }

  .donation-option {
    display: flex;
    padding: 1rem 1.25rem;
    margin-bottom: 1.5rem;

    border: 2px solid rgba($color-red, 0.2);
    background-image: linear-gradient(
      to right,
      rgba($color-yellow, 0.2) 0%,
      rgba($color-red, 0.2) 100%
    );

    .donation-option__content {
      .donation-option__amount {
        font-size: 2rem;
        font-weight: 600;
        line-height: 1;

        .custom-amount {
          margin-top: 0.5rem;
          position: relative;
          width: 75%;

          .form-control {
            background-color: transparent;
            font-size: 1.75rem;
            font-weight: 600;
            font-style: normal;
            color: inherit;
            padding-right: 1.75rem;
          }

          label {
            position: absolute;
            top: 0.7rem;
            right: 0.5rem;
            font-size: 2rem;
          }
        }
      }

      .donation-option__description {
        font-size: 1rem;
        font-weight: 300;
        font-style: italic;
        margin-top: 0.5rem;
      }
    }

    .donation-option__icon {
      display: flex;
      align-items: center;

      .icon {
        width: 2.5rem;
        color: rgba($color-red, 0.6);

        svg {
          width: 100%;
          height: 100%;
        }
      }
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
