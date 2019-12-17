<template>
  <div class="card-payment">
    <div v-if="error" class="alert alert-danger">{{ error }}</div>
    <form v-else>
      <div class="form-group">
        <label>Nadaljuj s klikom na gumb</label>
        <div id="paypal-button" />
      </div>
    </form>
  </div>
</template>

<script>
let braintree = null;
let paypal = null;
if (typeof window !== 'undefined') {
  braintree = require('braintree-web');
  paypal = require('paypal-checkout');
}

export default {
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
            onAuthorize: (data, options) => {
              this.$emit('payment-start');
              return paypalCheckoutInstance
                .tokenizePayment(options)
                .then((payload) => {
                  this.error = null;
                  this.$emit('success', { nonce: payload.nonce });
                });
            },
            onCancel: (data) => {
              this.error = 'Payment Cancelled';
            },
            onError: (error) => {
              // eslint-disable-next-line no-console
              console.error(error);
              this.error = error.message;
            },
          },
          '#paypal-button',
        );
        this.$emit('ready');
      } catch (error) {
        // eslint-disable-next-line no-console
        console.error(error);
        this.error = error.message;
      }
    }
  },
};
</script>

<style lang="scss" scoped>
label {
  font-size: 1.25rem;
  font-weight: 300;
  text-align: center;
  display: block;
}
</style>
