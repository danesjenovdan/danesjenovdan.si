<template>
  <div class="container">
    <div class="col-6 offset-3">
      <div class="card bg-light">
        <div class="card-header">Payment Information</div>
        <div class="card-body">
          <div v-if="nonce" class="alert alert-success">
            Successfully generated nonce.
          </div>
          <div v-if="error" class="alert alert-danger">{{ error }}</div>
          <form>
            <div class="form-group">
              <label for="amount">Amount</label>
              <div class="input-group">
                <div class="input-group-prepend">
                  <span class="input-group-text">$</span>
                </div>
                <input
                  id="amount"
                  v-model="amount"
                  type="number"
                  class="form-control"
                  placeholder="Enter Amount"
                />
              </div>
            </div>
            <hr />
            <div class="form-group">
              <label>Credit Card Number</label>
              <div id="creditCardNumber" class="form-control"></div>
            </div>
            <div class="form-group">
              <div class="row">
                <div class="col-6">
                  <label>Expire Date</label>
                  <div id="expireDate" class="form-control"></div>
                </div>
                <div class="col-6">
                  <label>CVV</label>
                  <div id="cvv" class="form-control"></div>
                </div>
              </div>
            </div>
            <button
              @click.prevent="payWithCreditCard"
              class="btn btn-primary btn-block"
            >
              Pay with Credit Card
            </button>
            <hr />
            <div id="paypalButton"></div>
          </form>
        </div>
      </div>
    </div>
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
      hostedFieldInstance: false,
      nonce: '',
      error: '',
      amount: 10,
    };
  },
  mounted() {
    braintree.client
      .create({
        authorization: 'sandbox_93smtrz3_bbgx4xf7h8bx24xg',
      })
      .then((clientInstance) => {
        const options = {
          client: clientInstance,
          styles: {
            input: {
              'font-size': '14px',
              'font-family': 'Open Sans',
            },
          },
          fields: {
            number: {
              selector: '#creditCardNumber',
              placeholder: 'Enter Credit Card',
            },
            cvv: {
              selector: '#cvv',
              placeholder: 'Enter CVV',
            },
            expirationDate: {
              selector: '#expireDate',
              placeholder: '00 / 0000',
            },
          },
        };
        return Promise.all([
          braintree.hostedFields.create(options),
          braintree.paypalCheckout.create({ client: clientInstance }),
        ]);
      })
      .then((instances) => {
        const hostedFieldInstance = instances[0];
        const paypalCheckoutInstance = instances[1];
        // Use hostedFieldInstance to send data to Braintree
        this.hostedFieldInstance = hostedFieldInstance;
        // Setup PayPal Button
        return paypal.Button.render(
          {
            env: 'sandbox',
            style: {
              label: 'paypal',
              size: 'responsive',
              shape: 'rect',
            },
            payment: () => {
              return paypalCheckoutInstance.createPayment({
                flow: 'checkout',
                intent: 'sale',
                amount: parseFloat(this.amount) > 0 ? this.amount : 10,
                displayName: 'Braintree Testing',
                currency: 'USD',
              });
            },
            onAuthorize: (data, options) => {
              return paypalCheckoutInstance
                .tokenizePayment(options)
                .then((payload) => {
                  console.log(payload);
                  this.error = '';
                  this.nonce = payload.nonce;
                });
            },
            onCancel: (data) => {
              console.log(data);
              console.log('Payment Cancelled');
            },
            onError: (err) => {
              console.error(err);
              this.error =
                'An error occurred while processing the paypal payment.';
            },
          },
          '#paypalButton',
        );
      })
      .catch((err) => {
        console.error(err);
      });
  },
  methods: {
    payWithCreditCard() {
      if (this.hostedFieldInstance) {
        this.error = '';
        this.nonce = '';
        this.hostedFieldInstance
          .tokenize()
          .then((payload) => {
            console.log(payload);
            this.nonce = payload.nonce;
          })
          .catch((err) => {
            console.error(err);
            this.error = err.message;
          });
      }
    },
  },
};
</script>

<style lang="scss" scoped></style>
