<template>
  <div class="checkout">
    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <checkout-stage v-if="gift">
      <template slot="title">Koga obdaruješ? ({{ gift.amount }} €)</template>
      <template slot="content">
        <div class="gift-content">
          <div class="form-group row">
            <div class="d-flex align-items-center col-3">
              <span class="name-label">Dragi/-a</span>
            </div>
            <div class="col-9">
              <input
                id="name"
                v-model="name"
                placeholder="[vpiši ime]"
                class="form-control form-control-lg"
              />
            </div>
          </div>
          <div class="form-group">
            <input
              id="email"
              v-model="email"
              type="email"
              placeholder="E-naslov obdarovanca/-ke"
              class="form-control form-control-lg"
            />
          </div>
          <div class="form-group">
            <label for="message" class="message-label">
              Napiši svoje sporočilo ali le uredi naš predlog.
            </label>
            <textarea
              id="message"
              v-model="message"
              type="text"
              placeholder="Sporočilo"
              rows="10"
              class="form-control form-control-lg"
            />
          </div>
        </div>
      </template>
      <template slot="footer">
        <div class="confirm-button-container">
          <confirm-button
            :key="`next-gift-${giftIndex}`"
            :disabled="!canUpdateGift"
            :loading="giftUpdating"
            :text="
              giftIndex === gifts.length - 1
                ? 'Zaključi z obdarovanjem'
                : 'Naslednje darilo'
            "
            color="secondary"
            arrow
            @click.native="updateGift"
          />
        </div>
      </template>
    </checkout-stage>
  </div>
</template>

<script>
import CheckoutStage from '~/components/CheckoutStage.vue';
import ConfirmButton from '~/components/ConfirmButton.vue';

const defaultMessage = `Med prazniki se vse prevečkrat obdarujemo zato, ker se pač tako spodobi, zapravljamo denar za stvari, ki jih obdarovanci ne potrebujejo ali si jih ne želijo, ter tudi sami prejemamo tovrstna darila. Tako v imenu nenapisane dolžnosti prispevamo k hiperprodukciji, onesnaževanju in nepotrebnemu trošenju.

Letos se upiram taki praksi in ti za novo leto podarjam donacijo inštitutu Danes je nov dan v tvojem imenu. Zbirajo za pet različnih aktivističnih projektov z raznolikimi partnerji.

Donatorji lahko na njihovo spletno stran naložijo svojo slikico ali si izberejo katero od prednaloženih. S klikom na to povezavo lahko to urediš zase in deliš svoje darilo na družbenih omrežjih :)

Namesto kupovanja nepotrebnih daril tudi ti rajši prispevaj za tiste socialne problematike, ki so ti najbližje!

Lepo praznuj,`;

// https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email#Validation
const EMAIL_REGEX = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;

export default {
  nuxtI18n: {
    paths: {
      sl: '/doniraj/darila',
      en: '/donate/gifts',
    },
  },
  layout: 'checkout',
  pageColor: 'secondary',
  components: {
    CheckoutStage,
    ConfirmButton,
  },
  async asyncData({ query, $axios }) {
    const token = query.token;
    const giftsResponse = await $axios.$get(
      `https://podpri.djnd.si/api/assign-gift/${token}/`,
    );
    return {
      token,
      gifts: giftsResponse.gifts || [],
    };
  },
  data() {
    return {
      error: null,
      giftIndex: 0,
      giftUpdating: false,
      name: '',
      email: '',
      message: defaultMessage,
    };
  },
  computed: {
    gift() {
      if (this.giftIndex >= 0 && this.giftIndex < this.gifts.length) {
        return this.gifts[this.giftIndex];
      }
      return null;
    },
    canUpdateGift() {
      if (!this.name || !this.email || !this.message) {
        return false;
      }
      if (!EMAIL_REGEX.test(this.email)) {
        return false;
      }
      // mautic fails after payment if invalid email
      // TODO: fix regex instead of this tmp
      const tmp = this.email.split('@');
      if (tmp.length < 2 || !tmp[1].includes('.')) {
        return false;
      }
      return true;
    },
  },
  created() {
    if (!this.token || !this.gifts || !this.gifts.length) {
      this.$router.push(
        this.localePath({
          name: 'donate-thanks',
        }),
      );
    }
  },
  methods: {
    async updateGift() {
      try {
        this.giftUpdating = true;
        await this.$axios.$post('https://podpri.djnd.si/api/assign-gift/', {
          owner_token: this.token,
          subscriber_token: this.gift.gift_token,
          name: this.name,
          gift_email: this.email,
          message: this.message,
        });

        if (this.giftIndex < this.gifts.length - 1) {
          this.name = '';
          this.email = '';
          this.message = defaultMessage;
          this.giftIndex++;
          this.giftUpdating = false;
        } else {
          this.$router.push(
            this.localePath({
              name: 'donate-thanks',
            }),
          );
        }
      } catch (error) {
        // eslint-disable-next-line no-console
        console.error(error);
        this.error = error;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.checkout {
  .gift-content {
    max-width: 540px;
    margin: 0 auto;

    .name-label {
      font-size: 1.25rem;
      font-weight: 300;
      font-style: italic;
    }

    .message-label {
      font-weight: 300;
      font-style: italic;
    }
  }

  .confirm-button-container {
    text-align: center;
  }
}
</style>
