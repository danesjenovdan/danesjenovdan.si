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
let paypal = null;
if (typeof window !== 'undefined') {
  braintree = require('braintree-web');
  paypal = require('paypal-checkout');
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
  },
  data() {
    return {
      hostedFieldsInstance: null,
      error: null,
      warning: null,
    };
  },
  async mounted() {
    if (braintree && paypal) {
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
        await paypal.Button.render(
          {
            env: 'production',
            style: {
              label: 'paypal',
              size: 'responsive',
              shape: 'rect',
              tagline: false,
            },
            payment: () => {
              return paypalCheckoutInstance.createPayment({
                flow: 'checkout',
                intent: 'sale',
                amount: this.amount,
                displayName: 'Danes je nov dan',
                currency: 'EUR',
              });
            },
            onAuthorize: (data, actions) => {
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
          },
          '#paypal-button',
        );
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
