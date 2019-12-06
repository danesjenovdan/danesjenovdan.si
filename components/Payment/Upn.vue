<template>
  <div class="card-payment">
    <div v-if="error" class="alert alert-danger">{{ error }}</div>
    <div v-if="nonce" class="alert alert-success">
      Successfully generated nonce.
    </div>
    <form v-else>
      <div class="form-group">
        <label>Po e-pošti ti bomo poslali položnico</label>
      </div>
      <more-button
        :to="localePath('shop-checkout')"
        :text="'KUPI'"
        @click.native="sendUPN"
        block
        color="secondary"
        icon="heart"
      />
    </form>
  </div>
</template>

<script>
import MoreButton from '~/components/MoreButton.vue';

export default {
  components: {
    MoreButton,
  },
  methods: {
    sendUPN() {
      // eslint-disable-next-line no-console
      console.log('SEND UPN');
    },
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
