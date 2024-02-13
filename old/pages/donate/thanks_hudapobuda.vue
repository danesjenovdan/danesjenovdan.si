<template>
  <div class="checkout">
    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <checkout-stage v-if="stage === 'thankyou'" no-header class="hudapobuda">
      <template slot="content">
        <div class="text-center">
          <img
            src="/img/hudapobuda-donations/nvo-crowdfunder-hvala.svg"
            class="mx-4"
          />
        </div>
        <h1 class="thankyou__title">Hvala za podporo!</h1>
        <p class="thankyou__subtitle">
          Uspešno smo prejeli tvojo donacijo. Hvala, ker nam pomagaš
          uresničevati hude pobude, ki krepijo skupnosti!
        </p>
      </template>
    </checkout-stage>
  </div>
</template>

<script>
// import ConfirmButton from '~/components/ConfirmButton.vue';
// import AvatarSelector from '~/components/AvatarSelector.vue';
// import DynamicLink from '~/components/DynamicLink.vue';
import CheckoutStage from '~/components/CheckoutStage.vue';
// import DonationImages from '~/components/DonationImages.vue';

export default {
  nuxtI18n: {
    paths: {
      sl: '/doniraj_hudapobuda/hvala',
      en: '/doniraj_hudapobuda/hvala',
    },
    fallbackLocale: 'sl',
  },
  components: {
    // ConfirmButton,
    // AvatarSelector,
    // DynamicLink,
    CheckoutStage,
    // DonationImages,
  },
  layout: 'checkout',
  pageColor: 'secondary',
  asyncData({ query }) {
    const token = query.token;
    return {
      token,
    };
  },
  data() {
    return {
      error: null,
      stage: 'thankyou',
      url: null,
      displayMySupport: false,
      imageIsLegal: false,
      imageUploading: false,
      imageBlob: null,
      images: [],
    };
  },
  computed: {
    canUploadImage() {
      return (
        this.token &&
        this.displayMySupport &&
        this.imageIsLegal &&
        this.imageBlob
      );
    },
  },
  // created() {
  //   if (!this.token) {
  //     this.stage = 'share';
  //   }
  // },
  async mounted() {
    this.images = await this.$axios.$get('https://podpri.djnd.si/api/images/');
  },
  methods: {
    onAvatarChange(blob) {
      this.imageBlob = blob;
    },
    async uploadImage() {
      if (this.canUploadImage) {
        this.imageUploading = true;
        const formData = new FormData();
        if (this.url && this.url !== '') {
          formData.append('url', this.url);
        }
        formData.append(
          'image',
          this.imageBlob,
          Date.now().toString(36) + '.jpg',
        );
        await this.$axios.$patch(
          `https://podpri.djnd.si/api/images/${this.token}/`,
          formData,
        );
        this.stage = 'share';
        this.images = await this.$axios.$get(
          'https://podpri.djnd.si/api/images/',
        );
      }
    },
    onShareClick(event, type) {
      const shareLink = 'https://danesjenovdan.si/doniraj';
      const shareText =
        'S svojo donacijo podpiram aktivistične projekte in nadaljnje neodvisno delovanje inštituta Danes je nov dan. Pridruži se boju za bolj vključujoč jutri in jih podpri tudi ti!';
      const titleText = 'Doniram za nov dan!';
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
            'Danes je nov dan',
            '@danesjenovdan',
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
@import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;700&amp;display=swap');

.checkout {
  img {
    max-width: 20rem;
  }

  .thankyou__title {
    font-family: $font-family-okolaks;
    font-size: 1.85rem;
    text-align: center;
    font-weight: 600;
    text-transform: uppercase;
    margin: 1.25rem 0 0 0;

    @include media-breakpoint-up(md) {
      font-size: 5rem;
      font-weight: 700;
    }
  }

  .thankyou__subtitle {
    font-family: $font-family-comfortaa;
    text-align: center;
    font-weight: 400;
    font-size: 1.25rem;
    margin: 0 0 1.25rem 0;

    @include media-breakpoint-up(md) {
      font-size: 2.5rem;
      font-weight: 300;
    }
  }
}
</style>
