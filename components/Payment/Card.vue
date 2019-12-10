<template>
  <div class="card-payment">
    <div v-if="error" class="alert alert-danger">{{ error }}</div>
    <form v-else>
      <div class="form-group">
        <div
          id="cc-number"
          :class="['form-control', 'form-control-lg', { focus: numberFocused }]"
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
      <div v-if="!paymentInProgress" class="confirm-button-container">
        <confirm-button
          :disabled="!formValid"
          @click.native="payWithCreditCard"
          text="Plačaj"
          color="secondary"
          arrow
          hearts
        />
      </div>
      <template v-else>
        <div class="loader-container load-container--small">
          <div class="lds-dual-ring" />
        </div>
      </template>
    </form>
  </div>
</template>

<script>
import ConfirmButton from '~/components/ConfirmButton.vue';

let braintree = null;
if (typeof window !== 'undefined') {
  braintree = require('braintree-web');
}

export default {
  components: {
    ConfirmButton,
  },
  props: {
    token: {
      type: String,
      required: true,
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
    };
  },
  async mounted() {
    if (braintree) {
      try {
        const clientInstance = await braintree.client.create({
          authorization: this.token,
        });
        const placeholderStyle = {
          'font-style': 'italic',
          'font-weight': '300',
          color: '#444',
          'text-decoration': 'underline',
        };
        const options = {
          client: clientInstance,
          styles: {
            input: {
              'font-size': '19.2px',
              'font-family':
                '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif',
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
              placeholder: 'Številka kartice',
            },
            expirationDate: {
              selector: '#cc-expirationDate',
              placeholder: 'Rok veljavnosti',
            },
            cvv: {
              selector: '#cc-cvv',
              placeholder: 'CVV',
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
        });
        this.hostedFieldsInstance.on('inputSubmitRequest', () => {
          this.payWithCreditCard();
        });
      } catch (error) {
        // eslint-disable-next-line no-console
        console.error(error);
        this.error = error.message;
      }
    }
  },
  methods: {
    payWithCreditCard() {
      if (this.hostedFieldsInstance && !this.paymentInProgress) {
        this.paymentInProgress = true;
        this.error = null;
        this.hostedFieldsInstance
          .tokenize()
          .then((payload) => {
            this.$emit('success', { nonce: payload.nonce });
          })
          .catch((error) => {
            // eslint-disable-next-line no-console
            console.error(error);
            this.error = error.message;
          });
      }
    },
  },
};
</script>

<style lang="scss" scoped>
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
</style>
