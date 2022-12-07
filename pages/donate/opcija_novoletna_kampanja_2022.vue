<template>
  <div class="container-fluid">
    <div class="djnd-logo">
      <img src="../../static/icons/donations/2022/djdn-logo-dark-100.png" />
    </div>
    <div class="row">
      <img
        class="img-fluid header-image"
        :src="
          require(`../../static/icons/donations/2022/naslovi/${options[option].headerSrc}`)
        "
      />
    </div>
    <div class="row my-5">
      <div class="col-12" v-html="options[option].htmlText"></div>
    </div>
    <div class="row justify-content-center colored-section py-8">
      <div class="col-lg-10">
        <div class="row">
          <div class="col-lg-4">
            <h4>Nameni nam 1 % dohodnine!</h4>
            <div class="icons-p my-4">
              <img
                class=""
                src="../../static/icons/donations/2022/ikone/1FA99.svg"
              />
              <img
                class=""
                src="../../static/icons/donations/2022/ikone/1F44F.svg"
              />
              <img
                class=""
                src="../../static/icons/donations/2022/ikone/1F4AB.svg"
              />
              <img
                class=""
                src="../../static/icons/donations/2022/ikone/1F496.svg"
              />
            </div>
            <h2>Tebe nič ne stane, nam pa pomeni veliko!</h2>
          </div>
          <div class="col-lg-8">
            <donation-dohodnina-embed />
            <div class="my-4">
              <a
                href="https://edavki.durs.si/EdavkiPortal/OpenPortal/CommonPages/Opdynp/PageD.aspx?category=namenitev_dela_dohodnine_fo"
                target="_blank"
                class="btn-link"
              >
                <p>Vlogo lahko oddaš tudi s certifikatom na eDavkih!</p>
                <img
                  class="button-arrow"
                  src="../../static/icons/donations/2022/noun-arrow.svg"
                />
              </a>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-12">
            <hr />
          </div>
        </div>
        <div class="row">
          <div class="col-lg-4">
            <h4>Doniraj nam vsak mesec!</h4>
            <div class="icons-p my-4">
              <img
                class=""
                src="../../static/icons/donations/2022/ikone/2728.svg"
              />
              <img
                class=""
                src="../../static/icons/donations/2022/ikone/1F381.svg"
              />
              <img
                class=""
                src="../../static/icons/donations/2022/ikone/1FAF6.svg"
              />
              <img
                class=""
                src="../../static/icons/donations/2022/ikone/1F3C6.svg"
              />
            </div>
            <h2>Ker nas želiš redno podpirati!</h2>
          </div>
          <div class="col-lg-8">
            <h4 class="donation-header">Izberi višino mesečne donacije!</h4>
            <div class="row">
              <div
                class="col-lg-3"
                v-for="(dp, i) in donationPresets"
                :key="`presets-${i}`"
              >
                <!-- <div class="donation-button">5 EUR</div> -->
                <donation-option
                  :donation-preset="dp"
                  @select="selectDonationPreset(dp)"
                />
              </div>
            </div>
            <nuxt-link
              :to="{
                path: '/doniraj/novi/5',
                query: { amount: selectedDonationAmount },
              }"
              class="btn-link"
            >
              <p>Doniraj!</p>
              <img
                class="button-arrow"
                src="../../static/icons/donations/2022/noun-arrow.svg"
              />
            </nuxt-link>
          </div>

          <!-- preusmeri na http://localhost:3001/doniraj-djnd/5?amount=? -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import DonationLogo from '~/components/DonationLogo.vue';
// import DonationChoiceButtonWide from '~/components/DonationChoiceButtonWide.vue';
import DonationDohodninaEmbed from '~/components/DonationDohodninaEmbed.vue';
import DonationOption from '~/components/DonationOption.vue';

export default {
  components: {
    // DonationLogo,
    // DonationChoiceButtonWide,
    DonationDohodninaEmbed,
    DonationOption,
  },
  layout: 'donate-2022',

  pageColor: 'secondary',

  nuxtI18n: {
    paths: {
      // sl: '/doniraj-novoletna-kampanja-2022',
      // en: '/donate-new-year-campaign-2022',
      sl: '/doniraj/:option',
      en: '/donate/:option',
    },
  },

  data() {
    const option = this.$route.params.option;

    return {
      showDohodnina: false,
      donationAmount: 0,
      options: {
        'brez-denarnice': {
          htmlText:
            '<p>Brez skrbi, podpreš nas lahko brez denarnice, gotovine ali kreditne kartice! Nameni nam 1 % dohodnine – gotov_a boš v 46 sekundah!</p>',
          donate: 'dohodnina',
          headerSrc: 'naslov_DENARNICA.png',
        },
        najemnina: {
          htmlText:
            '<p class="paragraph">Stanje na najemnem trgu se iz leta v leto slabša, zato poskušamo v sklopu <a href="">Najemniškega SOS</a>-a omiliti stanovanjske stiske.</p><p>Ker si z denarjem na tesnem, nas lahko podpreš z donacijo 1 % dohodnine – na tvojem bančnem računu se ne bo nič poznalo.</p>',
          donate: 'dohodnina',
          headerSrc: 'naslov_NIMAM_ZA_NAJEMNINO.png',
        },
        'ne-zaupam': {
          htmlText:
            '<p>Ni problema, podpreš nas lahko tudi brez plačila, in sicer tako, da nam nameniš 1 % dohodnine – postopek je preprost in ne pušča možnosti, da ti denar ukrade heker!</p>',
          donate: 'dohodnina',
          headerSrc: 'naslov_NE_ZAUPAM.png',
        },
        soros: {
          htmlText:
            '<p>Pa ne, da spet bereš Janševe tvite? Žal nas Soroš (še) ne plačuje, financira pa nas več kot 10 organizacij in veliko čudovitih posameznic_kov.</p><p>Pridruži se jim in nam pomagaj v boju za bolj solidarno družbo!</p>',
          donate: 'dohodnina_narocnina',
          headerSrc: 'naslov_NIMAM_ZA_NAJEMNINO.png',
        },
        'kaj-bluzite': {
          htmlText:
            '<p>Ups, pa res – zelo smo ti hvaležni za pomoč. Ker pa boj za solidarno družbo ni poceni, nam lahko za praznike podariš še mesečno donacijo ali pa 1% dohodnine! 😜</p>',
          donate: 'dohodnina_narocnina',
          headerSrc: 'naslov_BLUZITE.png',
        },
        'ne-znam': {
          htmlText:
            '<p>Enkrat si že kliknil_a, še dvakrat, pa smo zaključili! Dlje traja, da na Netflixu izbereš, kaj boš gledal_a.</p>',
          donate: 'dohodnina_narocnina',
          headerSrc: 'naslov_ZAKOMPLICIRANO.png',
        },
        'iz-desne': {
          htmlText:
            '<p>O, živjo, kako si pa ti pristal_a tukaj?</p><p>No, saj ni važno – dokaži, da so transparentnost, demokratizacija in nadzor nad oblastjo, za kar se borimo na Danes je nov dan, vrednote, skupne vsem, in podpri naše delo!</p>',
          donate: 'dohodnina_narocnina',
          headerSrc: 'naslov_NIMAM_ZA_NAJEMNINO.png',
        },
        davkoplacevalec: {
          htmlText:
            '<p>Pazi to – 1 % tega, kar ti pobere država, lahko vzameš nazaj in podariš nam.</p><p>Tako podpreš transparentnost, demokratizacijo ter nadzor nad oblastjo, pokažeš sredinca sistemu in ne izgubiš niti evra!</p>',
          donate: 'dohodnina',
          headerSrc: 'naslov_NIMAM_ZA_NAJEMNINO.png',
        },
        cringe: {
          htmlText: '<p>Ampak smo svobodni – pridruži se nam!</p>',
          donate: 'dohodnina_narocnina',
          headerSrc: 'naslov_NIMAM_ZA_NAJEMNINO.png',
        },
      },
      donationPresets: [
        {
          amount: 5,
          description: '',
          selected: false,
          eventName: 'five',
          monthly: true,
          oneTime: false,
        },
        {
          amount: 11,
          description: '',
          selected: false,
          eventName: 'eleven',
          monthly: true,
          oneTime: true,
        },
        {
          amount: 24,
          description: '',
          selected: false,
          eventName: 'twentyfour',
          monthly: true,
          oneTime: true,
        },
        {
          custom: true,
          amount: null,
          description: 'Vnesi poljuben znesek!',
          selected: false,
          eventName: 'aeleven',
          monthly: true,
          oneTime: true,
        },
      ],
      option,
    };
  },

  head() {
    return {
      title: 'Poženi nov dan!',
      meta: [
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        {
          hid: 'description',
          name: 'description',
          content:
            'Leto sklepamo z zbiranjem donacij za neodvisno delovanje. Podpri Danes je nov dan in poskrbi, da bomo v 2022 delovali tudi na tvoj pogon.',
        },
        {
          hid: 'og:title',
          property: 'og:title',
          content: 'Poženi nov dan!',
        },
        {
          hid: 'og:description',
          property: 'og:description',
          content:
            'Leto sklepamo z zbiranjem donacij za neodvisno delovanje. Podpri Danes je nov dan in poskrbi, da bomo v 2022 delovali tudi na tvoj pogon.',
        },
        {
          hid: 'og:image',
          property: 'og:image',
          content: 'https://danesjenovdan.si/donatorska-2021-OG.png',
        },
        {
          hid: 'twitter:title',
          property: 'twitter:title',
          content: 'Poženi nov dan!',
        },
        {
          hid: 'twitter:description',
          property: 'twitter:description',
          content:
            'Leto sklepamo z zbiranjem donacij za neodvisno delovanje. Podpri Danes je nov dan in poskrbi, da bomo v 2022 delovali tudi na tvoj pogon.',
        },
        {
          hid: 'twitter:image',
          property: 'twitter:image',
          content: 'https://danesjenovdan.si/donatorska-2021-OG.png',
        },
      ],
    };
  },

  computed: {
    selectedDonationAmount() {
      const selected = this.donationPresets.find((dp) => dp.selected);
      return selected ? Number(selected.amount) : 0;
    },
    // donationAmountPercentage() {
    //   return Math.round((this.donationAmount / 15000) * 100);
    // },
    // daysLeft() {
    //   const today = new Date();
    //   const deadline = new Date(2022, 0, 3);
    //   const oneDay = 1000 * 60 * 60 * 24;
    //   return Math.ceil((deadline.getTime() - today.getTime()) / oneDay);
    // },
  },

  methods: {
    selectDonationPreset(sdp) {
      this.donationPresets.forEach((dp) => {
        dp.selected = dp === sdp;
      });
    },
    goToCheckout(dp) {
      console.log(dp);
      // this.$router.push(
      //   this.localePath({ name: 'me', query: { email: this.email } }),
      // );
    },
  },

  async mounted() {
    // const donationStatistics = await this.$axios.$get(
    //   'https://podpri.djnd.si/api/donation-statistics/10/',
    // );
    // this.donationAmount = donationStatistics['donation-amount'];
  },
};
</script>

<style lang="scss" scoped>
/deep/ .logo {
  width: 230px;

  @include media-breakpoint-up(sm) {
    width: 300px;
  }
}

.djnd-logo {
  display: flex;
  justify-content: end;

  img {
    width: 90px;
    margin: 40px;
  }
}

.py-8 {
  padding: 100px 0;
}

h1 {
  font-size: 65px;
  font-weight: 600;
  // line-height: 100px;
  font-style: italic;
  letter-spacing: -1px;
  text-align: left;
  width: 100%;

  @include media-breakpoint-down(sm) {
    font-size: 50px;
    line-height: 60px;
    margin-bottom: 0;
    padding-left: 30px;
    padding-right: 30px;
  }
}

h2 {
  font-size: 60px;
  font-style: italic;
  font-weight: 700;
  margin-bottom: 3rem;
  color: #000000;
  line-height: 60px;

  @include media-breakpoint-down(sm) {
    font-size: 32px;
    line-height: 40px;
    margin-bottom: 0;
    padding-left: 30px;
    padding-right: 30px;
  }
}

h4 {
  color: #000000;
  font-size: 40px;
  font-weight: 700;
  line-height: 44px;
}

/deep/ p {
  font-size: 20px;
  color: #333333;
  font-weight: 200;
  width: 100%;
  max-width: 872px;
  padding-left: 30px;
  padding-right: 30px;
  margin-left: auto;
  margin-right: auto;

  @include media-breakpoint-up(md) {
    font-size: 30px;
    padding: 0;
  }
}

.button-arrow {
  width: 50px;
}

.colored-section {
  background-color: #fdf7f6;
}

.icons-p img {
  display: inline-block;
  width: 60px;
}

iframe {
  border: 2px solid #df786c;
}

.btn-link {
  padding: 40px 100px 40px 0;
  position: relative;
  text-align: center;
  display: flex;
  align-items: center;
  border: 2px solid #df786c;
  width: 100%;

  p {
    margin: 0;
    flex: 1;
    font-size: 30px;
    color: #333333;
    font-weight: 700;
    line-height: 32px;
  }

  span {
    position: absolute;
    right: 20px;
  }

  &:hover {
    text-decoration: none;
  }
}

.colored-text {
  color: #dc776b;
  font-weight: 900;
}

.limit-like-p {
  width: 100%;
  max-width: 872px;
}
.pad-like-p {
  padding-left: 30px;
  padding-right: 30px;
}
</style>
