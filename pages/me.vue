<template>
  <div class="me-container">
    <div class="row justify-content-center">
      <div class="col-xl-10">
        <div class="intro">
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
        </div>
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
                class="form-control form-control-lg mt-4 mb-4"
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
                large
                @click.native="submitForm"
              />
            </form>
          </div>
        </div>
        <template v-else-if="settings">
          <div class="row justify-content-center">
            <div class="col form-col">
              <p>
                <strong>{{ email }}</strong>, pripravili smo vse možne različne scenarije bodoče e-komunikacije s
                tabo, ti pa se moraš le opredeliti do vsakega od njih!
              </p>
            </div>
          </div>
          <div class="row justify-content-center">
            <div v-for="key in settingKeys" :key="key" class="col-12 settings-col">
              <email-subscription-tile
                :title="$t(`me.settings.${key}.title`)"
                :description="$t(`me.settings.${key}.description`)"
                :icon="key"
                :color="meta[key].color"
                :label-off="$t(`me.settings.${key}.label-off`)"
                :label-on="$t(`me.settings.${key}.label-on`)"
                :checked="settings[key].permission"
                :loading="meta[key].loading"
                @change="onSettingChange(key, $event)"
              >
                <div v-if="key === 'konsenz'">
                  <input
                    v-model="name"
                    type="text"
                    class="form-control name-input"
                    :placeholder="$t(`me.settings.${key}.enter-name`)"
                  />
                </div>
              </email-subscription-tile>
            </div>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import MoreButton from '~/components/MoreButton.vue';
import EmailSubscriptionTile from '~/components/EmailSubscriptionTile.vue';

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
    EmailSubscriptionTile,
  },
  data() {
    return {
      loading: false,
      success: false,
      message: '',
      meta: {
        supporter: {
          show: true,
          color: 'secondary',
          order: 100,
          loading: false,
        },
        pp: {
          show: false,
          order: 200,
          loading: false,
        },
        agrument: {
          show: true,
          color: 'primary',
          order: 300,
          loading: false,
        },
        djnd: {
          show: true,
          color: 'secondary',
          order: 400,
          loading: false,
        },
        parlameter: {
          show: true,
          color: 'parlameter',
          order: 500,
          loading: false,
        },
        konsenz: {
          show: true,
          color: 'primary',
          order: 600,
          loading: false,
        },
      },
    };
  },
  computed: {
    settingKeys() {
      if (!this.settings) {
        return [];
      }
      return Object.keys(this.settings)
        .filter(a => this.meta[a] && this.meta[a].show)
        .sort((a, b) => this.meta[a].order - this.meta[b].order);
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
      email: query.email || '',
      token: query.token || '',
    };
  },
  methods: {
    async submitForm() {
      if (!this.loading && this.email && this.email.indexOf('@') !== -1) {
        this.loading = true;
        try {
          const response = await this.$axios.$get('https://spam.djnd.si/deliver-email/', {
            params: {
              email: this.email,
            },
          });
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
    async onSettingChange(key, newValue) {
      const params = {
        token: this.token,
        email: this.email,
        permission: newValue,
      };
      if (key === 'konsenz') {
        if (!this.name) {
          alert(this.$t(`me.settings.${key}.invalid-name`));
          return;
        }
        params.name = this.name;
      }
      try {
        this.meta[key].loading = true;
        const response = await this.$axios.$get(`https://spam.djnd.si/confirm-${key}/`, {
          params,
        });
        // axios can return a number, so cast to string just in case
        if (String(response) === '1') {
          this.settings[key].permission = newValue;
        } else {
          this.settings[key].permission = newValue;
          this.$nextTick(() => {
            this.settings[key].permission = !newValue;
          });
        }
      } catch {
        this.settings[key].permission = newValue;
        this.$nextTick(() => {
          this.settings[key].permission = !newValue;
        });
      } finally {
        this.meta[key].loading = false;
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
  padding-top: 1.25rem;

  .intro {
    @include media-breakpoint-up(lg) {
      margin: 0 0 6rem;
    }

    .lead {
      margin-bottom: 2rem;
      font-size: 1.75rem;
      font-weight: 200;
      line-height: 1.3;

      @include media-breakpoint-up(lg) {
        font-size: 2.5rem;
        line-height: 1.1;
      }

      strong {
        font-weight: 600;
      }
    }
  }

  .form-col {
    max-width: 550px;
    margin-bottom: 1.5rem;

    @include media-breakpoint-up(md) {
      text-align: center;
    }

    p {
      font-size: 1.25rem;
      font-weight: 200;
      line-height: 1.2;
      margin-bottom: 2rem;
    }

    .more-button {
      width: 100%;

      @include media-breakpoint-up(md) {
        width: auto;
      }
    }
  }

  .name-input {
    margin-top: 1.5rem;
  }
}
</style>
