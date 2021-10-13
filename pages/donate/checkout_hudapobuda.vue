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

    <checkout-stage v-if="stage === 'info'" :stage="stage" class="hudapobuda">
      <template slot="title">VPIŠI SVOJ E-NASLOV</template>
      <template slot="content">
        <div class="info-content">
          <p class="text-center">
            Hvala, da se z nami podajaš na pot uresničevanja hude pobude!
          </p>
          <p class="text-center">
            Najprej te prosimo, da nam zaupaš svoj e-naslov, saj ga potrebujemo
            za potrditev donacije. V naslednjem koraku zapišeš še podatke o
            plačilnem sredstvu in postopek bo zaključen. Tako preprosto je!
          </p>
          <div class="form-group">
            <input
              id="email"
              v-model="email"
              type="email"
              placeholder="E-naslov"
              class="form-control form-control-lg"
            />
            <div class="custom-control custom-checkbox mt-4">
              <input
                id="newsletter-id"
                type="checkbox"
                class="custom-control-input"
              />
              <label for="newsletter-id" class="custom-control-label"
                >Strinjam se, da me občasno obvestite o izvedbi hude pobude in
                morebitnih drugih novostih.</label
              >
            </div>
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
            @click.native="continueToNextStage"
          />
        </div>
      </template>
    </checkout-stage>

    <checkout-stage
      v-if="stage === 'payment'"
      :stage="stage"
      class="hudapobuda"
    >
      <template slot="title"> PLAČILO </template>
      <template slot="content">
        <div class="payment-container">
          <payment-switcher
            :recurring="false"
            :force-slovenian="true"
            class="hudapobuda"
            @change="onPaymentChange"
          />
          <div v-if="checkoutLoading" class="payment-loader">
            <div class="lds-dual-ring" />
          </div>
          <template v-if="payment === 'card'">
            <card-payment
              :token="token"
              :force-slovenian="true"
              @ready="onPaymentReady"
              @validity-change="paymentInfoValid = $event"
              @payment-start="paymentInProgress = true"
              @success="paymentSuccess"
              @error="paymentError"
            />
          </template>
          <template v-if="payment === 'paypal'">
            <paypal-payment
              :token="token"
              :amount="selectedDonationAmount"
              :recurring="false"
              :force-slovenian="true"
              @ready="onPaymentReady"
              @payment-start="paymentInProgress = true"
              @success="paymentSuccess"
              @error="paymentError"
            />
          </template>
          <template v-if="payment === 'upn'">
            <upn-payment
              :amount="selectedDonationAmount"
              :force-slovenian="true"
              @ready="onUPNPaymentReady"
              @success="paymentSuccess"
            />
          </template>
          <div class="cart-total">
            <span>Znesek za plačilo:</span>
            <i>{{ selectedDonationAmount }} €</i>
          </div>
        </div>
      </template>
      <template slot="footer">
        <div class="confirm-button-container">
          <confirm-button
            key="next-payment"
            :disabled="!canContinueToNextStage"
            :loading="paymentInProgress"
            text="Doniraj"
            color="secondary"
            @click.native="continueToNextStage"
          />
        </div>
        <div class="secondary-link">
          <dynamic-link @click="goBack">Nazaj</dynamic-link>
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
import CheckoutStage from '~/components/CheckoutStage.vue';
import DynamicLink from '~/components/DynamicLink.vue';

// https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email#Validation
const EMAIL_REGEX = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;

export default {
  nuxtI18n: {
    paths: {
      sl: '/doniraj_hudapobuda/placaj',
      en: '/doniraj_hudapobuda/placaj',
    },
    fallbackLocale: 'sl',
  },
  components: {
    ConfirmButton,
    PaymentSwitcher,
    CardPayment,
    PaypalPayment,
    UpnPayment,
    CheckoutStage,
    DynamicLink,
  },
  layout: 'checkout',
  pageColor: 'secondary',
  data() {
    return {
      error: null,
      stage: 'info',
      selectedDonationAmount: 0,
      donationId: null,
      checkoutLoading: false,
      payFunction: undefined,
      paymentInfoValid: false,
      paymentInProgress: false,
      token: null,
      customerId: null,
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
    canContinueToNextStage() {
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
  mounted() {
    this.$i18n.setLocale('sl');
    if (this.$route.query.amount) {
      this.selectedDonationAmount = Number(this.$route.query.amount);
    }
    if (this.$route.query.campaign) {
      this.donationId = Number(this.$route.query.campaign);
    } else {
      // throw error
      console.log('error -  we need donation id!');
    }
  },
  methods: {
    paymentError(argument) {
      // eslint-disable-next-line
      console.log('ERROR VERY ERROR');
      // eslint-disable-next-line
      console.log(argument);
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
              `https://podpri.djnd.si/api/generic-donation/${this.donationId}/`,
            );
            this.token = checkoutResponse.token;
            this.customerId = checkoutResponse.customer_id;
            this.stage = 'payment';
            console.log(checkoutResponse);
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
    goBack() {
      if (this.stage === 'payment') {
        this.stage = 'info';
        return;
      }
      if (this.stage === 'info') {
        this.stage = 'select-amount';
        return;
      }
      return undefined;
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
    onPaymentChange(payment) {
      this.checkoutLoading = true;
      this.paymentInfoValid = false;
      this.payment = payment;
    },
    async paymentSuccess({ nonce } = {}) {
      this.paymentInProgress = true;
      this.nonce = nonce;
      const paymentURL = `https://podpri.djnd.si/api/generic-donation/${this.donationId}/`;
      try {
        const response = await this.$axios.$post(paymentURL, {
          payment_type: this.nonce ? 'braintree' : 'upn',
          nonce: this.nonce,
          customer_id: this.customerId,
          amount: this.selectedDonationAmount,
          email: this.email,
          name: `${this.firstName} ${this.lastName}`,
          address: `${this.streetAddress}, ${this.postalCode} ${this.post}`,
          mailing: this.mailing,
        });

        this.paymentInProgress = false;
        this.$router.push(
          // this.localePath({ name: 'thanks', query: { token } }),
          `/doniraj_stanovanjski-sos/hvala?token=${response.upload_token}`,
        );
        this.paymentInProgress = true;
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
@import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;700&amp;display=swap');

input,
label:before {
  border: 2px solid black;
}
input,
input::placeholder {
  text-decoration: none;
  font-style: normal;
  font-family: 'Courier New';
}
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
    .confirm-button {
      background-color: #a6d07d;
      border: 2px solid black;
      font-family: $font-family-comfortaa;
      color: black;
      text-transform: capitalize;
      font-style: normal;
      font-size: 1.5rem;
      font-weight: 700;
      padding: 1rem 3rem;
      width: 100%;
      max-width: 540px;
    }
  }

  .change-monthly {
    text-align: center;
    margin-bottom: 3rem;
    margin-top: -1.5rem;

    a {
      font-size: 1rem;
      font-weight: 600;
      font-style: italic;
      color: inherit;
      text-decoration: underline;
      cursor: pointer;

      @include media-breakpoint-up(md) {
        font-size: 1.5rem;
      }

      &:hover {
        text-decoration: none;
      }
    }
  }

  .secondary-link {
    text-align: center;
    margin-top: 1.5rem;

    a {
      font-size: 1rem;
      font-weight: 600;
      color: inherit;
      text-decoration: underline;
      cursor: pointer;

      @include media-breakpoint-up(md) {
        font-size: 1.5rem;
      }

      &:hover {
        text-decoration: none;
      }
    }
  }

  .payment-container,
  .info-content {
    width: 100%;
    max-width: 540px;
    margin: 0 auto;
  }

  .payment-container {
    display: flex;
    flex-direction: column;
    flex: 1;

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

    .cart-total {
      text-align: right;
      background-color: #fffdef;
      padding: 0.5rem 1rem;
      margin: auto auto 0 auto;
      margin-top: 1.5rem;
      margin-bottom: 1rem;
      width: 100%;
      max-width: 350px;
      font-family: $font-family-comfortaa;
      font-weight: 600;

      i {
        font-size: 1.25rem;
        font-style: normal;
        margin-left: 0.25rem;
      }
    }
  }

  .custom-control.custom-checkbox
    .custom-control-input:checked
    ~ .custom-control-label:before {
    border: 2px solid black;
    background-color: transparent;
  }

  .custom-control.custom-checkbox
    .custom-control-input:checked
    ~ .custom-control-label:after {
    background-image: url('/img/hudapobuda-donations/check.png');
    background-position: center;
    background-repeat: no-repeat;
    background-size: 80%;
  }

  .custom-checkbox {
    margin-bottom: 1rem;
    &:after {
      border: 2px solid black;
    }

    .custom-control-label {
      font-size: 0.925rem;
      line-height: 1.1;
      min-height: 2rem;
      display: flex;
      align-items: center;
      font-family: $font-family-comfortaa;
    }
  }

  .payment-switcher .nav .nav-item .nav-link.active {
    background-color: #f4b7d1;
    border-radius: 0;
  }

  .card-payment {
    .card-info {
      font-family: $font-family-comfortaa;
    }
  }
}
</style>
