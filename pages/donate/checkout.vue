<template>
  <div class="checkout">
    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <checkout-stage v-if="stage === 'select-amount'">
      <template slot="title">
        Izberi višino donacije!
      </template>
      <template slot="content">
        <div class="donation-options">
          <donation-option
            v-for="(dp, i) in donationPresets"
            :key="`presets-${i}`"
            :donationPreset="dp"
            @select="gift ? addDonationGift(dp) : selectDonationPreset(dp)"
          />
          <div
            v-for="n in 10"
            :key="`flex-spacer-${n}`"
            class="donation-option"
          />
        </div>
        <template v-if="gift">
          <h2 class="donation-gifts-title">
            Obstoječa darila ({{ donationGifts.length }})
          </h2>
          <div class="donation-options donation-gifts">
            <donation-option
              v-for="(dg, i) in donationGifts"
              :key="`gifts-${i}`"
              :donationPreset="dg"
              @select="removeDonationGift(dg)"
              amount-only
            />
            <div
              v-for="n in 10"
              :key="`flex-spacer-${n}`"
              class="donation-option"
            />
          </div>
        </template>
      </template>
      <template slot="footer">
        <div class="confirm-button-container">
          <confirm-button
            key="next-select-amount"
            :disabled="!canContinueToNextStage"
            :loading="checkoutLoading"
            @click.native="continueToNextStage"
            text="Podpri"
            color="secondary"
            arrow
            hearts
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
            @click.native="continueToNextStage"
            text="Plačaj"
            color="secondary"
            arrow
            hearts
          />
        </div>
      </template>
    </checkout-stage>

    <checkout-stage v-if="stage === 'info'">
      <template slot="title">
        Hvala!<br />
        Kam ti pošljemo zahvalo?
      </template>
      <template slot="content">
        <div class="info-content">
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
              id="address"
              v-model="address"
              type="address"
              placeholder="Naslov"
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
              id="info-newsletter"
              v-model="subscribeNewsletter"
              type="checkbox"
              name="subscribeNewsletter"
              class="custom-control-input"
            />
            <label class="custom-control-label" for="info-newsletter"
              >Želim prejemati newsletter</label
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
            @click.native="continueToNextStage"
            text="Potrdi"
            color="secondary"
            arrow
            hearts
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
      donationGifts: [],
      checkoutLoading: false,
      payFunction: undefined,
      paymentInfoValid: false,
      paymentInProgress: false,
      token: null,
      payment: null,
      nonce: undefined,
      name: null,
      address: null,
      email: null,
      subscribeNewsletter: false,
      infoSubmitting: false,
    };
  },
  computed: {
    selectedDonationAmount() {
      if (this.gift) {
        return this.donationGifts.reduce((acc, dg) => acc + dg.amount, 0);
      }
      const selected = this.donationPresets.find((dp) => dp.selected);
      return selected ? selected.amount : 0;
    },
    canContinueToNextStage() {
      if (this.stage === 'select-amount') {
        return this.selectedDonationAmount >= 1;
      }
      if (this.stage === 'payment') {
        return this.payFunction && this.paymentInfoValid;
      }
      if (this.stage === 'info') {
        return this.infoValid;
      }
      return false;
    },
    infoValid() {
      if (!this.name || !this.email || !this.address) {
        return false;
      }
      if (!EMAIL_REGEX.test(this.email)) {
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
  asyncData({ query }) {
    const gift = query.gift === 'true' || query.gift === '1';
    return {
      gift,
    };
  },
  methods: {
    selectDonationPreset(sdp) {
      this.donationPresets.forEach((dp) => {
        dp.selected = dp === sdp;
      });
    },
    addDonationGift(dp) {
      this.donationGifts.unshift({
        amount: dp.amount,
        selected: true,
      });
      if (dp.custom) {
        dp.amount = null;
      }
    },
    removeDonationGift(dg) {
      const i = this.donationGifts.findIndex((d) => d === dg);
      this.donationGifts.splice(i, 1);
    },
    async continueToNextStage() {
      if (this.canContinueToNextStage) {
        if (this.stage === 'select-amount') {
          try {
            this.checkoutLoading = true;
            const checkoutResponse = await this.$axios.$get(
              'https://podpri.djnd.si/api/donate/',
            );
            this.token = checkoutResponse.token;
            this.stage = 'payment';
          } catch (error) {
            // eslint-disable-next-line no-console
            console.error(error);
            this.error = error;
          }
        } else if (this.stage === 'payment') {
          if (this.payFunction) {
            this.payFunction();
          }
        } else if (this.stage === 'info') {
          try {
            // const giftAmounts = this.gift
            //   ? this.donationGifts.map((g) => g.amount)
            //   : undefined;

            // const response = await this.$axios.$patch(
            //   `https://podpri.djnd.si/api/donate${this.gift ? '-gift' : ''}/`,
            //   {
            //     gifts_amounts: giftAmounts,
            //     name: this.name,
            //     email: this.email,
            //     address: this.address,
            //     mailing: this.subscribeNewsletter,
            //   },
            // );
            const response = {};

            if (response.upload_token) {
              // TODO: redirect to page
              // this.$router.push(
              //   this.localePath({
              //     name: 'donate-thanks',
              //     query: { token: response.upload_token },
              //   }),
              // );
              // [PATCH] https://podpri.djnd.si/api/images/9cdd6ed1c061d8182b8ceabfb57f2a52/
            } else if (response.owner_token) {
              // TODO: redirect to page
              // this.$router.push(
              //   this.localePath({
              //     name: 'donate-gifts',
              //     query: { token: response.owner_token },
              //   }),
              // );
              // [GET] https://podpri.djnd.si/api/assign-gift/ed79f46269ee4794b813d8ea419e8ee9/
            }
          } catch (error) {
            // eslint-disable-next-line no-console
            console.error(error);
            this.error = error;
          }
        }
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
        // const response = await this.$axios.$post(
        //   `https://podpri.djnd.si/api/donate${this.gift ? '-gift' : ''}/`,
        //   {
        //     payment_type: this.nonce ? 'braintree' : 'upn',
        //     nonce: this.nonce,
        //     amount: this.selectedDonationAmount,
        //   },
        // );
        // TODO: get some token or something to know where to patch in the next step
        await 0;

        this.paymentInProgress = false;
        this.stage = 'info';
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

    &.donation-gifts {
      .donation-option /deep/ .donation-option__content-wrapper {
        @include media-breakpoint-up(md) {
          flex-direction: row;
          min-height: auto;

          .donation-option__amount {
            margin-bottom: 0;
          }
        }
      }
    }
  }

  .donation-gifts-title {
    font-size: 1.25rem;
    text-align: left;
    font-weight: 300;
    margin: 1rem 0 2rem 0;
    text-transform: uppercase;

    @include media-breakpoint-up(md) {
      font-size: 1.5rem;
      margin-left: 1rem;
    }
  }

  .confirm-button-container {
    text-align: center;
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
