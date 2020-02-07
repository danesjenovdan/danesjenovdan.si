<template>
  <div class="checkout">
    <div v-if="error" class="alert alert-danger">
      <p>
        Zgodila se je napaka št. {{ error.status }}. Naš strežnik je ni mogel
        rešiti, prejel je naslednje sporočilo:
        <strong>{{
          error.data && error.data.msg ? error.data.msg : error.message
        }}</strong>
      </p>
      <p>
        Zaračunali ti nismo ničesar, ves denar je še vedno na tvoji kartici.
        Predlagamo, da osvežiš stran in poskusiš ponovno. Če ne bo šlo, nam piši
        na
        <a href="mailto:vsi@danesjenovdan.si">vsi@danesjenovdan.si</a> in ti
        bomo poskusili pomagati.
      </p>
    </div>

    <checkout-stage v-if="stage === 'select-amount'" :stage="stage">
      <template slot="title">
        Izberi višino donacije!
      </template>
      <template slot="content">
        <div class="donation-options">
          <donation-option
            v-for="(dp, i) in donationPresets"
            :key="`presets-${i}`"
            :donation-preset="dp"
            @select="selectDonationPreset(dp)"
          />
          <div
            v-for="n in 10"
            :key="`flex-spacer-${n}`"
            class="donation-option"
          />
        </div>
      </template>
      <template slot="footer">
        <div class="confirm-button-container">
          <confirm-button
            key="next-select-amount"
            :disabled="!canContinueToNextStage"
            :loading="checkoutLoading"
            text="PODPRI NAS"
            color="secondary"
            arrow
            hearts
            @click.native="continueToNextStage"
          />
        </div>
        <div class="secondary-link">
          <!-- TODO: link to monthly -->
          <nuxt-link :to="localePath({})">
            Želiš darovati mesečno?
          </nuxt-link>
        </div>
      </template>
    </checkout-stage>

    <checkout-stage v-if="stage === 'info'" :stage="stage">
      <template slot="title">
        Podatki
      </template>
      <template slot="content">
        <div class="info-content">
          <div class="form-group">
            <input
              id="firstName"
              v-model="firstName"
              placeholder="Ime"
              class="form-control form-control-lg"
            />
          </div>
          <div class="form-group">
            <input
              id="lastName"
              v-model="lastName"
              placeholder="Priimek"
              class="form-control form-control-lg"
            />
          </div>
          <div class="form-group">
            <input
              id="streetAddress"
              v-model="streetAddress"
              placeholder="Ulica in hišna številka"
              class="form-control form-control-lg"
            />
          </div>
          <div class="form-group form-row">
            <div class="col-4">
              <input
                id="postalCode"
                v-model="postalCode"
                placeholder="Poštna številka"
                class="form-control form-control-lg"
              />
            </div>
            <div class="col-8">
              <input
                id="post"
                v-model="post"
                placeholder="Pošta"
                class="form-control form-control-lg"
              />
            </div>
          </div>
          <div class="form-group">
            <input
              id="email"
              v-model="email"
              type="email"
              placeholder="E-naslov"
              class="form-control form-control-lg"
            />
          </div>
          <div class="custom-control custom-checkbox">
            <input
              id="info-newsletter"
              v-model="subscribeNewsletter"
              type="checkbox"
              name="subscribeNewsletter"
              class="custom-control-input"
            />
            <label class="custom-control-label" for="info-newsletter"
              >Želim se naročiti na e-novice.</label
            >
          </div>
        </div>
      </template>
      <template slot="footer">
        <div class="confirm-button-container">
          <confirm-button
            key="next-info"
            :disabled="!canContinueToNextStage"
            :loading="infoSubmitting"
            text="Naprej"
            color="secondary"
            arrow
            hearts
            @click.native="continueToNextStage"
          />
        </div>
        <div class="secondary-link">
          <nuxt-link :to="localePath({})">
            Nazaj
          </nuxt-link>
        </div>
      </template>
    </checkout-stage>

    <checkout-stage v-if="stage === 'payment'" :stage="stage">
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
            <card-payment
              :token="token"
              @ready="onPaymentReady"
              @validity-change="paymentInfoValid = $event"
              @payment-start="paymentInProgress = true"
              @success="paymentSuccess"
            />
          </template>
          <template v-if="payment === 'paypal'">
            <paypal-payment
              :token="token"
              :amount="selectedDonationAmount"
              @ready="onPaymentReady"
              @payment-start="paymentInProgress = true"
              @success="paymentSuccess"
            />
          </template>
          <template v-if="payment === 'upn'">
            <upn-payment />
          </template>
        </div>
      </template>
      <template slot="footer">
        <div class="confirm-button-container">
          <confirm-button
            key="next-payment"
            :disabled="!canContinueToNextStage"
            :loading="paymentInProgress"
            text="DONIRAJ"
            color="secondary"
            arrow
            hearts
            @click.native="continueToNextStage"
          />
        </div>
      </template>
    </checkout-stage>
  </div>
</template>

<script>
import ConfirmButton from '~/components/ConfirmButton.vue';
import PaymentSwitcher from '~/components/Payment/Switcher.vue';
import CardPayment from '~/components/Payment/Card.vue';
import PaypalPayment from '~/components/Payment/Paypal.vue';
import UpnPayment from '~/components/Payment/Upn.vue';
import DonationOption from '~/components/DonationOption.vue';
import CheckoutStage from '~/components/CheckoutStage.vue';

// https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email#Validation
const EMAIL_REGEX = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;

export default {
  nuxtI18n: {
    paths: {
      sl: '/doniraj/placaj',
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
    CheckoutStage,
  },
  data() {
    return {
      error: null,
      stage: 'select-amount',
      donationPresets: [
        {
          amount: 11,
          description: 'Čaka te mini presenečenje!',
          selected: false,
          eventName: 'eleven',
        },
        {
          amount: 24,
          description: 'Čaka te majhno presenečenje!',
          selected: false,
          eventName: 'twentyfour',
        },
        {
          amount: 47,
          description: 'Čaka te presečenje!',
          selected: false,
          eventName: 'fortyseven',
        },
        {
          amount: 101,
          description: 'Ti si presenečenje! In čaka te ornk presenečenje :)',
          selected: false,
          eventName: 'whale',
        },
        {
          custom: true,
          amount: null,
          description: 'Vnesi poljuben znesek!',
          selected: false,
          eventName: 'aeleven',
        },
      ],
      checkoutLoading: false,
      payFunction: undefined,
      paymentInfoValid: false,
      paymentInProgress: false,
      token: null,
      payment: null,
      nonce: undefined,
      firstName: null,
      lastName: null,
      streetAddress: null,
      postalCode: null,
      post: null,
      email: null,
      subscribeNewsletter: false,
      infoSubmitting: false,
    };
  },
  computed: {
    selectedDonationAmount() {
      const selected = this.donationPresets.find((dp) => dp.selected);
      return selected ? Number(selected.amount) : 0;
    },
    canContinueToNextStage() {
      if (this.stage === 'select-amount') {
        return this.selectedDonationAmount >= 1;
      }
      if (this.stage === 'info') {
        return this.infoValid && !this.checkoutLoading;
      }
      if (this.stage === 'payment') {
        return this.payFunction && this.paymentInfoValid;
      }
      return false;
    },
    infoValid() {
      if (!this.email || !EMAIL_REGEX.test(this.email)) {
        return false;
      }
      // mautic fails after payment if invalid email
      // TODO: fix regex instead of this tmp
      const tmp = this.email.split('@');
      if (tmp.length < 2 || !tmp[1].includes('.')) {
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
    async continueToNextStage() {
      if (this.canContinueToNextStage) {
        if (this.stage === 'select-amount') {
          this.stage = 'info';
          return;
        }
        if (this.stage === 'info') {
          try {
            this.checkoutLoading = true;
            const checkoutResponse = await this.$axios.$get(
              'https://podpri.djnd.si/api/donate/',
            );
            this.token = checkoutResponse.token;
            this.stage = 'payment';
          } catch (error) {
            // eslint-disable-next-line no-console
            console.error(error.response);
            this.error = error.response;
          }
          return;
        }
        if (this.stage === 'payment') {
          if (this.payFunction) {
            this.payFunction();
          }
          return;
        }
        return undefined;
      }
    },
    onPaymentReady({ pay } = {}) {
      this.checkoutLoading = false;
      this.paymentInfoValid = false;
      this.payFunction = pay;
    },
    onPaymentChange(payment) {
      this.checkoutLoading = true;
      this.paymentInfoValid = false;
      this.payment = payment;
    },
    async paymentSuccess({ nonce } = {}) {
      this.nonce = nonce;

      try {
        await this.$axios.$post(`https://podpri.djnd.si/api/donate/`, {
          // payment_type: this.nonce ? 'braintree' : 'upn',
          nonce: this.nonce,
          amount: this.selectedDonationAmount,
        });

        this.paymentInProgress = false;
        this.stage = 'info';
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
.checkout {
  .donation-options {
    display: flex;
    flex-direction: column;

    @include media-breakpoint-up(md) {
      flex-wrap: wrap;
      flex-direction: row;
      margin-left: -0.75rem;
      margin-right: -0.75rem;
    }

    .donation-option {
      @include media-breakpoint-up(md) {
        flex: 1 1 250px;
        flex-direction: column;
        align-items: stretch;
        margin-left: 0.75rem;
        margin-right: 0.75rem;
      }
    }
  }

  .confirm-button-container {
    text-align: center;
  }

  .secondary-link {
    text-align: center;
    margin-top: 1.5rem;

    a {
      font-size: 1.5rem;
      font-weight: 600;
      font-style: italic;
      color: inherit;
      text-decoration: underline;

      &:hover {
        text-decoration: none;
      }
    }
  }

  .payment-container {
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
  }

  .payment-container,
  .info-content {
    max-width: 540px;
    margin: 0 auto;
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
