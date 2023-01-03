<template>
  <div class="container-fluid">
    <div class="djnd-logo">
      <a href="/">
        <img
          src="../../../static/icons/donations/2022/djdn-logo-dark-100.png"
          alt="DJND logo"
        />
      </a>
    </div>

    <div class="row">
      <img
        class="header-image"
        :src="
          require(`../../../static/icons/donations/2022/naslovi/${options[option].headerSrc}`)
        "
        :alt="options[option].title"
      />
    </div>
    <div class="row my-5">
      <div class="col-12" v-html="options[option].htmlText"></div>
    </div>
    <div class="row justify-content-center colored-section py-8">
      <div class="col-lg-10">
        <div class="row" v-if="options[option].donate.includes('dohodnina')">
          <div class="col-lg-4 pr-5">
            <h4>Nameni nam 1 % dohodnine!</h4>
            <div class="icons-p my-2 my-lg-4">
              <img
                src="../../../static/icons/donations/2022/ikone/1FA99.svg"
                alt=""
              />
              <img
                src="../../../static/icons/donations/2022/ikone/1F44F.svg"
                alt=""
              />
              <img
                src="../../../static/icons/donations/2022/ikone/1F4AB.svg"
                alt=""
              />
              <img
                src="../../../static/icons/donations/2022/ikone/1F496.svg"
                alt=""
              />
            </div>
            <h2>Tebe nič ne stane, nam pa pomeni veliko!</h2>
          </div>
          <div
            class="col-lg-8"
            v-if="!options[option].donate.includes('cnvos')"
          >
            <p class="dohodnina-instructions">
              Vpiši svoje podatke v obrazec spodaj in izberi eno od dveh
              možnosti za oddajo obrazca.
            </p>
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
                  src="../../../static/icons/donations/2022/noun-arrow.svg"
                  alt=""
                />
              </a>
            </div>
          </div>
          <div class="col-lg-8" v-if="options[option].donate.includes('cnvos')">
            <div>
              <a
                href="https://www.cnvos.si/enprocent/"
                target="_blank"
                class="btn-link"
              >
                <p>Razdeli 1 % dohodnine</p>
                <img
                  class="button-arrow"
                  src="../../../static/icons/donations/2022/noun-arrow.svg"
                  alt=""
                />
              </a>
            </div>
          </div>
        </div>
        <div v-if="options[option].donate == 'dohodnina_narocnina'" class="row">
          <div class="col-12">
            <hr />
          </div>
        </div>
        <div v-if="options[option].donate.includes('narocnina')" class="row">
          <div class="col-lg-4 pr-5">
            <h4>Doniraj nam vsak mesec!</h4>
            <div class="icons-p my-4">
              <img
                src="../../../static/icons/donations/2022/ikone/2728.svg"
                alt=""
              />
              <img
                src="../../../static/icons/donations/2022/ikone/1F381.svg"
                alt=""
              />
              <img
                src="../../../static/icons/donations/2022/ikone/1FAF6.svg"
                alt=""
              />
              <img
                src="../../../static/icons/donations/2022/ikone/1F3C6.svg"
                alt=""
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
                <donation-option
                  class="donation-option-custom"
                  :donation-preset="dp"
                  @select="selectDonationPreset(dp)"
                />
              </div>
            </div>
            <div class="row">
              <div class="col-12 d-flex justify-content-center">
                <a
                  :href="`/doniraj/novi/5?amount=${selectedDonationAmount}`"
                  target="_blank"
                  class="donate-button"
                  :class="{ disabled: !selectedDonationAmount }"
                >
                  <p>Doniraj!</p>
                  <img
                    class="button-arrow"
                    src="../../../static/icons/donations/2022/noun-arrow.svg"
                    alt=""
                  />
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import DonationDohodninaEmbed from '~/components/DonationDohodninaEmbed.vue';
import DonationOption from '~/components/DonationOption.vue';

export default {
  components: {
    DonationDohodninaEmbed,
    DonationOption,
  },
  layout: 'donate-2022',

  pageColor: 'secondary',

  nuxtI18n: {
    paths: {
      sl: '/novoletna-kampanja-2022/:option',
      en: '/new-years-campaign-2022/:option',
    },
  },

  data() {
    const option = this.$route.params.option;

    return {
      showDohodnina: false,
      donationAmount: 0,
      options: {
        'brez-denarnice': {
          title: 'Ker sem pozabil_a denarnico doma',
          htmlText:
            '<p>Brez skrbi, <a href="https://danesjenovdan.si/dejavnosti" target="_blank" class="project-link">naše delo</a> lahko podpreš tudi brez denarnice, gotovine ali kreditne kartice! Nameni nam 1 % dohodnine – gotov_a boš v 46 sekundah!</p>',
          donate: 'dohodnina',
          headerSrc: 'naslov_DENARNICA.png',
        },
        'ni-za-najemnino': {
          title: 'Ker nimam niti za najemnino',
          htmlText:
            '<p>Stanje na najemnem trgu se iz leta v leto slabša, zato poskušamo v sklopu <a href="https://najemniski-sos.si/" target="_blank" class="project-link">Najemniškega SOS</a>-a omiliti stanovanjske stiske.</p><p>Ker si z denarjem na tesnem, nas lahko podpreš z donacijo 1 % dohodnine – na tvojem bančnem računu se ne bo nič poznalo.</p>',
          donate: 'dohodnina',
          headerSrc: 'naslov_NIMAM_ZA_NAJEMNINO.png',
        },
        'ne-zaupam': {
          title: 'Ker ne zaupam spletnim plačilom',
          htmlText:
            '<p>Ni problema! Podpreš nas lahko tudi brez plačila, in sicer tako, da nam nameniš 1 % dohodnine – postopek je preprost in ne pušča možnosti, da ti denar ukrade heker!</p>',
          donate: 'dohodnina',
          headerSrc: 'naslov_NE_ZAUPAM.png',
        },
        soros: {
          title: 'Ker vas itak plačuje Soroš',
          htmlText:
            '<p>Pa ne, da spet bereš <a href="https://twito.si/" target="_blank" class="project-link">Janševe tvite</a>? Financira nas več kot 10 organizacij in veliko čudovitih posameznic_kov.</p><p>Pridruži se jim in nam pomagaj v boju za bolj solidarno družbo!</p>',
          donate: 'dohodnina_narocnina',
          headerSrc: 'naslov_SOROS.png',
        },
        'kaj-bluzite': {
          title: 'Kaj bluzite, saj sem že doniral_a',
          htmlText:
            '<p>Ups, pa res – zelo smo ti hvaležni za pomoč. Ker pa boj za solidarno družbo ni poceni, nam lahko za praznike podariš še mesečno donacijo ali pa 1% dohodnine! 😜</p>',
          donate: 'dohodnina_narocnina',
          headerSrc: 'naslov_BLUZITE.png',
        },
        'ne-znam': {
          title: 'Ker je preveč zakomplicirano',
          htmlText:
            '<p>Enkrat si že kliknil_a, samo še dvakrat, pa smo zaključili! Dlje traja, da na Netflixu izbereš, kaj boš gledal_a.</p>',
          donate: 'dohodnina_narocnina',
          headerSrc: 'naslov_ZAKOMPLICIRANO.png',
        },
        'z-desne': {
          title: 'Ker sem desničar_ka',
          htmlText:
            '<p>O, živjo, kako si pa ti pristal_a tukaj?</p><p>No, saj ni važno – dokaži, da so <a href="https://danesjenovdan.si/lestvica-transparentnosti/" target="_blank" class="project-link">transparentnost</a>, <a href="https://participativni-proracun.djnd.si/" target="_blank" class="project-link">demokratizacija</a> in <a href="https://obljubadeladolg.si/" target="_blank" class="project-link">nadzor nad oblastjo</a>, za kar se borimo na Danes je nov dan, vrednote, skupne vsem. Podpri naše delo in pomagaj pri spravi!</p>',
          donate: 'dohodnina_narocnina',
          headerSrc: 'naslov_DESNICAR.png',
        },
        davkoplacevalec: {
          title: 'Ker mi že država preveč pobere od plače',
          htmlText:
            '<p>Pazi to – 1 % tega, kar ti pobere država, lahko vzameš nazaj in podariš nam.</p><p>Tako lahko hkrati podpreš <a href="https://danesjenovdan.si/lestvica-transparentnosti/" target="_blank" class="project-link">transparentnost</a>, <a href="https://participativni-proracun.djnd.si/" target="_blank" class="project-link">demokratizacijo</a> in <a href="https://obljubadeladolg.si/" target="_blank" class="project-link">nadzor nad oblastjo</a>, pokažeš sredinca sistemu in ne izgubiš niti evra!</p>',
          donate: 'dohodnina',
          headerSrc: 'naslov_DRZAVA.png',
        },
        'kaj-pocnemo': {
          title: 'Ker sploh ne vem, kaj vi počnete',
          htmlText:
            '<p>Čeprav mogoče še nisi slišal_a za nas, pa se te naše delo skoraj zagotovo tiče. Če želiš biti tudi ti del projektov, kot so <a href="https://parlameter.si/" target="_blank" class="project-link">Parlameter</a>, <a href="https://pravna-mreza.si/" target="_blank" class="project-link">Pravna mreža</a>, <a href="https://najemniski-sos.si/" target="_blank" class="project-link">Najemniški SOS</a>, <a href="https://danesjenovdan.si/lestvica-transparentnosti/" target="_blank" class="project-link">lestvica transparentnosti občin</a>, <a href="https://kvizle.si/#/calendar" target="_blank" class="project-link">Kvizle</a>, <a href="https://danesjenovdan.si/agrument" target="_blank" class="project-link">Agrument</a> in <a href="https://volitvomat.si/" target="_blank" class="project-link">Volitvomat</a>, nam nameni 1 % dohodnine ali mesečno donacijo!</p>',
          donate: 'dohodnina_narocnina',
          headerSrc: 'naslov_KAJPOCNETE.png',
        },
        'hocem-donirati-mesecno': {
          title: 'Pa saj hočem mesečno donirati',
          htmlText:
            '<p>O, super! Zelo smo ti hvaležni, da podpiraš naše delo.</p>',
          donate: 'narocnina',
          headerSrc: 'naslov_MESECNA.png',
        },
        'hocem-donirati-dohodnino': {
          title: 'Pa saj hočem donirati 1 % dohodnine',
          htmlText:
            '<p>O, super! Zelo smo ti hvaležni, da podpiraš naše delo.</p>',
          donate: 'dohodnina',
          headerSrc: 'naslov_DOHODNINA.png',
        },
        'doniram-drugam': {
          title: 'Ker raje dam komu, ki bolj rabi',
          htmlText:
            '<p>Razumemo in podpiramo! Če pa želiš svoj 1 % dohodnine vseeno razdeliti med več organizacij in del nameniti tudi nam, lahko to narediš z le nekaj kliki, nam pa polepšaš celo leto!</p>',
          donate: 'cnvos_dohodnina',
          headerSrc: 'naslov_BOLJRABI.png',
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
      title: 'Zakaj nisi še nikoli doniral_a Danes je nov dan?',
      meta: [
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        {
          hid: 'description',
          name: 'description',
          content:
            'Deli svoj razlog, mi pa ti povemo, kako nam lahko vseeno pomagaš!',
        },
        {
          hid: 'og:title',
          property: 'og:title',
          content: 'Zakaj nisi še nikoli doniral_a Danes je nov dan?',
        },
        {
          hid: 'og:description',
          property: 'og:description',
          content:
            'Deli svoj razlog, mi pa ti povemo, kako nam lahko vseeno pomagaš!',
        },
        {
          hid: 'og:image',
          property: 'og:image',
          content: 'https://danesjenovdan.si/donatorska-2022_OG.png',
        },
        {
          hid: 'twitter:title',
          property: 'twitter:title',
          content: 'Zakaj nisi še nikoli doniral_a Danes je nov dan?',
        },
        {
          hid: 'twitter:description',
          property: 'twitter:description',
          content:
            'Deli svoj razlog, mi pa ti povemo, kako nam lahko vseeno pomagaš!',
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
    // goToCheckout(dp) {
    //   console.log(dp);
    //   // this.$router.push(
    //   //   this.localePath({ name: 'me', query: { email: this.email } }),
    //   // );
    // },
  },
};
</script>

<style lang="scss" scoped>
.djnd-logo {
  display: flex;
  justify-content: end;

  a {
    margin: 40px;
  }

  img {
    width: 90px;
  }

  @include media-breakpoint-down(sm) {
    a {
      margin: 20px;
    }
  }
}

.header-image {
  max-width: 100%;
  height: auto;

  @include media-breakpoint-down(sm) {
    min-height: 60px;
    object-fit: cover;
  }
}

.py-8 {
  padding: 100px 0;

  @include media-breakpoint-down(sm) {
    padding: 40px 0;
  }
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
    font-size: 28px;
    line-height: 32px;
    margin-bottom: 20px;
  }
}

h4 {
  color: #000000;
  font-size: 40px;
  font-weight: 700;
  line-height: 44px;

  @include media-breakpoint-down(sm) {
    font-size: 20px;
    line-height: 22px;
  }
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

  @include media-breakpoint-down(sm) {
    width: 30px;
  }
}

.colored-section {
  background-color: #fdf7f6;
}

.icons-p img {
  display: inline-block;
  width: 60px;

  @include media-breakpoint-down(sm) {
    width: 40px;
  }
}

iframe {
  border: 2px solid #df786c;
}

hr {
  border-color: #df786c;
  border-width: 2px;
  margin: 100px 0;

  @include media-breakpoint-down(sm) {
    margin: 40px 0;
  }
}

.donation-header {
  color: #333333;
  font-size: 36px;
  line-height: 40px;
  margin-bottom: 30px;

  @include media-breakpoint-down(sm) {
    font-size: 20px;
    line-height: 24px;
    margin-top: 30px;
  }
}

.dohodnina-instructions {
  font-size: 24px;
  font-weight: 200;
  line-height: 1.25;
  margin-left: 0;
  margin-right: 0;

  @include media-breakpoint-down(sm) {
    font-size: 16px;
    padding: 0;
  }
}

.btn-link {
  padding: 40px 100px 40px 20px;
  position: relative;
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
    padding: 0;
    text-align: center;
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

  @include media-breakpoint-down(sm) {
    padding: 20px 60px 20px 20px;

    p {
      font-size: 20px;
      line-height: 24px;
      text-align: left;
    }
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

  &.disabled {
    pointer-events: none;
    cursor: default;
    opacity: 0.5;
  }

  @include media-breakpoint-down(sm) {
    width: 100%;

    p {
      font-size: 20px;
      line-height: 24px;
    }
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

      @include media-breakpoint-down(sm) {
        align-items: start;
      }

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
