<template>
  <div class="checkout">
    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <div
      v-else-if="stage === 'select-donation'"
      class="checkout__select-donation"
    >
      <h1 class="checkout__title">Izberi višino donacije!</h1>
      <donation-option
        v-for="(dp, i) in donationPresets"
        :key="i"
        :donationPreset="dp"
        @select="selectDonationPreset(dp)"
      />
      <div class="confirm-button-container">
        <confirm-button
          key="next-select-donation"
          :disabled="!canContinueToYourInfo"
          @click.native="continueToYourInfo"
          text="Podpri"
          color="secondary"
          arrow
          hearts
        />
      </div>
    </div>

    <div v-else-if="stage === 'your-info'" class="checkout__your-info">
      <h1 class="checkout__title">Hvala! Kdo si?</h1>
      <form @submit.prevent="continueToPayment">
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
        <div class="custom-control custom-checkbox">
          <input
            id="info-display-support"
            v-model="displayMySupport"
            type="checkbox"
            name="delivery"
            class="custom-control-input"
            value="pickup"
          />
          <label class="custom-control-label" for="info-display-support"
            >Prikažite me na seznamu podpornikov</label
          >
        </div>
        <div class="custom-control custom-checkbox">
          <input
            id="info-newsletter"
            v-model="subscribeNewsletter"
            type="checkbox"
            name="delivery"
            class="custom-control-input"
            value="post"
          />
          <label class="custom-control-label" for="info-newsletter"
            >Želim prejemati newsletter</label
          >
        </div>
        <!-- this is here so you can submit the form with the enter key -->
        <input type="submit" hidden />
      </form>
      <div class="confirm-button-container">
        <confirm-button
          key="next-your-info"
          v-if="!checkoutLoading"
          :disabled="!canContinueToPayment"
          @click.native="continueToPayment"
          text="Plačaj"
          color="secondary"
          arrow
          hearts
        />
        <template v-else>
          <div class="loader-container load-container--small">
            <div class="lds-dual-ring" />
          </div>
        </template>
      </div>
    </div>

    <div v-else-if="stage === 'payment'" class="checkout__payment">
      <h1 class="checkout__title">Plačilo</h1>
      <payment-switcher @change="onPaymentChange" />
      <template v-if="payment === 'card'">
        <card-payment :token="token" @success="paymentSuccess" />
      </template>
      <template v-if="payment === 'paypal'">
        <paypal-payment
          :token="token"
          :amount="selectedDonationPreset.amount"
          @success="paymentSuccess"
        />
      </template>
      <template v-if="payment === 'upn'">
        <upn-payment />
      </template>
    </div>

    <div v-else-if="stage === 'thankyou'" class="checkout__thankyou">
      <div class="thankyou__content">
        <div>
          <div class="icon icon-heart--secondary" />
        </div>
        <h1>Hvala za podporo!</h1>
        <h2>S tvojo pomočjo smo močnejši.</h2>
      </div>
      <div style="height: 300px; background: #ccc">
        TEHTNICA
      </div>
      <div class="confirm-button-container">
        <confirm-button
          key="next-thankyou"
          @click.native="stage = 'select-avatar'"
          text="Dodaj svoj obraz"
          color="secondary"
          arrow
        />
      </div>
      <div class="terms">
        <nuxt-link @click="stage = 'share'" to="#">Preskoči</nuxt-link>
      </div>
    </div>

    <div v-else-if="stage === 'select-avatar'" class="checkout__select-avatar">
      <h2 class="checkout__title">Dodaj svojo sliko ali izberi avatar!</h2>
      <div style="height: 300px; background: #ccc">
        SELECTOR
      </div>
      <div class="confirm-button-container">
        <confirm-button
          key="next-select-avatar"
          @click.native="stage = 'share'"
          text="Potrdi"
          color="secondary"
        />
      </div>
    </div>
  </div>
</template>

<script>
import shopMixin from '~/mixins/shop.js';
import ConfirmButton from '~/components/ConfirmButton.vue';
import PaymentSwitcher from '~/components/Payment/Switcher.vue';
import CardPayment from '~/components/Payment/Card.vue';
import PaypalPayment from '~/components/Payment/Paypal.vue';
import UpnPayment from '~/components/Payment/Upn.vue';
import DonationOption from '~/components/DonationOption.vue';

// https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email#Validation
const EMAIL_REGEX = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
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
    PaymentSwitcher,
    CardPayment,
    PaypalPayment,
    UpnPayment,
    DonationOption,
  },
  mixins: [shopMixin],
  data() {
    return {
      error: null,
      // stage: 'select-donation',
      stage: 'thankyou',
      donationPresets: [
        {
          amount: 11,
          description: 'TODO: this text',
          selected: false,
        },
        {
          amount: 24,
          description: 'TODO: this text',
          selected: false,
        },
        {
          amount: 47,
          description: 'TODO: this text',
          selected: false,
        },
        {
          amount: 100,
          description: 'TODO: this text',
          selected: false,
        },
        {
          custom: true,
          amount: null,
          description: 'TODO: this text',
          selected: false,
        },
      ],
      name: null,
      email: null,
      displayMySupport: false,
      subscribeNewsletter: false,
      checkoutLoading: false,
      token: null,

      payment: null,
      orderKey: null,
      items: null,
    };
  },
  computed: {
    selectedDonationPreset() {
      return this.donationPresets.find((dp) => dp.selected);
    },
    canContinueToYourInfo() {
      return (
        this.selectedDonationPreset && this.selectedDonationPreset.amount >= 1
      );
    },
    canContinueToPayment() {
      if (!this.name || !this.email) {
        return false;
      }
      if (!EMAIL_REGEX.test(this.email)) {
        return false;
      }
      return true;
    },
  },
  methods: {
    selectDonationPreset(sdp) {
      this.donationPresets.forEach((dp) => {
        dp.selected = dp === sdp;
      });
    },
    continueToYourInfo() {
      if (this.canContinueToYourInfo) {
        this.stage = 'your-info';
      }
    },
    async continueToPayment() {
      try {
        // TODO: shake invalid/empty fields
        // TODO: check email and address fields with regex?
        if (!this.canContinueToPayment) {
          return;
        }

        this.checkoutLoading = true;
        const checkoutResponse = await this.$axios.$get(
          'https://podpri.djnd.si/api/donate',
        );
        this.token = checkoutResponse.token;
        this.checkoutLoading = false;

        this.stage = 'payment';
      } catch (error) {
        // eslint-disable-next-line no-console
        console.error(error);
        this.error = error;
      }
    },
    onPaymentChange(payment) {
      this.payment = payment;
    },
    continueToFaces() {
      this.stage = 'faces';
    },
    async paymentSuccess({ nonce } = {}) {
      try {
        await this.$axios.$post('https://podpri.djnd.si/api/donate', {
          payment_type: nonce ? 'braintree' : 'upn',
          nonce,
          amount: this.selectedDonationPreset.amount,
          name: this.name,
          email: this.email,
          displayMySupport: this.displayMySupport,
          subscribeNewsletter: this.subscribeNewsletter,
        });
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

  h2 {
    font-size: 1.5rem;
    text-align: center;
    font-weight: 300;
    margin: 3rem 0;
  }

  .confirm-button-container {
    margin-top: 2rem;
    text-align: center;
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

  .payment-switcher {
    margin-bottom: 2rem;
  }

  .checkout__thankyou {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin: 0 auto;

    .thankyou__content {
      display: flex;
      flex-direction: column;
      justify-content: center;
      flex: 1;

      .icon {
        margin: 0 auto;
        width: 4rem;
        height: 4rem;
      }

      h1 {
        text-transform: uppercase;
        margin: 0;
        margin-top: 1.5rem;
        font-style: italic;
        text-align: center;
      }

      h2 {
        margin: 0;
        margin-top: 0.75rem;
        font-style: italic;
        text-align: center;
        font-weight: 400;
        font-size: 1.5rem;
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
  margin: 1rem;
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
