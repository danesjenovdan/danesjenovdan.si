<template>
  <div class="checkout">
    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <div v-else-if="stage === 'select-amount'" class="checkout__select-amount">
      <h1 class="checkout__title">Izberi višino donacije!</h1>
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
        <h2 class="checkout__subtitle">Obstoječa darila</h2>
        <div class="donation-options donation-gifts">
          <donation-option
            v-for="(dg, i) in donationGifts"
            :key="`gifts-${i}`"
            :donationPreset="dg"
            @select="removeDonationGift(dg)"
          />
        </div>
      </template>

      <div class="confirm-button-container">
        <confirm-button
          key="next-select-amount"
          :disabled="!canContinueToInfo"
          @click.native="continueToInfo"
          text="Podpri"
          color="secondary"
          arrow
          hearts
        />
      </div>
    </div>

    <div v-else-if="stage === 'info'" class="checkout__info">
      <h1 class="checkout__title">
        Hvala!<br />
        Kam ti pošljemo zahvalo?
      </h1>
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
        <!-- this is here so you can submit the form with the enter key -->
        <input type="submit" hidden />
      </form>
      <div class="confirm-button-container">
        <confirm-button
          key="next-info"
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
      <div class="payment-container">
        <payment-switcher @change="onPaymentChange" />
        <template v-if="payment === 'card'">
          <card-payment :token="token" @success="paymentSuccess" />
        </template>
        <template v-if="payment === 'paypal'">
          <paypal-payment
            :token="token"
            :amount="selectedDonationAmount"
            @success="paymentSuccess"
          />
        </template>
        <template v-if="payment === 'upn'">
          <upn-payment />
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import ConfirmButton from '~/components/ConfirmButton.vue';
import PaymentSwitcher from '~/components/Payment/Switcher.vue';
import CardPayment from '~/components/Payment/Card.vue';
import PaypalPayment from '~/components/Payment/Paypal.vue';
import UpnPayment from '~/components/Payment/Upn.vue';
import DonationOption from '~/components/DonationOption.vue';

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
      name: null,
      address: null,
      email: null,
      subscribeNewsletter: false,
      checkoutLoading: false,
      token: null,
      payment: null,
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
    canContinueToInfo() {
      return this.selectedDonationAmount >= 1;
    },
    canContinueToPayment() {
      if (!this.name || !this.email) {
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
    continueToInfo() {
      if (this.canContinueToInfo) {
        this.stage = 'info';
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
          'https://podpri.djnd.si/api/donate/',
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
    async paymentSuccess({ nonce } = {}) {
      try {
        const giftAmounts = this.gift
          ? this.donationGifts.map((g) => g.amount)
          : undefined;

        const response = await this.$axios.$post(
          `https://podpri.djnd.si/api/donate${this.gift ? '-gift' : ''}/`,
          {
            payment_type: nonce ? 'braintree' : 'upn',
            nonce,
            amount: this.selectedDonationAmount,
            name: this.name,
            email: this.email,
            address: this.address,
            mailing: this.subscribeNewsletter,
            gifts_amounts: giftAmounts,
          },
        );

        if (response.upload_token) {
          // this.$router.push(this.localePath('shop'));
        }
        // this.stage = 'thankyou';
        // TODO: move to thankyou page
        console.log(response);
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
  justify-content: center;
  padding: 1.5rem 0;

  .checkout__title {
    font-size: 1.75rem;
    text-align: center;
    font-weight: 600;
    margin-bottom: 1.5rem;

    @include media-breakpoint-up(md) {
      font-size: 3rem;
      margin-bottom: 2.25rem;
    }
  }

  .checkout__subtitle {
    font-size: 1.25rem;
    text-align: left;
    font-weight: 300;
    margin: 2rem 0;
    text-transform: uppercase;
  }

  .confirm-button-container {
    margin-top: 2rem;
    text-align: center;

    @include media-breakpoint-up(md) {
      margin-top: 10rem;

      /deep/ .confirm-button {
        font-size: 3rem;

        .arrow {
          height: 0.75em;
        }

        .heart {
          height: 1.25em;
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

  .payment-switcher {
    margin-bottom: 2rem;
  }

  .donation-options {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;

    @include media-breakpoint-up(md) {
      flex-direction: row;
      margin: 0 -0.33rem;

      .donation-option {
        flex: 1;
        flex-basis: 250px;
        flex-direction: column;
        align-items: stretch;
        margin: 0 0.33rem;

        /deep/ .donation-option__content-wrapper {
          min-height: 20vh;
          margin-bottom: 0.66rem;
          padding: 1.5rem;
          flex-direction: column;

          .donation-option__amount {
            font-size: 2.25rem;
            margin-bottom: 1.25rem;
          }

          .donation-option__description {
            font-size: 1.25rem;
          }

          .donation-option__icon {
            flex-direction: column;
            align-items: flex-end;
            margin-right: -0.75rem;
            margin-bottom: -0.75rem;

            .icon {
              width: 3rem;
            }
          }
        }
      }

      &.donation-gifts {
        .donation-option {
          flex: 0 0 200px;

          /deep/ .donation-option__content-wrapper {
            flex-direction: row;
            min-height: auto;

            .donation-option__amount {
              margin-bottom: 0;
            }
          }
        }
      }
    }
  }

  .checkout__payment .payment-container,
  .checkout__info form {
    max-width: 540px;
    margin: 0 auto;
  }
}
</style>
