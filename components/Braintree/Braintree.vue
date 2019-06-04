<template>
  <div>
    <hosted-fields
      wrapper-class="constrain"
      :auth-token="'sandbox_g42y39zw_348pk9cgf3bgyw2b'"
      :collect-card-holder-name="false"
      :collect-postal-code="false"
      :enable-data-collector="false"
      @bthferror="btHFError"
      @bthfpayload="btHFPayload"
    />
    <button @click="submitTransaction">Submit</button>
  </div>
</template>

<script>
import HostedFields from 'vue-braintree-hosted-fields';

export default {
  components: {
    HostedFields,
  },
  methods: {
    btHFError(message) {
      console.error('message------', message);
      // do something with the error message
    },
    btHFPayload(payload) {
      console.log('payload------', payload);
      // do something with the token payload
    },
    submitTransaction() {
      this.$emit('tokenize');
    },
  },
};
</script>

<style lang="scss" scoped>
/deep/ {
  label {
    font-size: 16px;
    display: block;
    text-align: left;
    font-weight: bold;
    padding: 0.25rem;
  }

  .input-field {
    height: 50px;
    box-sizing: border-box;
    width: 100%;
    padding: 0.8rem;
    display: inline-block;
    box-shadow: none;
    font-weight: 600;
    font-size: 0.8rem;
    border-radius: 6px;
    border: 1px solid #dddddd;
    line-height: 1.2;
    background: #fcfcfc;
    margin-top: 0.1rem;
    margin-bottom: 0.8rem;
    background: linear-gradient(to right, white 50%, #fcfcfc 50%);
    background-size: 200% 100%;
    background-position: right bottom;
    transition: all 300ms ease-in-out;
    font-size: 18px;
    text-align: left;
  }
}
</style>
