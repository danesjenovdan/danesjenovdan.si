<template>
  <div class="card-payment">
    <payment-error v-if="error" />
    <template v-else>
      <form>
        <div class="form-group">
          <div class="lonec-medu">
            <input
              type="text"
              name="name"
              placeholder="Your full name please"
              v-model="honeyPotName"
            />
            <input
              type="text"
              name="address"
              placeholder="Your address please"
              v-model="honeyPotAddress"
            />
            <input
              type="text"
              name="post"
              placeholder="Your postal code and office name please"
              v-model="honeyPotPost"
            />
          </div>
          <div
            id="cc-number"
            :class="[
              'form-control',
              'form-control-lg',
              { focus: numberFocused },
            ]"
          />
        </div>
        <div class="form-group">
          <div
            id="cc-expirationDate"
            :class="[
              'form-control',
              'form-control-lg',
              { focus: expirationDateFocused },
            ]"
          />
        </div>
        <div class="form-group">
          <div
            id="cc-cvv"
            :class="['form-control', 'form-control-lg', { focus: cvvFocused }]"
          />
        </div>
      </form>
      <div class="card-info">
        Informacij o tvoji kartici ne pošiljamo na svoj strežnik in ne
        shranjujemo. Za varnost plačila skrbi
        <br />
        <img
          src="https://s3.amazonaws.com/braintree-badges/braintree-badge-light.png"
          width="164px"
          height="44px"
          border="0"
        />
      </div>
    </template>
  </div>
</template>

<script>
import PaymentError from './Error.vue';

let braintree = null;
if (typeof window !== 'undefined') {
  braintree = require('braintree-web');
}

export default {
  components: {
    PaymentError,
  },
  props: {
    token: {
      type: String,
      required: true,
    },
    forceSlovenian: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      hostedFieldsInstance: null,
      error: null,
      numberFocused: false,
      expirationDateFocused: false,
      cvvFocused: false,
      formValid: false,
      paymentInProgress: false,
      honeyPotName: '',
      honeyPotAddress: '',
      honeyPotPost: '',
    };
  },
  async mounted() {
    if (this.forceSlovenian) {
      this.$i18n.locale = 'sl';
    }
    if (braintree) {
      try {
        const clientInstance = await braintree.client.create({
          authorization: this.token,
        });
        const placeholderStyle = {
          // 'font-style': 'italic',
          // 'font-weight': '300',
          color: '#444',
          // 'text-decoration': 'underline',
        };
        const options = {
          client: clientInstance,
          styles: {
            input: {
              'font-size': '19.2px',
              'font-family': 'monospace',
            },
            'input.invalid': {
              color: '#dd786b',
            },
            // placeholder styles need to be individually adjusted
            '::-webkit-input-placeholder': placeholderStyle,
            '::-ms-input-placeholder': placeholderStyle,
            '::placeholder': placeholderStyle,
          },
          fields: {
            number: {
              selector: '#cc-number',
              placeholder: this.$t('shop.checkout.cardNumber'),
            },
            expirationDate: {
              selector: '#cc-expirationDate',
              placeholder: this.$t('shop.checkout.expirationDate'),
            },
            cvv: {
              selector: '#cc-cvv',
              placeholder: this.$t('shop.checkout.cvv'),
            },
          },
        };
        this.hostedFieldsInstance = await braintree.hostedFields.create(
          options,
        );

        this.hostedFieldsInstance.on('focus', (event) => {
          this[`${event.emittedBy}Focused`] = true;
        });
        this.hostedFieldsInstance.on('blur', (event) => {
          this[`${event.emittedBy}Focused`] = false;
        });
        this.hostedFieldsInstance.on('validityChange', (event) => {
          const formValid = Object.keys(event.fields).every((key) => {
            return event.fields[key].isValid;
          });
          this.formValid = formValid;
          this.$emit('validity-change', formValid);
        });
        this.hostedFieldsInstance.on('inputSubmitRequest', () => {
          this.payWithCreditCard();
        });

        this.$emit('ready', { pay: this.payWithCreditCard });
      } catch (error) {
        // eslint-disable-next-line no-console
        console.error(error);
        this.error = error.message;
        this.$emit('error', { error });
      }
    }
  },
  methods: {
    payWithCreditCard() {
      if (
        this.honeyPotName !== '' ||
        this.honeyPotAddress !== '' ||
        this.honeyPotPost !== ''
      ) {
        this.error = 'Preveč medu.';
        this.$emit('error', 'Preveč medu.');
      } else if (this.hostedFieldsInstance && !this.paymentInProgress) {
        this.paymentInProgress = true;
        this.$emit('payment-start');
        this.error = null;
        this.hostedFieldsInstance
          .tokenize({
            vault: true,
          })
          .then((payload) => {
            this.$emit('success', { nonce: payload.nonce });
          })
          .catch((error) => {
            // eslint-disable-next-line no-console
            console.error(error);
            this.error = error.message;
            this.$emit('error', { error });
          });
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.lonec-medu {
  display: none !important;
}
.card-payment {
  width: 100%;
  max-width: 350px;
  margin: 0 auto;

  .focus {
    border: 1px solid $color-red;
    box-shadow: 0 0 0 0.2rem rgba($color-red, 0.25);
  }

  .confirm-button-container {
    margin-top: 2rem;
    text-align: center;
  }

  .loader-container {
    display: flex;
    justify-content: center;
    margin: 3rem 0;

    &.load-container--small {
      margin: 1rem 0;
    }
  }

  .card-info {
    font-weight: 300;
    font-size: 1rem;
    text-align: center;

    img {
      margin-top: 0.5rem;
    }
  }
}
</style>
