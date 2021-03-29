<template>
  <div class="me-container">
    <div class="row justify-content-center">
      <div class="col-xl-10">
        <div class="intro">
          <p class="lead">
            <strong>Danes je nov dan</strong> je neprofiten inštitut, ki skrbi
            za varen, vključujoč in sodoben splet − in svet. Ne trolamo, ne
            pošiljamo neželene pošte, ne težimo in ne žicamo.
          </p>
          <p class="lead">
            Radi bi ti pisali, kadar naredimo kaj dobrega, kadar se dogaja kaj
            pomembnega, radi bi te spoznali z dnevnimi agrumenti, novostmi in
            aktualnimi projekti.
          </p>
        </div>
        <div v-if="showForm" class="row justify-content-center">
          <div class="col form-col">
            <p>
              Da bomo vedeli, čigave nastavitve urejaš, prosimo vpiši svoj
              e-naslov. Na ta naslov ti bomo poslali personalizirano povezavo do
              spletne strani za urejanje nastavitev. Sporočilo bo prispelo na
              tvoj naslov v roku 30 minut.
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
                :disabled="
                  loading || !email.length || email.indexOf('@') === -1
                "
                :to="localePath('me')"
                :text="'POTRDI'"
                icon="heart"
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
                <strong>{{ email }}</strong
                >, pripravili smo vse možne različne scenarije bodoče
                e-komunikacije s tabo, ti pa se moraš le opredeliti do vsakega
                od njih!
              </p>
            </div>
          </div>
          <div class="row justify-content-center">
            <div
              v-for="key in settingKeys"
              :key="key"
              class="col-12 settings-col"
            >
              <email-subscription-tile
                :title="$t(`me.settings.${key}.title`)"
                :description="$t(`me.settings.${key}.description`)"
                :icon="key"
                :color="meta[key].color"
                :label-off="$t(`me.settings.${key}.label-off`)"
                :label-on="$t(`me.settings.${key}.label-on`)"
                :checked="settings[key]"
                :loading="meta[key].loading"
                @change="onSettingChange(key, $event)"
              >
                <div v-if="key === 'konsenz'">
                  <input
                    v-model="name"
                    :placeholder="$t(`me.settings.${key}.enter-name`)"
                    type="text"
                    class="form-control name-input"
                  />
                </div>
              </email-subscription-tile>
            </div>
            <more-button :text="'SHRANI'" large @click.native="onSaveClick" />
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
  components: {
    MoreButton,
    EmailSubscriptionTile,
  },
  layout: 'checkout',
  async asyncData({ $axios, query, error }) {
    let showForm = true;
    const settings = {
      agrument: false,
      general: false,
      parlameter: false,
    };
    if (query.email && query.token) {
      console.log('I CAN HAS STUFF');
      const token = encodeURIComponent(query.token);
      const email = encodeURIComponent(query.email);
      const endpoint = `https://podpri.djnd.si/api/segments/my?token=${token}&email=${email}`;
      console.log(endpoint);
      try {
        const response = await $axios.$get(endpoint);
        if (response && typeof response === 'object') {
          showForm = false;
          response.segments.forEach((s) => {
            settings[s.alias] = s.manuallyAdded;
          });
        }
      } catch (err) {
        if (err.response) {
          error({
            statusCode: err.response.status,
            message: err.response.data,
          });
          return;
        }
        error({ statusCode: 500, message: err.message });
        return;
      }
    }
    return {
      showForm,
      settings,
      email: query.email || '',
      token: query.token || '',
    };
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
        agrument: {
          show: true,
          color: 'primary',
          order: 200,
          loading: false,
        },
        general: {
          show: true,
          color: 'secondary',
          order: 300,
          loading: false,
        },
        parlameter: {
          show: true,
          color: 'parlameter',
          order: 400,
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
        .filter((a) => this.meta[a] && this.meta[a].show)
        .sort((a, b) => this.meta[a].order - this.meta[b].order);
    },
  },
  methods: {
    async submitForm() {
      if (!this.loading && this.email && this.email.includes('@')) {
        this.loading = true;
        try {
          const response = await this.$axios.$post(
            'https://podpri.djnd.si/api/subscribe/',
            {
              email: this.email,
            },
          );
          if (response.msg === 'mail sent') {
            this.success = true;
            this.message = 'Sporočilo poslano!';
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
      try {
        this.meta[key].loading = true;
        const reqUrl = `https://podpri.djnd.si/api/segments/${key}/contact/?email=${this.email}&token=${this.token}`;
        const response = newValue
          ? await this.$axios.$post(reqUrl)
          : await this.$axios.$delete(reqUrl);
        if (response.success) {
          this.settings[key] = newValue;
        } else {
          this.settings[key] = newValue;
          this.$nextTick(() => {
            this.settings[key] = !newValue;
          });
        }
      } catch {
        this.settings[key] = newValue;
        this.$nextTick(() => {
          this.settings[key] = !newValue;
        });
      } finally {
        this.meta[key].loading = false;
      }
    },
    onSaveClick() {
      alert('Nastavitve so shranjene!');
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
  padding-top: 6em;
  margin-bottom: 2rem;

  @include media-breakpoint-down(sm) {
    padding-top: 3em;
  }

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
