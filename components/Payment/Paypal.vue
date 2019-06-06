<template>
  <div class="card-payment">
    <div v-if="error" class="alert alert-danger">{{ error }}</div>
    <div v-if="nonce" class="alert alert-success">Successfully generated nonce.</div>
    <form v-else>
      <div class="form-group">
        <label>Nadaljuj s klikom na gumb</label>
        <div id="paypal-button"/>
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
  data() {
    return {
      hostedFieldsInstance: null,
      nonce: null,
      error: null,
    };
  },
  async mounted() {
    if (braintree && paypal) {
      try {
        const clientInstance = await braintree.client.create({
          authorization: 'sandbox_93smtrz3_bbgx4xf7h8bx24xg',
        });
        const options = {
          client: clientInstance,
        };
        const paypalCheckoutInstance = await braintree.paypalCheckout.create(options);
        return paypal.Button.render(
          {
            env: 'sandbox', // TODO: production
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
                amount: 10, // TODO: proper amount
                displayName: 'Danes je nov dan',
                currency: 'EUR',
              });
            },
            onAuthorize: (data, options) => {
              return paypalCheckoutInstance.tokenizePayment(options).then(payload => {
                this.error = null;
                this.nonce = payload.nonce;
              });
            },
            onCancel: data => {
              this.error = 'Payment Cancelled';
            },
            onError: error => {
              // eslint-disable-next-line no-console
              console.error(error);
              this.error = error.message;
            },
          },
          '#paypal-button',
        );
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
