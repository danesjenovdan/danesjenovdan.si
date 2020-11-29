<template>
  <div class="donation-landing-container">
    <donation-logo />
    <div class="row justify-content-center">
      <div class="limit-like-p">
        <h1 class="mega-header">Podpri nas!</h1>
        <div class="embed-responsive embed-responsive-16by9">
          <div class="embed-responsive-item d-flex align-items-center">
            <iframe
              :src="
                embedUrl('https://www.youtube.com/watch?v=Sb30U8DVGtU', false)
              "
              allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen
            />
          </div>
        </div>
      </div>
    </div>
    <div class="row justify-content-center">
      <p>
        Smo tista skupina prijateljev, ki se je pozimi 2012–13 dobivala v neki
        kleti za Bežigradom in vstajam nudila digitalno podporo ter
        infrastrukturo za vsebinske pobude. Odtlej smo prostočasni aktivizem
        zamenjali za ustanovitev inštituta Danes je nov dan, ki ima že več kot
        30 sodelavk in sodelavcev, od redno zaposlenih pa vse do prostovoljnih
        popoldancev in vikendašic.
      </p>
      <p>V tem času smo med drugim:</p>
    </div>
    <div class="row justify-content-center">
      <donation-info-box
        icon="agrument"
        text="Vsak delovni dan od 10. 2. 2014 naprej objavili agrument"
      />
      <donation-info-box
        icon="coding"
        text="V javno domeno dali že skoraj 2 milijona vrstic kode"
      />
      <donation-info-box
        icon="projects"
        text="Objavili več kot 30 kampanj brez proračuna"
      />
      <donation-info-box
        icon="videos"
        text="Z video parodijo bežali pred cenzuro SDS na 3 video platformah"
      />
    </div>
    <div class="row justify-content-center">
      <p>
        Za nadaljnje neodvisno delovanje potrebujemo tudi tvojo pomoč. Doniraš
        nam lahko:
      </p>
    </div>
    <div class="row justify-content-center">
      <div class="col limit-like-p d-flex">
        <h1>Doniraj za nov dan</h1>
      </div>
    </div>
    <div class="py-5 row justify-content-center">
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
          <div class="col-sm d-flex">
            <a href="/doniraj/placaj?gift=1" class="donate-href"
              >ali
              <span class="underline">Obdaruj bližnje z donacijo DJND</span></a
            >
          </div>
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
        <donation-campaign-progress :end-date="new Date('2020-01-06')" />
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
      <div class="col">
        <donation-choice-button />
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
          @click.native="onShareClick($event, 'fb')"
        />
      </div>
      <div class="col-xs-auto">
        <square-icon-button
          :color="'#228794'"
          icon="twitter"
          @click.native="onShareClick($event, 'tw')"
        />
      </div>
      <div class="col-xs-auto">
        <square-icon-button
          :color="'#df786c'"
          icon="email"
          @click.native="onShareClick($event, 'mail')"
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
import videoMixin from '~/mixins/video.js';

import DonationChoiceButton from '~/components/DonationChoiceButton.vue';

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
    DonationChoiceButton,
  },

  mixins: [videoMixin],

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
        'Danes je nov dan ob sedemletnici delovanja zbira donacije za aktivistične projekte v letu 2020. Pridruži se boju in jih podpri!';
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
          `${shareText} ${shareHashtag} ${shareLink}`,
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
            'Ob sedemletnici delovanja zbiramo donacije za aktivistične projekte v letu 2020. Pridruži se boju in podpri Danes je nov dan!',
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
            'Ob sedemletnici delovanja zbiramo donacije za aktivistične projekte v letu 2020. Pridruži se boju in podpri Danes je nov dan!',
        },
        {
          hid: 'og:image',
          property: 'og:image',
          content: 'https://danesjenovdan.si/djnd-og-doniraj.png',
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
            'Ob sedemletnici delovanja zbiramo donacije za aktivistične projekte v letu 2020. Pridruži se boju in podpri Danes je nov dan!',
        },
        {
          hid: 'twitter:image',
          property: 'twitter:image',
          content: 'https://danesjenovdan.si/djnd-og-doniraj.png',
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

  padding-left: 50px;
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
  max-width: 902px;
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
</style>
