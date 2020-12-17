<template>
  <div class="donation-landing-container">
    <donation-logo />
    <div class="row justify-content-center">
      <div class="limit-like-p">
        <h1 class="mega-header">Doniraj za nov dan!</h1>
      </div>
    </div>
    <div class="row justify-content-center">
      <p>Podpri naše delo v 2021!</p>
    </div>
    <div class="row justify-content-center">
      <div class="limit-like-p pad-like-p">
        <confirm-button
          key="next-summary"
          :to="''"
          :text="'Podpri'"
          color="secondary"
          arrow
          hearts
          @click.native="$router.push('/doniraj/placaj')"
        />
      </div>
    </div>
    <div class="row justify-content-center">
      <p>
        Leto sklepamo tudi z vsebinsko bilanco oz. poročilom o opravljenem delu.
        Izpostavljamo najpomembnejše dosežke in mejnike, ki smo jih dosegli
        tekom zadnjega kroga okoli sonca.
      </p>
    </div>
    <div class="row">
      <div class="achievement-tiles-container">
        <achievement-tile
          icon="consul"
          text="V 7 občinah smo namestili Consul."
          href="https://odlocamo-skupaj.nova-gorica.si/"
        />
        <achievement-tile
          icon="parlameter"
          text="V 3 državah vzdržujemo Parlameter."
          href="https://parlameter.org/"
        />
        <achievement-tile
          icon="pravnapomoc"
          text="Do brezplačne pravne pomoči smo pomagali 89 protestnikom."
          href="https://www.facebook.com/danesjenovdan/photos/a.415560015192794/3002029953212441"
        />
        <achievement-tile
          icon="boter"
          text="Raziskovalno smo na sledi skupini 500 potencialnih Twitter trolov."
          href="https://acfslovenia.si/podprti-projekti/twitter-brigade/"
        />
        <achievement-tile
          icon="stanovanja"
          text="Izpostavili smo 6 korona kiksov na področju stanovanjske politike."
          href="https://danesjenovdan.si/korona-kiks"
        />
        <achievement-tile
          icon="narava"
          text="Skupaj s koalicijo okoljskih NVO smo dosegli, da je peticijo Narave ne damo podpisalo več kot 36 000 ljudi."
          href="https://www.naravenedamo.si/"
        />
        <achievement-tile
          icon="zenske"
          text="Analizirali smo reprezentacijo spola v oddaji Odmevi."
          href="https://docs.google.com/spreadsheets/d/1VBe_QYF71K9nlUZW34OJDh2z2dPxoC_GG-zAUZ8A6y0/edit?usp=sharing"
        />
        <achievement-tile
          icon="PP"
          text="V zvezi s participativnim proračunom za besedo držimo 56 županov."
          href="https://danesjenovdan.si/participativni-proracun/"
        />
        <achievement-tile
          icon="brezstrahu"
          text="Izpostavili smo dvoličnost SMC in DeSUS ob vstopu v Janševo vlado."
          href="https://brezstrahu.si/"
        />
        <achievement-tile
          icon="fasizem"
          text="V Fašizmu za telebane smo popisali 39 primerov fašizacije slovenske družbe."
          href="https://fasizem.djnd.si/"
        />
        <achievement-tile
          icon="agrument"
          text="Za letošnje agrumente smo do decembra porabili 41569 besed."
          href="https://danesjenovdan.si/agrument"
        />
        <achievement-tile
          icon="knjiga1"
          text="Izdali smo knjigo Abecedarij svobode govora."
        />
        <achievement-tile
          icon="knjiga2"
          text="Izdali smo knjigo Psihoanalitski agrument."
        />
        <achievement-tile
          icon="pocivalsek"
          text="Počivalškov govor ob vstopu SMC v vlado smo opremili s satiričnimi podnapisi in sprožili debato o pošteni uporabi avtorskih materialov."
          href="https://danesjenovdan.si/videogalerija?video=https%3A%2F%2Fyoutu.be%2FMnUuwDKA5c4"
        />
        <achievement-tile
          icon="sodelovanje"
          text="Sodelovali smo s številnimi domačimi in tujimi civilnodružbenimi in nevladnimi organizacijami."
          href="https://danesjenovdan.si/o-nas"
        />
        <achievement-tile
          icon="pojavljanja"
          text="Kot strokovni sogovorniki smo pogosto nastopali v medijih"
          href="https://danesjenovdan.si/pojavljanja"
        />
        <achievement-tile
          icon="zicar"
          text="Ob petletnici sramotne žice na meji smo lansirali spletno igro Žicar 2.0."
          href="https://danesjenovdan.si/zicar/"
        />
        <achievement-tile
          icon="zradirani"
          text="V boju proti deložaciji smo podprli organizacije in ustvarjalce z Metelkove 6."
          href="https://www.zradirani-metelkova6.si/"
        />
        <achievement-tile
          icon="newsgradient"
          text="Objavili smo Newsgradient Bosna in Hercegovina."
          href="https://newsgradient.org/"
        />
        <achievement-tile
          icon="twito"
          text="Beležimo in analiziramo Twitter aktivnost Janeza Janše."
          href="https://twito.si/"
        />
      </div>
    </div>
    <div class="row justify-content-center">
      <p>
        V letu 2021 bi na inštitutu radi nadaljevali z aktivnostmi, ki se
        osredotočajo na spodbujanje politične participacije, sledenje političnih
        obljub, promocijo človekovih pravic in vključenosti, kultiviranje
        javnega in skupnega ter krepitev marginaliziranih glasov.
      </p>
      <p>Obdaruj nas!</p>
    </div>
    <div class="row justify-content-center">
      <div class="col limit-like-p d-flex">
        <h1>Doniraj za nov dan</h1>
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col limit-like-p d-flex">
        <div class="row">
          <div class="col-sm">
            <confirm-button
              key="next-summary"
              :to="''"
              :text="'Podpri nas'"
              color="secondary"
              arrow
              hearts
              @click.native="$router.push('/doniraj/placaj')"
            />
          </div>
          <!-- <div class="col-sm d-flex">
            <a href="/doniraj/placaj?gift=1" class="donate-href"
              >ali
              <span class="underline">Obdaruj bližnje z donacijo DJND</span></a
            >
          </div> -->
        </div>
      </div>
    </div>
    <div class="row vec-nas-je-kot align-items-center">
      <div class="col-md-6">
        <donation-images :images="images" class="pr-md-5" />
      </div>
      <div class="col-md-6">
        <donation-milestones :number-of-donations="images.length" />
      </div>
    </div>
    <div class="row align-items-center">
      <div class="col">
        <donation-summary
          :total-donations="totalDonations"
          :max-donation="maxDonation"
        />
      </div>
      <div class="col">
        <donation-campaign-progress
          :end-date="new Date('2021-01-06')"
          :total-days="35"
        />
      </div>
    </div>
    <div
      class="py-5 row justify-content-center align-items-center under-vec-nas-je-kot"
    >
      <h1>Doniraj za nov dan</h1>
      <confirm-button
        key="next-summary"
        :to="''"
        :text="'Podpri nas'"
        color="secondary"
        arrow
        hearts
        @click.native="$router.push('/doniraj/placaj')"
      />
    </div>
    <div class="row">
      <div class="col-md problem-col">
        <p>
          S tvojo podporo bomo nadaljevali s temami, ki smo jih zastavili v
          lanski donatorski kampanji.
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
    <div class="row row-social">
      <div class="col">
        <h1>Več nas bo, prej bomo na&nbsp;cilju&nbsp;...</h1>
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
import ConfirmButton from '~/components/ConfirmButton.vue';
import DonationImages from '~/components/DonationImages.vue';
import DonationMilestones from '~/components/DonationMilestones.vue';
import DonationSummary from '~/components/DonationSummary.vue';
import DonationCampaignProgress from '~/components/DonationCampaignProgress.vue';
import SquareIconButton from '~/components/SquareIconButton.vue';

import AchievementTile from '~/components/AchievementTile.vue';
import ProblemTile from '~/components/ProblemTile.vue';

export default {
  layout: 'donate',

  pageColor: 'secondary',

  nuxtI18n: {
    paths: {
      sl: '/doniraj',
      en: '/donate',
    },
  },

  components: {
    DonationLogo,
    ConfirmButton,
    DonationImages,
    DonationMilestones,
    DonationSummary,
    DonationCampaignProgress,
    SquareIconButton,
    AchievementTile,
    ProblemTile,
  },

  data() {
    return {
      images: [],
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
.donate-href {
  width: 100%;
  max-width: 250px;
  font-style: italic;
  font-size: 25px;
  font-weight: 500;
  line-height: 32px;
  text-decoration: underline;
  color: $black;

  margin: 20px;
  text-decoration: none;

  .underline {
    text-decoration: underline;
  }

  @include media-breakpoint-up(lg) {
    margin-left: 80px;
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
.embed-responsive {
  z-index: 1;
}
h1 {
  font-size: 80px;
  font-weight: 600;
  line-height: 100px;
  font-style: italic;
  letter-spacing: -1px;
  margin-top: 50px;
  margin-bottom: 50px;
  text-align: left;
  width: 100%;

  @include media-breakpoint-down(sm) {
    font-size: 55px;
    line-height: 70px;
    margin-bottom: 0;
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
.limit-like-p {
  width: 100%;
  max-width: 872px;
}
.pad-like-p {
  padding-left: 30px;
  padding-right: 30px;
}
.donation-info-box {
  @include media-breakpoint-up(md) {
    margin-top: 40px;
    margin-bottom: 40px;
  }
}
.vec-nas-je-kot {
  margin-top: 50px;
  margin-bottom: 50px;
  margin-left: -1.5em;
  margin-right: -1.5em;
  background-image: linear-gradient(
    to right,
    rgba(205, 172, 84, 0.2) 0%,
    rgba(223, 120, 108, 0.2) 100%
  );
  padding: 40px 1.5em 20px 1.5em;

  @include media-breakpoint-up(md) {
    margin-left: -3em;
    margin-right: -3em;
    padding: 40px 3em 20px 3em;
  }
}
.under-vec-nas-je-kot {
  margin-top: 50px;
  margin-bottom: 70px;
  background-image: linear-gradient(
    to right,
    rgba(205, 172, 84, 0.2) 0%,
    rgba(223, 120, 108, 0.2) 100%
  );

  padding: 20px;

  h1 {
    width: auto;
    font-size: 60px;
    line-height: 140px;
    font-weight: 700;
    line-height: 100px;
    font-style: italic;
    @include media-breakpoint-up(xl) {
      margin-right: 60px;
    }

    @include media-breakpoint-down(sm) {
      margin-top: 0;
      font-size: 55px;
      line-height: 70px;
    }
  }
}
.project-line {
  background-color: rgba(223, 120, 108, 0.05);
  padding: 30px;
  margin-bottom: 30px;
  display: flex;
  justify-content: center;

  img {
    width: 90px;
    height: auto;
    margin-right: 30px;
    margin-bottom: 20px;
  }

  h2 {
    font-weight: 600;
    font-style: italic;
    font-size: 40px;
    min-width: 250px;
  }

  p {
    font-size: 20px;
    padding-left: 0;
    padding-right: 0;
  }

  .partnerships {
    font-weight: 200;
    .partner {
      text-transform: uppercase;
      font-weight: 700;
    }
  }

  .partnership-images {
    img {
      margin-top: 20px;
      width: 50px;
      height: auto;
    }
  }

  @include media-breakpoint-up(md) {
    padding: 60px;
  }
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
.confirm-button {
  height: 100px;
  margin-top: 22px;
  margin-bottom: 22px;

  @include media-breakpoint-up(md) {
    height: 150px;
    width: 500px;
    margin-top: 0;
    margin-bottom: 0;
  }
}
.donation-scale-container {
  margin-bottom: 150px;

  @include media-breakpoint-up(md) {
    // position: absolute;
    // bottom: 40px;
    margin-bottom: 0;
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
.achievement-tiles-container {
  position: relative;
  margin: auto;
  display: block;
  padding-left: 5vw;
  padding-top: 100px;
  padding-bottom: 100px;

  @include media-breakpoint-down(sm) {
    padding-left: 0;
    padding-top: 10px;
    padding-bottom: 10px;
  }
}
</style>
