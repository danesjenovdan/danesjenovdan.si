<template>
  <div class="newsletter-container">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h1><strong>Prijavi se</strong> na naš Občasnik!</h1>
        <p>
          Vsak mesec ti bomo dostavili svežo bero informativnih vsebin in
          zanimivih zapisov o temah, ki nas žulijo, razveseljujejo ali
          navdihujejo, pisali pa ti bomo tudi, ko naredimo kaj dobrega ali ko se
          bo dogajalo kaj zanimivega.
        </p>
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-xl-8">
        <form
          v-if="$i18n.locale === 'sl'"
          class="mt-3 mt-xl-0"
          @submit.prevent="submitForm"
        >
          <div class="form-group">
            <input
              v-model="email"
              type="email"
              class="form-control my-2 m-lg-2"
              placeholder="Vpiši svoj e-naslov"
            />
            <more-button
              :text="'Prijavi me!'"
              :disabled="loading || !emailValid"
              class="my-2 m-lg-2"
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
  asyncData({ query }) {
    let email = '';
    if (query.email) {
      email = query.email;
    }
    return {
      email,
    };
  },
  data() {
    return {
      loading: false,
      success: false,
      message: '',
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
          this.message =
            'Hvala! Poslali smo ti sporočilo s povezavo, na kateri lahko potrdiš prijavo!';
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
    font-weight: 300;
    font-size: 36px;
    line-height: 40px;
    margin-bottom: 20px;
  }

  p {
    text-align: center;
    font-weight: 300;
    font-size: 18px;
    line-height: 20px;
  }

  .form-group {
    text-align: center;
    margin-top: 2rem;

    @include media-breakpoint-up(lg) {
      text-align: left;
      display: flex;
    }

    input.form-control {
      height: unset;
      font-size: 20px;
      flex-grow: 1;
      padding: 0.75rem 1.75rem 0.75rem 1.5rem;
    }

    .more-button {
      width: unset;
      flex-shrink: 0;
      color: #333;
      font-size: 30px;
      line-height: 40px;
      font-style: normal;
      letter-spacing: normal;
    }
  }

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
