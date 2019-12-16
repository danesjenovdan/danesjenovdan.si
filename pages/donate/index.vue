<template>
  <div class="donation-landing-container">
    <donation-logo />
    <h1 class="mega-header">
      Dragi <span class="strikethrough">Dedek Mraz</span><br />dobri človek!
    </h1>
    <div class="embed-responsive embed-responsive-16by9">
      <div class="embed-responsive-item d-flex align-items-center">
        <iframe
          src="https://player.vimeo.com/video/92594621"
          allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
        />
      </div>
    </div>
    <div class="py-5 row justify-content-center">
      <confirm-button
        key="next-summary"
        :to="''"
        :text="'Podpri'"
        @click.native="$router.push('/doniraj/placaj')"
        color="secondary"
        arrow
        hearts
      />
    </div>
    <div class="row justify-content-center">
      <p>
        Smo tista skupina prijateljev, ki se je pozimi 2012-13 dobivala v kleti
        za Bežigradom in vstajam nudila digitalno podporo ter infrastrukturo za
        vsebinske pobude. V teh sedmih letih smo prostočasni aktivizem zamenjali
        za ustanovitev inštituta Danes je nov dan, ki ima že več kot 30 sodelavk
        in sodelavcev, od redno zaposlenih pa vse do prostovoljnih popoldancev
        in vikendašic.
      </p>
      <p>V sedmih letih obstoja smo med drugim:</p>
    </div>
    <div class="row justify-content-center">
      <donation-info-box icon="agrument" text="Spisali 1600 agrumentov." />
      <donation-info-box
        icon="coding"
        text="V javno domeno dali več kot 1726000 vrstic kode."
      />
      <donation-info-box
        icon="projects"
        text="Objavili več kot 30 kampanj brez proračuna."
      />
      <donation-info-box
        icon="videos"
        text="Z video parodijo bežali cenzuri SDS na 3 video platformah."
      />
    </div>
    <div class="row justify-content-center">
      <p>
        Na inštitutu si želimo, da bi bili v 2020 manj odvisni od dela za
        mednarodne naročnike, ki nam jemlje čas in odvrača fokus od lokalnega
        aktivizma. Svoja znanja in veščine bi radi porabili za krepitev
        raznolikih bojev, kultiviranje javnega, zlasti digitalnega prostora,
        spodbujanje vključujoče politične participacije in krepitev
        marginaliziranih glasov.
      </p>
      <p>
        Obdaruj nas v svojem ali v imenu svojih bližnjih!
      </p>
      <h1>Doniraj za nov dan!</h1>
    </div>
    <div class="py-5 row justify-content-center">
      <confirm-button
        key="next-summary"
        :to="''"
        :text="'Podpri'"
        @click.native="$router.push('/doniraj')"
        color="secondary"
        arrow
        hearts
      />
    </div>
    <div class="row vec-nas-je-kot">
      <div class="col-lg-6">
        <donation-images :images="images" />
      </div>
      <div class="col-lg-6">
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
        <donation-campaign-progress />
      </div>
    </div>
    <div class="py-5 row justify-content-center under-vec-nas-je-kot">
      <h1>Doniraj za nov dan!</h1>
      <confirm-button
        key="next-summary"
        :to="''"
        :text="'Podpri'"
        @click.native="$router.push('/doniraj/placaj')"
        color="secondary"
        arrow
        hearts
      />
    </div>
    <div class="row">
      <p>S tvojo podporo bomo uresničili spodnje projekte:</p>
    </div>
    <div class="row project-line">
      <div class="col-xs-auto">
        <img src="/icons/projects/hate_speech_barvno.svg" />
      </div>
      <div class="col">
        <h2>Ustavimo oglaševanje ob sovražnih vsebinah</h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat.
        </p>
        <div class="partnerships">
          V partnerstvu z <span class="partner">Državljan D</span>
        </div>
        <div class="partnership-images"></div>
      </div>
    </div>
    <div class="row project-line">
      <div class="col-xs-auto">
        <img src="/icons/projects/okolje_barvno.svg" />
      </div>
      <div class="col">
        <h2>Razglasimo podnebno krizo</h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat.
        </p>
        <div class="partnerships">
          V partnerstvu s <span class="partner">PIC</span>,
          <span class="partner">Focus</span>,
          <span class="partner">Umanotera</span>,
          <span class="partner">Greenpeace Slovenija</span>
        </div>
        <div class="partnership-images"></div>
      </div>
    </div>
    <div class="row project-line">
      <div class="col-xs-auto">
        <img src="/icons/projects/obcinski_podatki_barvno.svg" />
      </div>
      <div class="col">
        <h2>Odpiranje občinskih podatkov</h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat.
        </p>
        <div class="partnerships"></div>
        <div class="partnership-images"></div>
      </div>
    </div>
    <div class="row project-line">
      <div class="col-xs-auto">
        <img src="/icons/projects/nepremicninski_davek_barvno.svg" />
      </div>
      <div class="col">
        <h2>Kje je nepremičninski davek?</h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat.
        </p>
        <div class="partnerships">
          V partnerstvu s <span class="partner">Kje bomo pa jutri spali?</span>
        </div>
        <div class="partnership-images"></div>
      </div>
    </div>
    <div class="row project-line">
      <div class="col-xs-auto">
        <img src="/icons/projects/medijska_reprezentacija_barvno.svg" />
      </div>
      <div class="col">
        <h2>Zastopanost spolov v medijih</h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat.
        </p>
        <div class="partnerships"></div>
        <div class="partnership-images"></div>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <h1>Več nas bo, prej bomo na cilju! POVEJ NAPREJ!</h1>
      </div>
    </div>
    <div class="row justify-content-center donation-social">
      <div class="col-xs-auto">
        <square-icon-button
          :color="'#228794'"
          icon="facebook"
          href="https://facebook.com/danesjenovdan"
        />
      </div>
      <div class="col-xs-auto">
        <square-icon-button
          :color="'#228794'"
          icon="twitter"
          href="https://facebook.com/danesjenovdan"
        />
      </div>
      <div class="col-xs-auto">
        <square-icon-button
          :color="'#df786c'"
          icon="email"
          href="https://facebook.com/danesjenovdan"
        />
      </div>
    </div>
  </div>
</template>

<script>
import DonationLogo from '~/components/DonationLogo.vue';
import ConfirmButton from '~/components/ConfirmButton.vue';
import DonationInfoBox from '~/components/DonationInfoBox.vue';
import DonationImages from '~/components/DonationImages.vue';
import DonationMilestones from '~/components/DonationMilestones.vue';
import DonationSummary from '~/components/DonationSummary.vue';
import DonationCampaignProgress from '~/components/DonationCampaignProgress.vue';
import SquareIconButton from '~/components/SquareIconButton.vue';

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
    DonationInfoBox,
    DonationImages,
    DonationMilestones,
    DonationSummary,
    DonationCampaignProgress,
    SquareIconButton,
  },

  data() {
    return {
      images: [],
    };
  },

  async mounted() {
    this.images = await this.$axios.$get('https://podpri.djnd.si/api/images/');
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
};
</script>

<style lang="scss" scoped>
// .donation-landing-container {
//   @include media-breakpoint-up(xl) {
//     padding-left: 150px;
//     padding-right: 150px;
//   }
// }
.logo {
  width: 300px;
}
.mega-header {
  font-size: 50px;
  line-height: 60px;
  color: rgba(223, 120, 108, 0.98);
  font-weight: 700;
  font-style: italic;
  text-shadow: -1px 1px 0 #333333, 1px 1px 0 #333333, 1px -1px 0 #333333,
    -1px -1px 0 #333333;

  margin-bottom: -10px;
  z-index: 100;

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
    font-size: 110px;
    line-height: 120px;
  }
}
.embed-responsive {
  z-index: 1;
}
h1 {
  font-size: 90px;
  font-weight: 500;
  line-height: 100px;
  font-style: italic;
}
p {
  font-size: 40px;
  color: #333333;
  font-weight: 200;
  width: 100%;
  max-width: 902px;
  margin-bottom: 1em;
}
.vec-nas-je-kot {
  background-image: linear-gradient(
    to right,
    rgba(205, 172, 84, 0.2) 0%,
    rgba(223, 120, 108, 0.2) 100%
  );
  padding: 20px 0;
}
.under-vec-nas-je-kot {
  background-image: linear-gradient(
    to right,
    rgba(205, 172, 84, 0.2) 0%,
    rgba(223, 120, 108, 0.2) 100%
  );

  padding: 20px;

  h1 {
    font-size: 60px;
    font-weight: 500;
    line-height: 100px;
    font-style: italic;
    margin-right: 30px;
  }
}
.project-line {
  background-color: rgba(223, 120, 108, 0.05);
  padding: 60px;
  margin-bottom: 30px;

  img {
    width: 90px;
    height: auto;
    margin-right: 30px;
  }

  h2 {
    font-weight: 500;
    font-style: italic;
    font-size: 30px;
  }

  p {
    font-size: 20px;
  }

  .partnerships {
    font-weight: 200;
    .partner {
      text-transform: uppercase;
      font-weight: 700;
    }
  }
}
.square-icon-button {
  display: inline-block;
}
.donation-social {
  margin-top: 50px;
}
</style>
