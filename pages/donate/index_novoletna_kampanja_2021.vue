<template>
  <div class="donation-landing-container">
    <donation-logo />
    <div class="row justify-content-center">
      <div class="limit-like-p">
        <h1 class="mega-header">Poženi nov dan!</h1>
      </div>
    </div>
    <div class="row justify-content-center">
      <p>
        Na Danes je nov dan smo v zadnjem letu premagali kar nekaj izzivov in
        uresničili številne projekte. Pri tem smo vse prevečkrat naleteli na
        odpor tistih, ki bi raje videli, da je družba nesolidarna, politika
        netransparentna, okolje prepuščeno kapitalu, misel pa zgolj slepo sledi
        sivemu povprečju. A to nas ni ustavilo in obljubimo, da se bomo za
        boljši jutri borili tudi v 2022.
      </p>
    </div>
    <div class="row justify-content-center">
      <div class="limit-like-p">
        <h2>
          Zato v decembru zbiramo sredstva za čim bolj neodvisno delovanje, pri
          tem pa potrebujemo tudi tvojo pomoč!
        </h2>
      </div>
    </div>
    <div class="row support-section position-relative py-5 my-5">
      <div class="gradient-section"></div>
      <div class="col-lg pr-lg-5">
        <div class="row">
          <div class="col">
            <h2 class="mb-4">
              Delovali bomo
              <span class="colored-text">{{ donationAmountPercentage }} %</span
              ><br class="d-none d-md-block" />
              na vaš pogon!
            </h2>
          </div>
        </div>
        <div class="row">
          <div class="col progress-wrapper">
            <div class="progress">
              <span
                class="progress-bar"
                :class="{
                  'd-none': donationAmountPercentage < 1,
                }"
                :style="{
                  width: `${donationAmountPercentage}%`,
                }"
              >
              </span>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-7 col-md-6">
            <p class="progress-bar-subtitle-left">
              <span>Zbrali smo že</span><br />
              <span>{{ donationAmount }} €</span><br />
              od <br class="d-md-none" /><span>15 000 €!</span><br />
            </p>
          </div>
          <div class="col-5 col-md-6">
            <p class="progress-bar-subtitle-right">
              <span>{{ daysLeft }}</span> dni do<br />
              konca kampanje.
            </p>
          </div>
        </div>
        <hr />
        <div class="row">
          <div class="col">
            <p>
              Čeprav spijemo samo eno kavo na dan, ugašamo luči in se trudimo
              poslovati brezpapirno, delovanje inštituta vseeno stane. Poskrbeti
              moramo za strežnike, na katerih gostimo spletna mesta in
              aplikacije, plačevati licence programov, ki jih uporabljamo pri
              delu, pošiljati pošto, koristiti storitve računovodskega servisa
              in poravnati še cel kup drugih operativnih malenkosti. Tako smo
              izračunali, da že naši osnovni stroški poslovanja nanesejo skupaj
              15 000 evrov na leto.
            </p>
            <p>
              Ker brez tega ni inštituta Danes je nov dan, računov pa ne moremo
              plačevati z zlobnimi tviti, ki jih sicer redno prejemamo, se
              obračamo nate. Pomagaj nam ohraniti neodvisnost in poskrbi, da
              bomo v letu 2022 delovali tudi na tvoj pogon!
            </p>
          </div>
        </div>
      </div>
      <div class="col-lg pl-lg-5">
        <h3 class="mt-4 mt-lg-0">Poženi naše delo!</h3>
        <donation-choice-button-wide
          donation-type="once"
          :href="
            $i18n.locale === 'sl'
              ? '/doniraj/placaj/enkrat'
              : '/en/donate/checkout/once'
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
          donation-type="tax-return"
          :href="
            $i18n.locale === 'sl'
              ? '/doniraj/en-procent'
              : '/en/donate/one-percent'
          "
        />
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="limit-like-p">
        <h1 class="mt-5">Kaj smo naredili v 2021?</h1>
        <p>
          Na Danes je nov dan se borimo za bolj solidarno družbo in bolj
          vključujoče politične procese, nadziramo politike in odločevalce,
          varujemo demokracijo, razkrivamo lažne javnosti na Twitterju in
          skrbimo za okolje ter skupnost. Kako? Oglej si naše projekte!
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
        <h1 class="mt-5">Za kaj se bomo borili v letu 2022?</h1>
        <p>
          Želimo si, da bi bili prihodnje leto čim bolj neodvisni. Da nam
          projektne prijave ne bi odvračale pozornosti od lokalnega aktivizma.
          Da lahko svoja znanja in veščine uporabljamo za krepitev raznolikih
          bojev, kultiviranje javnega, zlasti digitalnega prostora, spodbujanje
          politične participacije in krepitev marginaliziranih glasov. Da se nam
          pri tem pridružiš tudi ti!
        </p>
      </div>
    </div>
    <div class="row my-5 pt-md-5">
      <div class="col-md problem-col">
        <p>
          Tudi na tvoj pogon lahko nadaljujemo z delom, ki smo ga začeli letos.
          Želimo si biti ažurni in se odzivati na konkretne probleme v družbi.
        </p>
        <problem-tile
          title="Politična participacija"
          description="Ker bo 2022 tako imenovano super volilno leto, v katerem nas čakajo lokalne, državnozborske in predsedniške volitve, bomo z najrazličnejšimi aktivnostmi spodbujali čim večjo volilno udeležbo. Delili bomo praktične informacije, skrbeli za izboljšanje političnega diskurza, stranke in politike pa pozivali, da se jasno opredelijo do ključnih družbenih, političnih, ekonomskih in okoljskih vprašanj ter tako poskrbeli za čim večjo informiranost volivk in volivcev."
          icon="pravnapomoc.png"
        />
        <problem-tile
          title="Zaščita okolja"
          description="Pravice narave in pravice do narave so že od začetka delovanja Danes je nov dan med našimi ključnimi prioritetami in nič drugače ne bo v letu 2022. Še naprej bomo sodelovali z nevladnimi in civilnodružbenimi organizacijami s tega področja ter z njihovo pomočjo dihali za ovratnik oblasti, ki na okolje rada pozabi oz. se v zvezi z okoljskimi vprašanji pogosto spreneveda."
          icon="okolje_barvno.png"
        />
      </div>
      <div class="col-md">
        <problem-tile
          title="Dostop do podatkov"
          description="Tudi v letu 2022 bomo na vprašanja v zvezi z odprtostjo podatkov gledali z najrazličnejših vidikov. Občinsko različico Parlametra bomo implementirali v štirih občinah, z novo aplikacijo poskrbeli za transparentnost občinskih proračunov in proračunov nevladnih organizacij ter ponovno analizirali odprtost delovanja Državnega zbora RS. Parlameter bomo nadgradili z možnostjo neposrednega kontaktiranja poslank in poslancev."
          icon="obcinski_podatki_barvno.png"
        />
        <problem-tile
          title="Stanovanjska politika"
          description="Prihodnje leto bo eden od naših temeljnih fokusov vprašanje pomanjkanja dostopnih stanovanj oz. manko ustrezne stanovanjske politike. Ukvarjali se bomo s problemi pomanjkljive ter neustrezne zakonodaje, gradili najemniško skupnost ter izobraževali o pravicah najemnic in najemnikov. Poskušali bomo opolnomočiti veliko, a eno najbolj ranljivih skupin prebivalstva."
          icon="nepremicninski_davek_barvno.png"
        />
        <problem-tile
          title="Sovražni govor"
          description="Še naprej se bomo posvečali razkrivanju toksične politične propagande in manipulacije z javnim mnenjem, na katero bo treba biti v prihajajočem super volilnem letu še posebej pozoren. Raziskovali in opozarjali bomo na aktualne pojavnosti sovražnosti in ekstremističnih idej v medijih in v spletnih okoljih. Nadaljevali bomo s projektom Maršal Twito – Sledilnik, ki beleži in analizira Twitter aktivnost Janeza Janše, in ga še dodatno nadgradili."
          icon="hate_speech_barvno.png"
        />
      </div>
    </div>
    <div class="row support-section position-relative py-5 my-5">
      <div class="gradient-section"></div>
      <div class="col-md pr-md-5 d-flex align-items-center">
        <h1 class="mb-5 mb-lg-0">
          Doniraj in poskrbi, da bomo v 2022 delovali tudi na tvoj pogon!
        </h1>
      </div>
      <div class="col-md pl-md-5">
        <h3 class="second">Poženi naše delo!</h3>
        <donation-choice-button-wide
          donation-type="once"
          :href="
            $i18n.locale === 'sl'
              ? '/doniraj/placaj/enkrat'
              : '/en/donate/checkout/once'
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
          donation-type="tax-return"
          :href="
            $i18n.locale === 'sl'
              ? '/doniraj/en-procent'
              : '/en/donate/one-percent'
          "
        />
      </div>
    </div>
    <div class="row share-section">
      <div class="col-lg-6 position-relative">
        <h1>Več nas bo, prej bomo na cilju!</h1>
        <h2>POVEJ NAPREJ!</h2>
        <img class="share-image" src="../../static/icons/donations/share.png" />
      </div>
      <div class="col-lg-6 pl-lg-5">
        <div class="share-box position-relative">
          <div class="share-background"></div>
          <div class="p-4 p-lg-5 share-text position-relative">
            <div class="share-title">Kopiraj povezavo in deli!</div>
            <div class="share-link">djnd.si/doniraj</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import DonationLogo from '~/components/DonationLogo.vue';
import DonationChoiceButtonWide from '~/components/DonationChoiceButtonWide.vue';
import ProjectTileSmall from '~/components/ProjectTileSmall.vue';
import ProblemTile from '~/components/ProblemTile.vue';

export default {
  components: {
    DonationLogo,
    ProblemTile,
    DonationChoiceButtonWide,
    ProjectTileSmall,
  },
  layout: 'donate',

  pageColor: 'secondary',

  nuxtI18n: {
    paths: {
      sl: '/doniraj-novoletna-kampanja-2021',
      en: '/donate-new-year-campaign-2021',
    },
  },

  data() {
    return {
      images: [],
      donationAmount: 0,
      projects: [
        {
          imageSrc: 'glas-ljudstva.png',
          title: 'Glas ljudstva',
          description:
            'Z več kot 100 nevladnimi in civilnodružbenimi organizacijami pripravljamo 100 zahtev za politične stranke, s katerimi jih bomo pozvali k odgovornejšemu ravnanju.',
          url: 'https://glas-ljudstva.si/',
        },
        {
          imageSrc: 'najemniski-sos.png',
          title: 'Najemniški SOS',
          description:
            'Gradimo najemniško skupnost ter najemnike in najemnice izobražujemo o njihovih pravicah, jim odgovarjamo na pogosta vprašanja in jim omogočamo, da delijo svoje zgodbe.',
          url: 'https://najemniski-sos.si/',
        },
        {
          imageSrc: 'referendum.png',
          title: 'Referendum za pitno vodo',
          description:
            'S številnimi aktivnostmi smo na referendumu pomagali zavrniti škodljive zakonodajne spremembe na področju zaščite voda.',
          url: 'https://danesjenovdan.si/referendum/voda/',
        },
        {
          imageSrc: 'vizjak.png',
          title: 'Brez greha',
          description:
            'Z več kot 43 000 virtualnimi meti smo ustregli prošnji ministra Vizjaka, naj vanj prvi vrže kamen tisti, ki je brez greha, in opozorili na absurdnost njegove obrambe proti očitkom koruptivnosti.',
          url: 'https://brezgreha.si/',
        },
        {
          imageSrc: 'twitto.png',
          title: 'Maršal Twito',
          description:
            'S sledilnikom aktivnosti Janeza Janše na Twitterju že več kot eno leto vsak dan analiziramo količino časa, ki ga premier nameni temu družbenemu omrežju.',
          url: 'https://twito.si/',
        },
        {
          imageSrc: 'pravna-mreza.png',
          title: 'Pravna mreža za varstvo demokracije',
          description:
            'V sklopu Pravne mreže za varstvo demokracije smo nudili pomoč 1098 osebam, na ustavnem sodišču dosegli odpravo odlokov, ki so prepovedovali shode, in vložili predlog zakona o nalezljivih boleznih ter tako prispevali k odpravi protiustavnega stanja.',
          url: 'https://pravna-mreza.si/',
        },
        {
          imageSrc: 'lestvica-transparentnosti.png',
          title: 'Lestvica transparentnosti slovenskih občin',
          description:
            'Analizirali smo odprtost in transparentnost vseh 212 slovenskih občin in prav vsaki priporočili pet ukrepov, s pomočjo katerih bo lahko na tem področju še izboljšala svoje delovanje.',
          url: 'https://danesjenovdan.si/lestvica-transparentnosti/',
        },
        {
          imageSrc: 'ODD.png',
          title: 'Obljuba dela dolg',
          description:
            'Spremljamo in analiziramo izpolnjevanje 51 obljub iz koalicijske pogodbe trenutne vlade in skrbimo za dvig politične odgovornosti.',
          url: 'https://obljubadeladolg.si/',
        },
        {
          imageSrc: 'twitter-brigade.png',
          title: 'Twitter brigade',
          description:
            'Analizirali smo slovensko Twitter sfero in v javni diskurz ponesli pojem astroturfing kot orodje ustvarjanja lažne javnosti. Razkrili smo, kako delujejo lažni profili in poskrbeli, da je bil del omrežja suspendiran.',
          url: 'https://brigade.djnd.si/',
        },
        {
          imageSrc: 'huda-pobuda.png',
          title: 'Huda pobuda',
          description:
            'Na platformi za množično financiranje nevladnih organizacij Huda pobuda smo v prvem pozivu zbrali 4805 evrov in pomagali uresničiti tri projekte.',
          url: 'https://hudapobuda.si/',
        },
        {
          imageSrc: 'odmevi.png',
          title: 'Odmevi prve epidemije',
          description:
            'Z vidika spola smo analizirali oddaje Odmevi in pokazali na prisotnost seksizma, ki se je kazal zlasti pri številu vabljenih gostov in gostij ter izpostavljenih osebah v napovednikih.',
          url: 'https://danesjenovdan.si/odmevi',
        },
        {
          imageSrc: 'indeks-odprtosti.png',
          title: 'Analiza transparentnosti Državnega zbora RS',
          description:
            'Analizirali smo odprtost in transparentnost Državnega zbora Republike Slovenije, priporočila za izboljšave pa smo delili z javnostjo in zaposlenimi v parlamentu.',
          url: 'https://danesjenovdan.si/odprtost-dz',
        },
        {
          imageSrc: 'sramota.png',
          title: 'Mednarodna sramota',
          description:
            'S petmesečnim pregledom tujih medijskih objav o politični situaciji v Sloveniji smo razkrili slabo podobo naše države, ki jo v svetu riše trenutna oblast.',
          url: 'https://sramota.si/',
        },
        {
          imageSrc: 'feministicni.png',
          title: 'Feministični agrument',
          description:
            'Z novo izdajo v zbirki Agrument smo osvetlili 25 konceptov feminizma, ki segajo onkraj binarnih identitetnih, spolnih in seksualnih zamejitev ali izbir.',
          url: 'https://danesjenovdan.si/agrument/30.10.2021',
        },
        {
          imageSrc: 'parlameter.png',
          title: 'Parlameter',
          description:
            'Z orodjem Parlameter še naprej skrbimo za večjo transparentnost političnih procesov v Sloveniji, na Hrvaškem, v Bosni in Hercegovini ter v Ukrajini.',
          url: 'https://parlameter.si/',
        },
        {
          imageSrc: 'peticija-solstvo.png',
          title:
            'Peticija proti uničevanju javnega visokega šolstva in znanosti',
          description:
            'Pomagali smo zbrati več kot 14 000 podpisov in doseči, da je vlada po začetni blokadi le dala soglasje k razpisu za vpis na javne študijske programe.',
          url: 'https://www.akademska-skupnost.si/',
        },
        {
          imageSrc: 'consul.png',
          title: 'Consul',
          description:
            'V letu 2021 smo s šestimi občinami sodelovali pri implementaciji participativnega proračuna s platformo Consul.',
          url: 'https://consul.djnd.si/',
        },
        {
          imageSrc: 'agrument.png',
          title: 'Agrument',
          description:
            'V letu 2021 smo objavili 295 Agrumentov in še naprej skrbeli za opozarjanje na hrbtne plati velikih zgodb ter izpostavljanje majhnih, a pomembnih pripetljajev in zakulisnih dogodkov.',
          url: 'https://danesjenovdan.si/agrument',
        },
      ],
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
    donationAmountPercentage() {
      return Math.round((this.donationAmount / 15000) * 100);
    },
    daysLeft() {
      const today = new Date();
      const deadline = new Date(2022, 0, 3);
      const oneDay = 1000 * 60 * 60 * 24;
      return Math.ceil((deadline.getTime() - today.getTime()) / oneDay);
    },
  },

  async mounted() {
    // this.images = await this.$axios.$get('https://podpri.djnd.si/api/images/');
    const donationStatistics = await this.$axios.$get(
      'https://podpri.djnd.si/api/donation-statistics/10/',
    );
    this.donationAmount = donationStatistics['donation-amount'];
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
    font-size: 50px;
    line-height: 60px;
    margin-bottom: 0;
    padding-left: 30px;
    padding-right: 30px;
  }
}

h2 {
  font-size: 40px;
  font-style: italic;
  font-weight: 600;
  margin-bottom: 3rem;

  @include media-breakpoint-down(sm) {
    font-size: 32px;
    line-height: 40px;
    margin-bottom: 0;
    padding-left: 30px;
    padding-right: 30px;
  }
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

.progress-wrapper {
  @include media-breakpoint-down(sm) {
    padding-left: 45px;
    padding-right: 45px;
  }
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
    font-size: 20px;
  }

  .progress-bar-subtitle-left {
    line-height: 1.125;
    @include media-breakpoint-down(sm) {
      padding-right: 0;
    }
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
    font-size: 20px;
    text-align: right;
    padding-left: 10px;
    span {
      font-size: 30px;
      font-weight: 900;
    }
  }

  hr {
    border-top: 1px solid #333333;
  }

  h3 {
    font-weight: 700;
    font-style: italic;
  }

  h3.second {
    @include media-breakpoint-down(sm) {
      padding-left: 30px;
      padding-right: 30px;
    }
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

.share-section {
  margin-top: 100px;
  margin-bottom: 100px;
  h1 {
    line-height: 1.1;
    margin-bottom: 20px;
  }
  .share-title {
    font-style: italic;
    font-size: 20px;
    text-align: center;
    margin-bottom: 15px;
  }
  .share-link {
    border: 2px solid #333333;
    font-weight: 700;
    font-size: 30px;
    background-color: white;
    padding: 10px 20px;
    text-align: center;
    @include media-breakpoint-down(sm) {
      font-size: 24px;
    }
  }
  .share-image {
    position: absolute;
    height: 75%;
    left: 50%;
    margin-left: 2rem;
    top: 25%;
    @include media-breakpoint-down(lg) {
      display: none;
    }
  }
}

.share-box {
  margin: 45px;
  @include media-breakpoint-down(md) {
    margin-left: 0;
    margin-right: 0;
  }
  @include media-breakpoint-down(sm) {
    margin-left: 30px;
    margin-right: 30px;
  }
}

.share-background {
  background-image: linear-gradient(to right, #df786c 0%, #f5d6d3 100%);
  opacity: 0.2;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}
</style>
