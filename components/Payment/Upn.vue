<template>
  <div class="upn-payment">
    <div v-if="error" class="alert alert-danger">{{ error }}</div>
    <form v-else>
      <div class="form-group">
        <label>Po e-pošti ti bomo poslali položnico</label>
      </div>
      <more-button
        :to="localePath('shop-checkout')"
        :text="'KUPI'"
        block
        color="secondary"
        icon="heart"
        @click.native="sendUPN"
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
  data() {
    return {
      error: null,
    };
  },
  mounted() {
    this.$emit('ready');
  },
  methods: {
    sendUPN() {
      // eslint-disable-next-line no-console
      this.$emit('success');
    },
  },
};
</script>

<style lang="scss" scoped>
.upn-payment {
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
