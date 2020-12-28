<template>
  <div class="paypal-payment">
    <payment-error v-if="error" />
    <form v-else>
      <div class="form-group">
        <label v-t="'shop.checkout.paypalContinue'"></label>
        <div id="paypal-button" />
      </div>
      <div v-if="warning" class="form-group">
        <div class="alert alert-warning">{{ warning }}</div>
      </div>
    </form>
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
    amount: {
      type: Number,
      required: true,
    },
    recurring: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      hostedFieldsInstance: null,
      error: null,
      warning: null,
    };
  },
  async mounted() {
    if (braintree) {
      try {
        const clientInstance = await braintree.client.create({
          authorization: this.token,
        });
        const options = {
          client: clientInstance,
        };
        const paypalCheckoutInstance = await braintree.paypalCheckout.create(
          options,
        );
        const paypalSDKOptions = this.recurring
          ? { currency: 'EUR', vault: true }
          : { currency: 'EUR', intent: 'capture' };
        await paypalCheckoutInstance.loadPayPalSDK(paypalSDKOptions);
        await window.paypal
          .Buttons({
            fundingSource: window.paypal.FUNDING.PAYPAL,
            style: {
              tagline: false,
            },
            createOrder: this.recurring
              ? undefined
              : () => {
                  return paypalCheckoutInstance.createPayment({
                    flow: 'checkout',
                    intent: 'capture',
                    amount: this.amount,
                    displayName: 'Danes je nov dan',
                    currency: 'EUR',
                  });
                },
            createBillingAgreement: this.recurring
              ? () => {
                  return paypalCheckoutInstance.createPayment({
                    flow: 'vault',
                    amount: this.amount,
                    displayName: 'Danes je nov dan',
                    currency: 'EUR',
                  });
                }
              : undefined,
            onApprove: (data) => {
              this.warning = null;
              this.$emit('payment-start');
              return paypalCheckoutInstance.tokenizePayment(
                data,
                (error, payload) => {
                  if (error) {
                    // eslint-disable-next-line no-console
                    console.error(error);
                    this.error = error;
                    this.$emit('error', { error });
                  } else {
                    this.$emit('success', { nonce: payload.nonce });
                  }
                },
              );
            },
            onCancel: (data) => {
              this.warning = 'Payment Cancelled';
            },
            onError: (error) => {
              this.warning = null;
              // eslint-disable-next-line no-console
              console.error(error);
              this.error = error.message;
              this.$emit('error', { error });
            },
          })
          .render('#paypal-button');
        this.$emit('ready');
      } catch (error) {
        // eslint-disable-next-line no-console
        console.error(error);
        this.error = error.message;
        this.$emit('error', { error });
      }
    }
  },
};
</script>

<style lang="scss" scoped>
.paypal-payment {
  width: 100%;
  max-width: 350px;
  margin: 0 auto;

  label {
    font-size: 1.25rem;
    font-weight: 300;
    text-align: center;
    display: block;
  }
}
</style>
