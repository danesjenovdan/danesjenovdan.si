<template>
  <div class="donation-landing-container">
    <donation-logo />
    <div class="row justify-content-center">
      <div class="limit-like-p">
        <h1 class="mega-header">
          Dragi <span class="strikethrough">Dedek Mraz</span><br />dobri človek!
        </h1>
      </div>
    </div>
    <div class="row justify-content-center">
      <p>
        Danesjenovdanovci radi sprejemamo izzive. V letu 2021 smo jih premagali
        kar nekaj. A izzivi s sabo prinašajo tudi izpostavljenost. Mi se
        izpostavljamo, da imate vi lahko mir. Obljubimo, da bomo to delali tudi
        v letu 2022!
      </p>
    </div>
    <div class="row justify-content-center">
      <div class="limit-like-p">
        <h2>
          Letošnji december zbiramo sredstva za neodvisno delovanje in
          potrebujemo tudi tvojo pomoč.
        </h2>
      </div>
    </div>
    <div class="row support-section position-relative py-5 my-5">
      <div class="gradient-section"></div>
      <div class="col-md pr-md-5">
        <div class="row">
          <div class="col">
            <h2 class="mb-4">
              V naslednjem letu <span class="colored-text">41 %</span><br />
              delujemo na vaš pogon!
            </h2>
          </div>
        </div>
        <div class="row">
          <div class="col">
            <div class="progress">
              <span class="progress-bar"></span>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col">
            <p class="progress-bar-subtitle-left">
              <span>Zbrali smo že</span><br />
              <span>2345 €</span><br />
              od <span>15 000 €</span><br />
            </p>
          </div>
          <div class="col">
            <p class="progress-bar-subtitle-right">
              <span>7</span> dni do<br />
              konca kampanje
            </p>
          </div>
        </div>
        <hr />
        <div class="row">
          <div class="col">
            <p>
              Ful imamo stroškov za delovanje. To so stroški za serverje,
              domene, programje in licence. Brez njih smo bosi.
            </p>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
              enim enim ad minim veniam, quis nostrud exercitation ullamco
              laboris aliquip ex ea commodo consequat.
            </p>
          </div>
        </div>
      </div>
      <div class="col-md pl-md-5">
        <h3>Prispevaj tudi ti!</h3>
        <donation-choice-button-wide
          donation-type="tax-return"
          :href="
            $i18n.locale === 'sl'
              ? '/doniraj/placaj/enprocent'
              : '/en/donate/checkout/one-percent'
          "
        />
        <donation-choice-button-wide
          donation-type="monthly"
          :href="
            $i18n.locale === 'sl'
              ? '/doniraj/placaj/mesecno'
              : '/en/donate/checkout/monthly'
          "
        />
        <donation-choice-button-wide
          donation-type="once"
          :href="
            $i18n.locale === 'sl'
              ? '/doniraj/placaj/enkrat'
              : '/en/donate/checkout/once'
          "
        />
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="limit-like-p">
        <h1 class="mt-5">Kaj smo naredili v 2021?</h1>
        <p>
          V 2021 smo nadzirali lokalno politiko, spremljali vladne obljube,
          razkrivali Twitter omrežja, skrbeli za varstvo demokracije in
          skupnost.
        </p>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <div class="row my-4">
          <div
            v-for="project in projects"
            :key="project.title"
            class="col-lg-4 col-md-6 my-3"
          >
            <project-tile-small
              :image="
                require(`../../static/img/donation-campaign-2021/projects/${project.imageSrc}`)
              "
              :alt="project.title"
              :text="project.description"
              :url="project.url"
            />
          </div>
        </div>
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="limit-like-p">
        <h1 class="mt-5">Kaj si želimo za 2022</h1>
        <p>
          Na inštitutu si želimo, da bi bili v 2022 manj odvisni od projektnih
          prijav, ki nam jemljejo čas in odvračajo fokus od lokalnega aktivizma.
          Svoja znanja in veščine bi radi porabili za krepitev raznolikih bojev,
          kultiviranje javnega, zlasti digitalnega prostora, spodbujanje
          vključujoče politične participacije in krepitev marginaliziranih
          glasov.
        </p>
      </div>
    </div>
    <div class="row my-5 pt-5">
      <div class="col-md problem-col">
        <p>
          S tvojo podporo bomo nadaljevali z delom, ki smo ga začeli v letošnjem
          letu. Želimo si biti ažurni in se odzivati na konkretne probleme v
          družbi.
        </p>
        <problem-tile
          title="Sovražne vsebine"
          description="V letu 2021 bo naš fokus v zvezi s sovražnimi bo predvsem na Twitterju. Že letos smo začeli s projektom Maršal Twito – Sledilnik, ki beleži in analizira Twitter aktivnost Janeza Janše, kmalu bomo objavili raziskavo Twitter brigade, ki razkriva sume o delovanju koordinirane propagandistične mreže Twitter profilov, pozorni pa bomo tudi na aktualne pojavnosti sovražnosti v medijih in na spletu."
        />
        <problem-tile
          title="Odprti podatki"
          description="V letu 2021 se bomo v okviru tega področja v veliki meri fokusirali na vprašanje odprtosti lokalnih podatkov. Naš cilj je, da občinsko različico Parlametra spravimo v vsaj 4 občine ter da izdelamo lestvico transparentnosti slovenskih občin. Poleg tega bomo opravili regionalno analizo odprtosti parlamentarnih podatkov ter izpostavili pomembnost odprtih podatkov tudi v kontekstu slovenskega predsedovanja EU."
        />
      </div>
      <div class="col-md">
        <problem-tile
          title="Narava"
          description="Pravice narave in pravice do narave so že od začetka delovanja Danes je nov dan med našimi ključnimi prioritetami in nič drugače ne bo v letu 2021. Še naprej bomo sodelovali z nevladnimi in civilnodružbenimi organizacijami s tega področja ter z njihovo pomočjo dihali za ovratnik oblasti, ki na okolje rada pozabi oz. se v zvezi z okoljskimi vprašanji pogosto spreneveda."
        />
        <problem-tile
          title="Stanovanjska kriza"
          description="Tudi v prihodnjem letu bo eden od naših temeljnih fokusov vprašanje pomanjkanja dostopnih stanovanj oz. manko ustrezne stanovanjske politike. Ukvarjali se bomo s problemi pomanjkljive ter neustrezne zakonodaje, posebej natančno pa se bomo osredotočili na pravice najemojemalcev. Poskušali bomo torej opolnomočiti veliko, a eno najbolj ranljivih skupin prebivalstva."
        />
        <problem-tile
          title="Enakost spolov"
          description="Ena ključnih ugotovitev raziskave, v kateri smo analizirali Odmeve, je, da so ženske kot gostje izrazito podreprezentirane v medijih. Za leto 2021 pripravljamo feministični podkast; serijo pogovorov z ženskami, ki delujejo kot angažirane znanstvenice, aktivistke, premišljevalke ter strokovnjakinje. Poleg tega bo naš naslednji, že 4. po vrsti, tematski agrument 25 sobot zapovrstjo slovaril feministično terminologijo, pripravili in objavili pa bomo tudi feministični bralni seznam."
        />
      </div>
    </div>
    <div class="row support-section position-relative py-5 my-5">
      <div class="gradient-section"></div>
      <div class="col-md pr-md-5 d-flex align-items-center">
        <h1>Z donacijo lahko priliješ goriva za naš pogon!</h1>
      </div>
      <div class="col-md pl-md-5">
        <h3>Prispevaj tudi ti!</h3>
        <donation-choice-button-wide
          donation-type="tax-return"
          :href="
            $i18n.locale === 'sl'
              ? '/doniraj/placaj/dohodnina'
              : '/en/donate/checkout/tax-return'
          "
        />
        <donation-choice-button-wide
          donation-type="monthly"
          :href="
            $i18n.locale === 'sl'
              ? '/doniraj/placaj/mesecno'
              : '/en/donate/checkout/monthly'
          "
        />
        <donation-choice-button-wide
          donation-type="once"
          :href="
            $i18n.locale === 'sl'
              ? '/doniraj/placaj/enkrat'
              : '/en/donate/checkout/once'
          "
        />
      </div>
    </div>
    <div class="row row-social">
      <div class="col">
        <h1>Več nas bo, prej bomo na cilju!<br />POVEJ NAPREJ!</h1>
      </div>
    </div>
    <div class="row justify-content-center donation-social">
      <div class="col-xs-auto">
        <square-icon-button
          :color="'#228794'"
          icon="facebook"
          href="#"
          @click.native.prevent="onShareClick($event, 'fb')"
        />
      </div>
      <div class="col-xs-auto">
        <square-icon-button
          :color="'#228794'"
          icon="twitter"
          href="#"
          @click.native.prevent="onShareClick($event, 'tw')"
        />
      </div>
      <div class="col-xs-auto">
        <square-icon-button
          :color="'#df786c'"
          icon="email"
          href="#"
          @click.native.prevent="onShareClick($event, 'mail')"
        />
      </div>
    </div>
  </div>
</template>

<script>
import DonationLogo from '~/components/DonationLogo.vue';
// import ConfirmButton from '~/components/ConfirmButton.vue';
// import DonationImages from '~/components/DonationImages.vue';
// import DonationMilestones from '~/components/DonationMilestones.vue';
// import DonationSummary from '~/components/DonationSummary.vue';
// import DonationCampaignProgress from '~/components/DonationCampaignProgress.vue';
import SquareIconButton from '~/components/SquareIconButton.vue';
import DonationChoiceButtonWide from '~/components/DonationChoiceButtonWide.vue';
import ProjectTileSmall from '~/components/ProjectTileSmall.vue';

// import AchievementTile from '~/components/AchievementTile.vue';
import ProblemTile from '~/components/ProblemTile.vue';

export default {
  components: {
    DonationLogo,
    // ConfirmButton,
    // DonationImages,
    // DonationMilestones,
    // DonationSummary,
    // DonationCampaignProgress,
    SquareIconButton,
    // AchievementTile,
    ProblemTile,
    DonationChoiceButtonWide,
    ProjectTileSmall,
  },
  layout: 'donate',

  pageColor: 'secondary',

  nuxtI18n: {
    paths: {
      sl: '/donatorska-kampanja',
      en: '/donatorska-kampanja',
    },
  },

  data() {
    return {
      images: [],
      projects: [
        {
          imageSrc: 'ODD.png',
          title: 'Obljuba dela dolg',
          description:
            'Spremljamo in analiziramo izpolnjevanje 51 obljub iz koalicijske pogodbe trenutne vlade in skrbimo za dvig politične odgovornosti.',
          url: 'https://obljubadeladolg.si/',
        },
        {
          imageSrc: 'glas-ljudstva.png',
          title: 'Glas ljudstva',
          description:
            'Z več kot 100 nevladnimi in civilnodružbenimi organizacijami pripravljamo 100 zahtev za politične stranke, s katerimi jih bomo pozvali k odgovornejšemu ravnanju.',
          url: 'https://glas-ljudstva.si/',
        },
        {
          imageSrc: 'vizjak.png',
          title: 'Brez greha',
          description:
            'Z več kot 43 000 virtualnimi meti smo ustregli prošnji ministra Vizjaka, naj vanj prvi vrže kamen tisti, ki je brez greha, in opozorili na absurdnost njegove obrambe proti očitkom koruptivnosti.',
          url: 'https://brezgreha.si/',
        },
        {
          imageSrc: 'lestvica-transparentnosti.png',
          title: 'Lestvica transparentnosti slovenskih občin',
          description:
            'Analizirali smo odprtost in transparentnost vseh 212 slovenskih občin in prav vsaki priporočili pet ukrepov, s pomočjo katerih bo lahko na tem področju še izboljšala svoje delovanje.',
          url: 'https://danesjenovdan.si/lestvica-transparentnosti/',
        },
        {
          imageSrc: 'najemniski-sos.png',
          title: 'Najemniški SOS',
          description:
            'Gradimo najemniško skupnost ter najemnike in najemnice izobražujemo o njihovih pravicah, jim odgovarjamo na pogosta vprašanja in jim omogočamo, da delijo svoje zgodbe.',
          url: 'https://najemniski-sos.si/',
        },
        {
          imageSrc: 'odmevi.png',
          title: 'Odmevi prve epidemije',
          description:
            'Z vidika spola smo analizirali oddaje Odmevi in pokazali na prisotnost seksizma, ki se je kazal zlasti pri številu vabljenih gostov in gostij ter izpostavljenih osebah v napovednikih.',
          url: 'https://danesjenovdan.si/odmevi',
        },
        // {
        //   imageSrc: '',
        //   title: 'Referendum za pitno vodo',
        //   description:
        //     'S številnimi aktivnostmi smo na referendumu pomagali zavrniti škodljive zakonodajne spremembe na področju zaščite voda.',
        //   url: '',
        // },
        // {
        //   imageSrc: '',
        //   title: 'Maršal Twito',
        //   description:
        //     'S sledilnikom aktivnosti Janeza Janše na družbenem omrežju Twitter smo ugotovili, da je premier v letu 2021 tvitanju posvetil X časa',
        //   url: '',
        // },
        // {
        //   imageSrc: '',
        //   title: 'Pravna mreža za varstvo demokracije',
        //   description: '',
        //   url: '',
        // },
        // {
        //   imageSrc: '',
        //   title: 'Twitter brigade',
        //   description:
        //     'Analizirali smo slovensko Twitter sfero in v javni diskurz ponesli pojem astroturfing kot orodje ustvarjanja lažne javnosti. Razkrili smo, kako delujejo lažni profili in poskrbeli, da je bil del omrežja suspendiran.',
        //   url: '',
        // },
        // {
        //   imageSrc: '',
        //   title: 'Huda pobuda',
        //   description:
        //     'Na platformi za množično financiranje nevladnih organizacij Huda pobuda smo v prvem pozivu zbrali 4805 evrov in pomagali uresničiti tri projekte.',
        //   url: '',
        // },
        // {
        //   imageSrc: '',
        //   title: 'Analiza transparentnosti Državnega zbora RS',
        //   description:
        //     'Analizirali smo odprtost in transparentnost Državnega zbora Republike Slovenije, priporočila za izboljšave pa smo delili z javnostjo in zaposlenimi v parlamentu.',
        //   url: '',
        // },
        // {
        //   imageSrc: '',
        //   title: 'Mednarodna sramota',
        //   description:
        //     'S petmesečnim pregledom tujih medijskih objav o politični situaciji v Sloveniji smo razkrili slabo podobo naše države, ki jo v svetu riše trenutna oblast.',
        //   url: '',
        // },
        // {
        //   imageSrc: '',
        //   title: 'Feministični agrument',
        //   description:
        //     'Z novo izdajo v zbirki Agrument smo osvetlili 25 konceptov feminizma, ki segajo onkraj binarnih identitetnih, spolnih in seksualnih zamejitev ali izbir.',
        //   url: '',
        // },
        // {
        //   imageSrc: '',
        //   title: '',
        //   description: '',
        //   url: '',
        // },
        // {
        //   imageSrc: '',
        //   title: '',
        //   description: '',
        //   url: '',
        // },
        // {
        //   imageSrc: '',
        //   title: '',
        //   description: '',
        //   url: '',
        // },
        // {
        //   imageSrc: '',
        //   title: '',
        //   description: '',
        //   url: '',
        // },
      ],
    };
  },

  head() {
    return {
      title: 'Doniraj za nov dan!',
      meta: [
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        {
          hid: 'description',
          name: 'description',
          content:
            'Tudi letošnje leto sklepamo z zbiranjem donacij za nadaljnje delovanje. Pridruži se boju za bolj vključujoč jutri in podpri Danes je nov dan!',
        },
        {
          hid: 'og:title',
          property: 'og:title',
          content: 'Doniraj za nov dan!',
        },
        {
          hid: 'og:description',
          property: 'og:description',
          content:
            'Tudi letošnje leto sklepamo z zbiranjem donacij za nadaljnje delovanje. Pridruži se boju za bolj vključujoč jutri in podpri Danes je nov dan!',
        },
        {
          hid: 'og:image',
          property: 'og:image',
          content: 'https://danesjenovdan.si/og-image-donatorska.jpg',
        },
        {
          hid: 'twitter:title',
          property: 'twitter:title',
          content: 'Doniraj za nov dan!',
        },
        {
          hid: 'twitter:description',
          property: 'twitter:description',
          content:
            'Tudi letošnje leto sklepamo z zbiranjem donacij za nadaljnje delovanje. Pridruži se boju za bolj vključujoč jutri in podpri Danes je nov dan!',
        },
        {
          hid: 'twitter:image',
          property: 'twitter:image',
          content: 'https://danesjenovdan.si/og-image-donatorska.jpg',
        },
      ],
    };
  },

  computed: {
    totalDonations() {
      return this.images.reduce((prev, curr) => prev + curr.donation_amount, 0);
    },

    maxDonation() {
      return this.images.reduce(
        (prev, curr) =>
          curr.donation_amount > prev ? curr.donation_amount : prev,
        0,
      );
    },
  },

  async mounted() {
    this.images = await this.$axios.$get('https://podpri.djnd.si/api/images/');
  },

  methods: {
    onShareClick(event, type) {
      const shareLink = 'https://danesjenovdan.si/doniraj';
      const shareText =
        'Danes je nov dan tudi letošnje leto sklepa z zbiranjem donacij za nadaljnje delovanje. Pridruži se boju za bolj vključujoč jutri in podpri Danes je nov dan!';
      const titleText = 'Kupi darilo družbi. Podpri Danes je nov dan!';
      const shareHashtag = '';
      this.openSocialShareLink(
        type,
        titleText,
        shareText,
        shareLink,
        shareHashtag,
      );
    },
    openSocialShareLink(type, titleText, shareText, shareLink, shareHashtag) {
      let url = '';
      const title = encodeURIComponent(titleText);
      if (type === 'fb') {
        const link = encodeURIComponent(shareLink);
        url = `https://www.facebook.com/dialog/feed?app_id=301375193309601&redirect_uri=${link}&link=${link}&ref=responsive&name=${title}`;
      } else if (type === 'tw') {
        const text = encodeURIComponent(
          `${shareText.replace(
            ' Danes je nov dan',
            ' @danesjenovdan',
          )} ${shareHashtag} ${shareLink}`,
        );
        url = `https://twitter.com/intent/tweet?text=${text}`;
      } else if (type === 'mail') {
        const text = `${shareText} ${shareLink}`;
        url = `mailto:?subject=${title}&body=${text}`;
      }
      window.open(url, '_blank');
    },
  },
};
</script>

<style lang="scss" scoped>
// .donation-landing-container {
//   @include media-breakpoint-up(xl) {
//     padding-left: 150px;
//     padding-right: 150px;
//   }
// }

/deep/ .logo {
  width: 230px;

  @include media-breakpoint-up(sm) {
    width: 300px;
  }
}

.mega-header {
  position: relative;
  font-size: 50px;
  line-height: 60px;
  color: rgba(223, 120, 108, 0.98);
  font-weight: 700;
  font-style: italic;
  text-shadow: -1px 1px 0 #333333, 1px 1px 0 #333333, 1px -1px 0 #333333,
    -1px -1px 0 #333333;
  margin-top: 0;
  padding-left: 30px;
  z-index: 200;

  .strikethrough {
    position: relative;
    &::after {
      content: '';
      display: block;
      width: 100%;
      height: 9px;
      background-color: #393939;
      position: absolute;
      left: 0;
      top: 55%;
    }
  }

  @include media-breakpoint-up(md) {
    font-size: 90px;
    line-height: 90px;
    margin-top: 50px;
    padding-left: 0;
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
    font-size: 55px;
    line-height: 70px;
    margin-bottom: 0;
  }
}

h2 {
  font-size: 40px;
  font-style: italic;
  font-weight: 600;
  margin-bottom: 3rem;
}

p {
  font-size: 20px;
  color: #333333;
  font-weight: 200;
  width: 100%;
  max-width: 872px;
  margin-top: 1em;
  margin-bottom: 1em;
  padding-left: 30px;
  padding-right: 30px;

  @include media-breakpoint-up(md) {
    font-size: 30px;
    padding: 0;
  }
}

.gradient-section {
  background-image: linear-gradient(to right, #df786c 0%, #f5d6d3 100%);
  position: absolute;
  opacity: 0.2;
  top: 0;
  bottom: 0;
  width: 100vw;
  margin-left: calc(50% - 50vw);
}

.colored-text {
  color: #dc776b;
  font-weight: 900;
}

.progress {
  width: 100%;
  height: 2rem;
  margin-bottom: 0.5rem;
  background: $light;
  border: 2px solid black;
  overflow: hidden;

  .progress-bar {
    width: 0;
    height: 100%;
    background-image: linear-gradient(
      90deg,
      $color-green,
      $color-yellow,
      $color-red,
      $color-green,
      $color-yellow
    );
    background-size: 400% 100%;
    border-right: 2px solid black;
    animation: progress-animation 2s linear infinite;
  }
}

@-webkit-keyframes progress-animation {
  0% {
    background-position: 100%;
  }
  100% {
    background-position: 0;
  }
}

@keyframes progress-animation {
  0% {
    background-position: 100%;
  }
  100% {
    background-position: 0;
  }
}

.support-section {
  p {
    font-size: 1.5rem;
  }

  .progress-bar-subtitle-left {
    line-height: 1.125;
    span:first-child {
      text-transform: uppercase;
    }
    span:nth-of-type(2) {
      font-size: 60px;
      font-weight: 900;
    }
    span:nth-of-type(3) {
      font-size: 30px;
      font-weight: 900;
    }
  }

  .progress-bar-subtitle-right {
    line-height: 1.125;
    font-size: 1.5rem;
    text-align: right;
    span {
      font-size: 30px;
      font-weight: 900;
    }
  }

  hr {
    border-top: 2px solid #333333;
  }

  h3 {
    font-weight: 700;
    font-style: italic;
  }
}

.limit-like-p {
  width: 100%;
  max-width: 872px;
}
.pad-like-p {
  padding-left: 30px;
  padding-right: 30px;
}

.row-social {
  h1 {
    font-size: 50px;
    line-height: 60px;
    text-align: center;

    @include media-breakpoint-up(md) {
      font-size: 90px;
      line-height: 110px;
    }
  }
}

.square-icon-button {
  display: inline-block;
  width: 100px;
  height: 100px;

  @include media-breakpoint-up(md) {
    width: 150px;
    height: 150px;
  }
}

.donation-social {
  margin-top: 50px;
  padding-bottom: 50px;
  margin-bottom: 20px;
  position: relative;

  &::after {
    content: '';
    display: block;
    width: 100%;
    position: absolute;
    bottom: 0;
    border-bottom: 4px solid $black;
    opacity: 0.2;

    display: none;
  }
}

.problem-col {
  p {
    color: #333333;
    font-size: 27px;
    font-weight: 300;
    font-style: normal;
    letter-spacing: normal;
    line-height: 33.33px;
    text-align: left;
    margin-bottom: 90px;
  }
}
</style>
