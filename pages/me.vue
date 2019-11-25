<template>
  <div class="me-container">
    <p class="lead">
      <strong>Danes je nov dan</strong> je neprofiten inštitut,
      ki skrbi za varen, vključujoč in sodoben splet
      − in svet. Ne trolamo, ne pošiljamo neželene
      pošte, ne težimo in ne žicamo.
    </p>
    <p class="lead">
      Radi bi ti pisali, kadar naredimo kaj dobrega,
      kadar se dogaja kaj pomembnega, radi bi te
      spoznali z dnevnimi agrumenti, novostmi na
      Parlametru in drugimi projekti.
    </p>
    <div v-if="showForm" class="row justify-content-center">
      <div class="col form-col">
        <p>
          Da bomo vedeli, čigave nastavitve urejaš, prosimo vpiši svoj e-naslov. Na ta naslov ti
          bomo poslali personalizirano povezavo do spletne strani za urejanje nastavitev.
        </p>
        <form @submit.prevent="submitForm">
          <input
            v-if="!success"
            v-model="email"
            type="email"
            class="form-control mt-4 mb-4"
            placeholder="Vpiši svoj e-naslov"
          />
          <p v-if="message">
            <strong>{{ message }}</strong>
          </p>
          <more-button
            v-if="!success"
            :disabled="loading || !email.length || email.indexOf('@') === -1"
            icon="heart"
            :to="localePath('me')"
            :text="'POTRDI'"
            @click.native="submitForm"
          />
        </form>
      </div>
    </div>
    <div v-else-if="settings" class="row">
      <div v-for="key in settingKeys" :key="key">
        <h2>{{ key }}</h2>
        <div class="custom-control custom-switch">
          <input :id="`switch-${key}`" type="checkbox" class="custom-control-input" />
          <label :for="`switch-${key}`" class="custom-control-label">Toggle this switch element</label>
        </div>
        {{ settings[key].name }}
      </div>
    </div>
  </div>
</template>

<script>
import MoreButton from '~/components/MoreButton.vue';

export default {
  pageColor: 'primary',
  nuxtI18n: {
    paths: {
      sl: '/jaz',
      en: '/me',
    },
  },
  layout: 'checkout',
  components: {
    MoreButton,
  },
  data() {
    return {
      email: '',
      loading: false,
      success: false,
      message: '',
    };
  },
  computed: {
    settingKeys() {
      if (!this.settings) {
        return [];
      }
      return Object.keys(this.settings);
    },
  },
  async asyncData({ $axios, query }) {
    let showForm = true;
    let settings = null;
    let name = null;
    if (query.email && query.token) {
      const token = encodeURIComponent(query.token);
      const email = encodeURIComponent(query.email);
      const endpoint = `https://spam.djnd.si/get-settings/?token=${token}&email=${email}`;
      const response = await $axios.$get(endpoint);
      if (response && typeof response === 'object') {
        showForm = false;
        ({ name, ...settings } = response);
      }
    }
    return {
      showForm,
      settings,
      name,
    };
  },
  methods: {
    async submitForm() {
      if (!this.loading || this.email) {
        this.loading = true;
        try {
          const response = await this.$axios.$get(
            `https://spam.djnd.si/deliver-email/?email=${this.email}`,
          );
          // axios can return a number, so cast to string just in case
          if (String(response) === '1') {
            this.success = true;
            this.message = 'Sporočilo poslano na e-naslov!';
          } else {
            this.success = false;
            this.message = 'Prišlo je do napake :(';
          }
        } catch {
          this.success = false;
          this.message = 'Prišlo je do napake :(';
        } finally {
          this.loading = false;
        }
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.me-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;

  .lead {
    margin-top: 1.25rem;
    margin-bottom: 2rem;
    font-size: 1.75rem;
    font-weight: 200;
    line-height: 1.3;

    @include media-breakpoint-up(lg) {
      font-size: 3rem;
      line-height: 1.1;
    }

    strong {
      font-weight: 600;
    }
  }

  .form-col {
    max-width: 550px;
    margin-bottom: 1.5rem;

    @include media-breakpoint-up(lg) {
      text-align: center;
    }

    p {
      font-size: 1.25rem;
      font-weight: 200;
    }

    .more-button {
      width: 100%;

      @include media-breakpoint-up(lg) {
        width: auto;
      }
    }
  }
}
</style>
