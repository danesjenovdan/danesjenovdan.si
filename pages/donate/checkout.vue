<template>
  <div class="checkout">
    <div v-if="error" class="alert alert-danger">
      <p>
        Zgodila se je napaka št. {{ error.status }}. Naš strežnik je ni mogel
        rešiti, prejel je naslednje sporočilo:
        <strong>{{ error.data.msg }}</strong>
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
            text="PODPRI NAS"
            color="secondary"
            arrow
            hearts
          />
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
            @click.native="continueToNextStage"
            text="DONIRAJ"
            color="secondary"
            arrow
            hearts
          />
        </div>
      </template>
    </checkout-stage>

    <checkout-stage v-if="stage === 'info'" :stage="stage">
      <template slot="title">
        Hvala za plačilo!<br /><span v-if="selectedDonationAmount >= 11"
          >Kam ti pošljemo presenečenje?</span
        ><span v-else>Kam ti pošljemo potrdilo?</span>
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
              v-if="selectedDonationAmount >= 11"
            />
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
            @click.native="continueToNextStage"
            text="Naprej"
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
          description: 'Čaka te mini presenečenje!',
          selected: false,
        },
        {
          amount: 24,
          description: 'Čaka te majhno presenečenje!',
          selected: false,
        },
        {
          amount: 47,
          description: 'Čaka te presečenje!',
          selected: false,
        },
        {
          amount: 101,
          description: 'Ti si presenečenje! In čaka te ornk presenečenje :)',
          selected: false,
        },
        {
          custom: true,
          amount: null,
          description: 'Vnesi poljuben znesek!',
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
        if (this.selectedDonationAmount >= 1) {
          return true;
        } else if (
          parseInt(this.donationPresets.find((dp) => dp.custom).amount) > 0
        ) {
          return true;
        }
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
      if (!this.name || !this.email) {
        // USED TO BE ALSO || !this.address) {
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
        amount: parseInt(dp.amount),
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
          if (!this.selectedDonationAmount) {
            this.donationPresets.find((dp) => dp.custom).selected = true;
            if (this.gift) {
              const selected = this.donationPresets.find((dp) => dp.selected);
              this.addDonationGift(selected);
            }
          }
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
        } else if (this.stage === 'payment') {
          if (this.payFunction) {
            this.payFunction();
          }
        } else if (this.stage === 'info') {
          try {
            this.infoSubmitting = true;
            const response = await this.$axios.$post(
              `https://podpri.djnd.si/api/donate${this.gift ? '-gift' : ''}/`,
              {
                nonce: this.nonce,
                name: this.name,
                email: this.email,
                address: this.address,
                mailing: this.subscribeNewsletter,
              },
            );

            if (response.upload_token) {
              this.$router.push(
                this.localePath({
                  name: 'donate-thanks',
                  query: { token: response.upload_token },
                }),
              );
            } else if (response.owner_token) {
              this.$router.push(
                this.localePath({
                  name: 'donate-gifts',
                  query: { token: response.owner_token },
                }),
              );
            }
          } catch (error) {
            // eslint-disable-next-line no-console
            console.error(error.response);
            this.error = error.response;
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
        const giftAmounts = this.gift
          ? this.donationGifts.map((g) => g.amount)
          : undefined;

        await this.$axios.$post(
          `https://podpri.djnd.si/api/donate${this.gift ? '-gift' : ''}/`,
          {
            // payment_type: this.nonce ? 'braintree' : 'upn',
            nonce: this.nonce,
            amount: this.selectedDonationAmount,
            gifts_amounts: giftAmounts,
          },
        );

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
