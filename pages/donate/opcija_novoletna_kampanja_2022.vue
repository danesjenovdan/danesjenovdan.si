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
          <div class="col-lg-4 pr-5">
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
            <div class="mt-4">
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
          <div class="col-lg-4 pr-5">
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
                v-for="(dp, i) in donationPresets"
                :key="`presets-${i}`"
                class="col-lg-3 monthly-donation"
              >
                <!-- <div class="donation-button">5 EUR</div> -->
                <donation-option
                  class="donation-option-custom"
                  :donation-preset="dp"
                  @select="selectDonationPreset(dp)"
                />
              </div>
            </div>
            <div class="row">
              <div class="col-12 d-flex justify-content-center">
                <nuxt-link
                  :to="{
                    path: '/doniraj/novi/5',
                    query: { amount: selectedDonationAmount },
                  }"
                  class="donate-button"
                >
                  <p>Doniraj!</p>
                  <img
                    class="button-arrow"
                    src="../../static/icons/donations/2022/noun-arrow.svg"
                  />
                </nuxt-link>
              </div>
            </div>
          </div>
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
            '<p>Stanje na najemnem trgu se iz leta v leto slabša, zato poskušamo v sklopu <a href="https://najemniski-sos.si/" target="_blank" class="project-link">Najemniškega SOS</a>-a omiliti stanovanjske stiske.</p><p>Ker si z denarjem na tesnem, nas lahko podpreš z donacijo 1 % dohodnine – na tvojem bančnem računu se ne bo nič poznalo.</p>',
          donate: 'dohodnina',
          headerSrc: 'naslov_NIMAM_ZA_NAJEMNINO.png',
        },
        'ne-zaupam': {
          htmlText:
            '<p>Ni problema! Podpreš nas lahko tudi brez plačila, in sicer tako, da nam nameniš 1 % dohodnine – postopek je preprost in ne pušča možnosti, da ti denar ukrade heker!</p>',
          donate: 'dohodnina',
          headerSrc: 'naslov_NE_ZAUPAM.png',
        },
        soros: {
          htmlText:
            '<p>Pa ne, da spet bereš <a href="https://twito.si/" target="_blank" class="project-link">Janševe tvite</a>? Žal nas Soroš (še) ne plačuje, financira pa nas več kot 10 organizacij in veliko čudovitih posameznic_kov.</p><p>Pridruži se jim in nam pomagaj v boju za bolj solidarno družbo!</p>',
          donate: 'dohodnina_narocnina',
          headerSrc: 'naslov_SOROS.png',
        },
        'kaj-bluzite': {
          htmlText:
            '<p>Ups, pa res – zelo smo ti hvaležni za pomoč. Ker pa boj za solidarno družbo ni poceni, nam lahko za praznike podariš še mesečno donacijo ali pa 1% dohodnine! 😜</p>',
          donate: 'dohodnina_narocnina',
          headerSrc: 'naslov_BLUZITE.png',
        },
        'ne-znam': {
          htmlText:
            '<p>Enkrat si že kliknil_a, samo še dvakrat, pa smo zaključili! Dlje traja, da na Netflixu izbereš, kaj boš gledal_a.</p>',
          donate: 'dohodnina_narocnina',
          headerSrc: 'naslov_ZAKOMPLICIRANO.png',
        },
        'z-desne': {
          htmlText:
            '<p>O, živjo, kako si pa ti pristal_a tukaj?</p><p>No, saj ni važno – dokaži, da so <a href="https://danesjenovdan.si/lestvica-transparentnosti/" target="_blank" class="project-link">transparentnost</a>, <a href="https://participativni-proracun.djnd.si/" target="_blank" class="project-link">demokratizacija</a> in <a href="https://obljubadeladolg.si/" target="_blank" class="project-link">nadzor nad oblastjo</a>, za kar se borimo na Danes je nov dan, vrednote, skupne vsem, in podpri naše delo!</p>',
          donate: 'dohodnina_narocnina',
          headerSrc: 'naslov_DESNICAR.png',
        },
        davkoplacevalec: {
          htmlText:
            '<p>Pazi to – 1 % tega, kar ti pobere država, lahko vzameš nazaj in podariš nam.</p><p>Tako lahko hkrati podpreš <a href="https://danesjenovdan.si/lestvica-transparentnosti/" target="_blank" class="project-link">transparentnost</a>, <a href="https://participativni-proracun.djnd.si/" target="_blank" class="project-link">demokratizacijo</a> in <a href="https://obljubadeladolg.si/" target="_blank" class="project-link">nadzor nad oblastjo</a>, pokažeš sredinca sistemu in ne izgubiš niti evra!</p>',
          donate: 'dohodnina',
          headerSrc: 'naslov_DRZAVA.png',
        },
        cringe: {
          htmlText: '<p>Ampak smo svobodni – pridruži se nam!</p>',
          donate: 'dohodnina_narocnina',
          headerSrc: 'naslov_CRINGE.png',
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
            'Leto sklepamo z zbiranjem donacij za neodvisno delovanje. Podpri Danes je nov dan in poskrbi, da bomo v 2023 delovali tudi na tvoj pogon.',
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
            'Leto sklepamo z zbiranjem donacij za neodvisno delovanje. Podpri Danes je nov dan in poskrbi, da bomo v 2023 delovali tudi na tvoj pogon.',
        },
        {
          hid: 'og:image',
          property: 'og:image',
          content: 'https://danesjenovdan.si/donatorska-2022_OG.png',
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
            'Leto sklepamo z zbiranjem donacij za neodvisno delovanje. Podpri Danes je nov dan in poskrbi, da bomo v 2023 delovali tudi na tvoj pogon.',
        },
        {
          hid: 'twitter:image',
          property: 'twitter:image',
          content: 'https://danesjenovdan.si/donatorska-2022_OG.png',
        },
      ],
    };
  },

  computed: {
    selectedDonationAmount() {
      const selected = this.donationPresets.find((dp) => dp.selected);
      return selected ? Number(selected.amount) : 0;
    },
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

/deep/ .project-link {
  color: #333333;
  text-decoration: underline;
  font-weight: 400;
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

hr {
  border-color: #df786c;
  border-width: 2px;
  margin: 100px 0;
}

.donation-header {
  color: #333333;
  font-size: 36px;
  line-height: 40px;
  margin-bottom: 30px;
}

.btn-link {
  padding: 40px 100px 40px 0;
  position: relative;
  text-align: center;
  display: flex;
  align-items: center;
  border: 2px solid #df786c;
  max-width: 800px;

  p {
    margin: 0;
    flex: 1;
    font-size: 30px;
    color: #333333;
    font-weight: 700;
    line-height: 32px;
  }

  .button-arrow {
    position: absolute;
    right: 20px;
  }

  &:hover {
    text-decoration: none;
    background-image: none;
    background-color: #f5d6d3;
  }
}

.donate-button {
  border: 2px solid #df786c;
  display: flex;
  align-items: center;
  padding: 25px 120px 25px 35px;
  background-image: linear-gradient(to right, #f5d6d3 0%, #fdf7f6 100%);
  position: relative;

  p {
    font-size: 36px;
    font-weight: 700;
    line-height: 40px;
    color: #333333;
    margin-bottom: 0;
  }

  .button-arrow {
    position: absolute;
    right: 20px;
  }

  &:hover {
    text-decoration: none;
    background-image: none;
    background-color: #f5d6d3;
  }
}

/deep/ .donation-option-custom.donation-option {
  // height: 200px;
  height: 160px;
  .donation-option__content-wrapper {
    background-image: none;
    border: 2px solid #df786c;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;

    .donation-option__content {
      display: flex;
      align-items: center;
      .donation-option__amount {
        margin-bottom: 0.5rem;
        color: #333333;
        font-size: 30px;
        line-height: 32px;
      }
    }

    .donation-option__icon {
      .icon {
        position: absolute;
        width: 2rem;
        right: 10px;
        bottom: 10px;
      }
    }
  }

  &.donation-option--selected {
    .donation-option__content-wrapper {
      background-image: none;
      background-color: #f5d6d3;
    }
  }
}

.monthly-donation:last-child {
  /deep/ .donation-option-custom.donation-option {
    .donation-option__content {
      flex-direction: column-reverse;

      .donation-option__amount input {
        background-color: #ffffff;
      }

      .donation-option__description {
        font-size: 20px;
        font-weight: 400;
        font-style: normal;
        color: #000000;
        line-height: 20px;
      }
    }
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
