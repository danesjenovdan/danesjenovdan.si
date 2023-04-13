<template>
  <div class="newsletter-container">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h1><strong>Prijavi se</strong> na <br />Danes je nov dan novičnik!</h1>
        <p>
          Z zanimivimi temami in novicami te bomo zalagali vsak mesec, pisali pa
          ti bomo tudi, kadar naredimo kaj dobrega in kadar se dogaja kaj
          pomembnega.
        </p>
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-lg-8">
        <form
          v-if="$i18n.locale === 'sl'"
          class="mt-3 mt-xl-0"
          @submit.prevent="submitForm"
        >
          <div class="form-group">
            <input
              v-model="email"
              type="email"
              class="form-control m-2"
              placeholder="Vpiši svoj e-naslov"
            />
            <more-button
              :text="'Prijavi me!'"
              :disabled="loading || !emailValid"
              class="m-2"
              color="secondary"
              block
              to="#"
              @click.native="submitForm"
            />
          </div>
        </form>
      </div>
    </div>
    <div class="row justify-content-center" v-if="loading == true">
      <div class="loader-container">
        <div class="lds-dual-ring" />
      </div>
    </div>
    <div class="row justify-content-center" v-if="message">
      <p>{{ message }}</p>
    </div>
  </div>
</template>

<script>
import MoreButton from '~/components/MoreButton.vue';

export default {
  pageColor: 'primary',
  nuxtI18n: {
    paths: {
      sl: '/novicnik',
      en: '/newsletter',
    },
  },
  components: {
    MoreButton,
  },
  layout: 'default-no-support',
  data() {
    return {
      loading: false,
      success: false,
      message: '',
      email: '',
    };
  },
  computed: {
    emailValid() {
      return this.email && this.email.includes('@');
    },
  },
  methods: {
    async submitForm() {
      this.loading = true;
      this.message = '';
      try {
        const response = await this.$axios.$post(
          'https://podpri.lb.djnd.si/api/subscribe/',
          {
            email: this.email,
            segment_id: 21,
          },
        );
        if (response.msg === 'mail sent') {
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
    },
  },
};
</script>

<style lang="scss" scoped>
.newsletter-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-top: 1.25rem;

  h1 {
    text-align: center;
  }

  p {
    text-align: center;
  }

  .form-group {
    display: flex;

    input.form-control {
      height: 100%;
      flex-grow: 1;
      padding: 0.75rem 1.75rem 0.75rem 1.5rem;
    }

    .more-button {
      width: unset;
      flex-shrink: 0;
    }
  }

  // @include media-breakpoint-up(lg) {
  //   margin: 0 0 6rem;
  // }

  .loader-container {
    height: 2rem;
    line-height: 2rem;

    .lds-dual-ring {
      &,
      &::after {
        width: 2rem;
        height: 2rem;
      }
    }
  }
}
</style>
