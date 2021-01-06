<template>
  <div class="donation-landing-container">
    <div class="row justify-content-center">
      <div class="limit-like-p">
        <h1 class="mega-header" v-t="'donate.title'"></h1>
      </div>
    </div>
    <div class="row justify-content-center">
      <p v-t="'donate.description'"></p>
    </div>
    <div class="row justify-content-center">
      <div class="limit-like-p">
        <h2 v-t="'donate.subtitle'"></h2>
      </div>
    </div>
    <div class="row justify-content-center" id="donation-buttons">
      <div class="limit-like-p">
        <donation-choice-button
          donationType="monthly"
          :href="
            $i18n.locale === 'sl'
              ? '/doniraj/placaj/mesecno'
              : '/donate/checkout/monthly'
          "
        />
        <donation-choice-button
          donationType="once"
          :href="
            $i18n.locale === 'sl'
              ? '/doniraj/placaj/enkrat'
              : '/donate/checkout/once'
          "
        />
      </div>
    </div>
    <volunteer i18nPath="donate.naturalije" />
  </div>
</template>

<script>
import Volunteer from '~/components/Volunteer.vue';
import DonationChoiceButton from '~/components/DonationChoiceButton';

export default {
  components: {
    DonationChoiceButton,
    Volunteer,
  },

  layout: 'default-no-support',

  pageColor: 'secondary',

  nuxtI18n: {
    paths: {
      sl: '/doniraj',
      en: '/donate',
    },
  },

  data() {
    return {
      images: [],
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
            'S svojo donacijo podpri aktivistične projekte in nadaljnje neodvisno delovanje inštituta Danes je nov dan. Pridruži se boju za bolj vključujoč jutri in jih podpri tudi ti!',
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
            'S svojo donacijo podpri aktivistične projekte in nadaljnje neodvisno delovanje inštituta Danes je nov dan. Pridruži se boju za bolj vključujoč jutri in jih podpri tudi ti!',
        },
        {
          hid: 'og:image',
          property: 'og:image',
          content: 'https://danesjenovdan.si/og-image-doniraj.png',
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
            'S svojo donacijo podpri aktivistične projekte in nadaljnje neodvisno delovanje inštituta Danes je nov dan. Pridruži se boju za bolj vključujoč jutri in jih podpri tudi ti!',
        },
        {
          hid: 'twitter:image',
          property: 'twitter:image',
          content: 'https://danesjenovdan.si/og-image-doniraj.png',
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

  // z-index: 200;

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
h2 {
  color: #333333;
  font-size: 40px;
  font-weight: 400;
  font-style: italic;
  letter-spacing: normal;
  line-height: 50px;
  text-align: left;

  @include media-breakpoint-down(sm) {
    font-size: 30px;
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
  max-width: 672px;
  margin-top: 20px;
  margin-bottom: 20px;
  padding-left: 30px;
  padding-right: 30px;

  @include media-breakpoint-up(md) {
    font-size: 30px;
    padding: 0;
  }
}
.limit-like-p {
  width: 100%;
  max-width: 672px;
  margin-top: 20px;
  margin-bottom: 20px;
}
.pad-like-p {
  padding-left: 30px;
  padding-right: 30px;
}

#donation-buttons {
  .square-donation-button {
    float: left;

    &:last-child {
      float: right;
    }

    @include media-breakpoint-down(sm) {
      float: left !important;
    }
  }

  @include media-breakpoint-down(md) {
    width: 317px;
    margin: auto;
  }
}

p.naturalije {
  color: #333333;
  font-size: 20px;
  font-weight: 300;
  font-style: italic;
  letter-spacing: normal;
  line-height: 24.67px;
  text-align: left;
  margin-top: 20px;

  a {
    color: #333333;
    text-decoration: underline;
  }

  &::before {
    content: '';
    background-image: url('../../static/icons/donations/clovek.svg');
    display: block;
    float: left;
    position: relative;
    width: 70px;
    height: 70px;
    background-repeat: no-repeat;
    background-size: contain;
    top: -8px;
  }
}
</style>
