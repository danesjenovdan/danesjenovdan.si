<template>
  <div class="checkout checkout--parlameter">
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
        Izberi višino <strong v-if="monthlyDonation">mesečne</strong> donacije!
      </template>
      <template slot="content">
        <div class="change-monthly">
          <a v-if="monthlyDonation" @click.prevent="monthlyDonation = false">
            Želiš darovati enkrat?
          </a>
          <a v-else @click.prevent="monthlyDonation = true">
            Želiš darovati mesečno?
          </a>
        </div>
        <div class="donation-options">
          <donation-option
            v-for="(dp, i) in filteredDonationPresets"
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
      </template>
    </checkout-stage>

    <checkout-stage v-if="stage === 'info'" :stage="stage">
      <template slot="title"> Podatki </template>
      <template slot="content">
        <div class="info-content">
          <div class="form-group">
            <input
              id="email"
              v-model="email"
              type="email"
              placeholder="E-naslov"
              class="form-control form-control-lg"
            />
          </div>
          <hr />
          <p>
            Zadnje čase nas pogosto napadajo roboti. Ker se želimo prepričati, da si človek, nam prosim povej, kako se piše trenutni predsednik Vlade Republike Slovenije.
          </p>
          <div class="form-group">
            <input
              id="answer"
              v-model="answer"
              type="text"
              placeholder="Tvoj odgovor"
              class="form-control form-control-lg"
            />
          </div>
          <div class="lonec-medu">
            <input
              type="text"
              name="name"
              placeholder="Your full name please"
              v-model="honeyPotName"
            />
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
          <dynamic-link @click="goBack">Nazaj</dynamic-link>
        </div>
      </template>
    </checkout-stage>

    <checkout-stage v-if="stage === 'payment'" :stage="stage">
      <template slot="title"> Plačilo </template>
      <template slot="content">
        <div class="payment-container">
          <payment-switcher
            :has-upn="hasUpn"
            :recurring="monthlyDonation"
            @change="onPaymentChange"
          />
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
              @error="paymentError"
            />
          </template>
          <template v-if="payment === 'paypal'">
            <paypal-payment
              :token="token"
              :amount="selectedDonationAmount"
              :recurring="monthlyDonation"
              @ready="onPaymentReady"
              @payment-start="paymentInProgress = true"
              @success="paymentSuccess"
              @error="paymentError"
            />
          </template>
          <template v-if="payment === 'upn'">
            <upn-payment
              :amount="selectedDonationAmount"
              @ready="onUPNPaymentReady"
              @success="paymentSuccess"
            />
          </template>
          <div class="cart-total">
            <span>Znesek za plačilo</span>
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
            text="DONIRAJ"
            color="secondary"
            arrow
            hearts
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
import DonationOption from '~/components/DonationOption.vue';
import CheckoutStage from '~/components/CheckoutStage.vue';
import DynamicLink from '~/components/DynamicLink.vue';

// https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email#Validation
const EMAIL_REGEX =
  /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;

export default {
  nuxtI18n: {
    paths: {
      sl: '/doniraj_parlameter/placaj/:monthly',
      en: '/donate_parlameter/checkout/:monthly',
    },
  },
  components: {
    ConfirmButton,
    PaymentSwitcher,
    CardPayment,
    PaypalPayment,
    UpnPayment,
    DonationOption,
    CheckoutStage,
    DynamicLink,
  },
  layout: 'checkout',
  pageColor: 'secondary',
  data() {
    const monthlyDonation =
      this.$route.params.monthly === 'monthly' ||
      this.$route.params.monthly === 'mesecno';
    const campaignStringId = this.$route.query.campaign;
    const campaign = ['1', '2', '3'].includes(campaignStringId)
      ? Number(campaignStringId)
      : 1;
    return {
      error: null,
      stage: 'select-amount',
      donationPresets: [
        {
          amount: 5,
          description: '',
          selected: false,
          eventName: 'five',
          monthly: true,
          oneTime: false,
        },
        {
          amount: 11,
          description: '',
          selected: false,
          eventName: 'eleven',
          monthly: true,
          oneTime: true,
        },
        {
          amount: 24,
          description: '',
          selected: false,
          eventName: 'twentyfour',
          monthly: true,
          oneTime: true,
        },
        {
          amount: 47,
          description: '',
          selected: false,
          eventName: 'fortyseven',
          monthly: true,
          oneTime: true,
        },
        {
          amount: 101,
          description: '',
          selected: false,
          eventName: 'whale',
          monthly: false,
          oneTime: true,
        },
        {
          custom: true,
          amount: null,
          description: 'Vnesi poljuben znesek!',
          selected: false,
          eventName: 'aeleven',
          monthly: true,
          oneTime: true,
        },
      ],
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
      monthlyDonation,
      campaign,
      hasUpn: true,
      answer: '',
      honeyPotName: '',
    };
  },
  computed: {
    filteredDonationPresets() {
      return this.donationPresets.filter((dp) =>
        this.monthlyDonation
          ? dp.monthly === this.monthlyDonation
          : dp.oneTime !== this.monthlyDonation,
      );
    },
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
    paymentError(argument) {
      // eslint-disable-next-line
      console.log('ERROR VERY ERROR');
      // eslint-disable-next-line
      console.log(argument);
    },
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
          if (this.honeyPotName !== '') {
            this.error = 'Preveč medu.';
            this.$emit('error', 'Preveč medu.');
          } else {
            try {
              this.checkoutLoading = true;
              const checkoutResponse = await this.$axios.$get(
                `https://podpri.djnd.si/api/generic-donation/${
                  this.campaign
                }/?question_id=1&answer=${encodeURIComponent(this.answer)}`,
              );
              this.token = checkoutResponse.token;
              this.customerId = checkoutResponse.customer_id;
              this.stage = 'payment';
            } catch (error) {
              // eslint-disable-next-line no-console
              console.error(error.response);
              this.error = error.response;
            }
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
      const paymentURL = this.monthlyDonation
        ? `https://podpri.djnd.si/api/generic-donation/subscription/${this.campaign}/`
        : `https://podpri.djnd.si/api/generic-donation/${this.campaign}/`;
      try {
        await this.$axios.$post(paymentURL, {
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
          this.localePath({
            name: 'donate-thanks_parlameter',
            query: { campaign: this.campaign },
          }),
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
.lonec-medu {
  display: none !important;
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
      background-color: rgba($color-red, 0.15);
      padding: 0.5rem 1rem;
      margin: auto auto 0 auto;
      margin-top: 1.5rem;
      margin-bottom: 1rem;
      width: 100%;
      max-width: 350px;

      i {
        font-weight: 600;
        font-size: 1.25rem;
        margin-left: 0.25rem;
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

.checkout.checkout--parlameter /deep/ {
  .donation-option {
    .donation-option__content-wrapper {
      background-image: linear-gradient(-218deg, #d9e7ed 0%, #d9e7ed 100%);
      border-color: rgba(#197197, 0.2);

      .donation-option__icon {
        .icon {
          color: #197197;
        }
      }
    }

    &:focus,
    &.donation-option--selected {
      .donation-option__content-wrapper {
        border-color: #197197;
        box-shadow: 0 0 0 0.2rem rgba(#197197, 0.25);
      }
      path.circle {
        fill: $white;
        stroke-width: 0;
      }
      path.checkmark {
        fill: #197197;
        stroke-width: 0;
      }
    }
  }

  .confirm-button {
    background-color: #197197;
  }

  .form-control:focus,
  .form-control.focus {
    border-color: #197197;
    box-shadow: 0 0 0 0.2rem rgba(#197197, 0.25);
  }

  .payment-switcher .nav .nav-item .nav-link {
    &.active {
      background-color: #197197;
      color: #fff;
    }
    &:focus {
      outline: 5px auto rgba(#197197, 0.25);
    }
  }

  .payment-container .cart-total {
    background-color: transparent;
    background-image: linear-gradient(-218deg, #d9e7ed 0%, #d9e7ed 100%);
  }
}
</style>
