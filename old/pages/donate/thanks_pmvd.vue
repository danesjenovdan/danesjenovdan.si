<template>
  <div class="checkout">
    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <checkout-stage v-if="stage === 'thankyou'" no-header>
      <template slot="content">
        <!-- <div class="thankyou__icon">
          <div class="icon icon-heart--secondary" />
        </div> -->
        <h1 class="thankyou__title">
          <div class="icon">
            <svg viewBox="12.005 16.033 75.99 67.934" fill="#160444">
              <path
                id="path2"
                d="M31.756 16.033c-5.075 0-10.122 2.005-13.969 6.031-7.693 8.051-7.715 20.974-.03 29.031l30.78 32.282c.746.787 2.162.787 2.907 0 10.268-10.746 20.513-21.504 30.781-32.25 7.693-8.052 7.693-20.98 0-29.032-7.694-8.051-20.275-8.051-27.969 0l-4.25 4.407-4.25-4.438c-4.147-4.357-9.286-6.052-14-6.031zm0 3.937c3.999 0 8.019 1.625 11.125 4.875l5.687 5.97c.746.787 2.162.787 2.907 0l5.656-5.938c6.212-6.502 16.007-6.501 22.219 0 6.212 6.5 6.212 16.999 0 23.5C69.57 58.61 59.786 68.86 50.006 79.095l-29.344-30.75c-6.207-6.509-6.212-16.999 0-23.5 3.106-3.25 7.095-4.875 11.094-4.875z"
              />
              <path
                id="path12"
                style="fill: transparent; stroke-width: 0.30070534"
                d="M 37.342652,67.767099 C 18.090047,46.826364 18.134724,46.877597 16.973735,44.409678 c -1.344773,-2.85859 -1.920544,-5.305628 -1.915189,-8.139595 0.0086,-4.56069 1.508983,-8.704631 4.317498,-11.924728 3.302805,-3.786823 6.989467,-5.546676 11.61956,-5.546676 5.242144,0 7.873474,1.476455 13.852388,7.772658 3.348548,3.526253 4.10063,4.173099 4.851999,4.173099 0.749401,0 1.611575,-0.735442 5.483968,-4.677862 4.822118,-4.909325 6.28592,-5.976108 9.328474,-6.798363 5.302958,-1.433133 10.830326,0.210955 14.897861,4.431292 2.249881,2.334398 3.625629,4.861192 4.435424,8.146396 1.06796,4.332548 0.507725,9.059656 -1.549861,13.077342 C 81.742592,46.003554 80.187686,48.058365 78.6601,49.7279 77.19211,51.332301 70.230527,58.916512 63.189912,66.581706 56.1493,74.246899 50.243163,80.683736 50.065167,80.885788 49.821604,81.162266 46.674044,77.916694 37.342652,67.767099 Z"
                inkscape:connector-curvature="0"
              />
            </svg>
          </div>
          Hvala za donacijo!
        </h1>
        <!-- <h2 class="thankyou__subtitle">Skupaj bomo prevagali.</h2> -->
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
      sl: '/doniraj_pmvd/hvala',
      en: '/doniraj_pmvd/hvala',
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
  head() {
    return {
      title: 'Doniram za nov dan!',
      meta: [
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        {
          hid: 'description',
          name: 'description',
          content:
            'S svojo donacijo podpiram aktivistične projekte in nadaljnje neodvisno delovanje inštituta Danes je nov dan. Pridruži se boju za bolj vključujoč jutri in jih podpri tudi ti!',
        },
        {
          hid: 'og:title',
          property: 'og:title',
          content: 'Doniram za nov dan!',
        },
        {
          hid: 'og:description',
          property: 'og:description',
          content:
            'S svojo donacijo podpiram aktivistične projekte in nadaljnje neodvisno delovanje inštituta Danes je nov dan. Pridruži se boju za bolj vključujoč jutri in jih podpri tudi ti!',
        },
        {
          hid: 'og:image',
          property: 'og:image',
          content: 'https://danesjenovdan.si/og-image-doniraj.png',
        },
        {
          hid: 'twitter:title',
          property: 'twitter:title',
          content: 'Doniram za nov dan!',
        },
        {
          hid: 'twitter:description',
          property: 'twitter:description',
          content:
            'S svojo donacijo podpiram aktivistične projekte in nadaljnje neodvisno delovanje inštituta Danes je nov dan. Pridruži se boju za bolj vključujoč jutri in jih podpri tudi ti!',
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
@import url('https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@1,800&family=Space+Grotesk:wght@300;400;700&display=swap');

.checkout {
  .thankyou__icon {
    margin-top: 2rem;

    @include media-breakpoint-up(md) {
      display: none;
    }

    .icon {
      margin: 0 auto;
      width: 3.5rem;
      height: 3.5rem;
    }
  }

  .thankyou__title {
    font-family: 'Alegreya', sans-serif;
    color: #160444;
    font-size: 1.85rem;
    text-align: center;
    font-weight: 600;
    text-transform: uppercase;
    font-style: italic;
    margin: 1.25rem 0 0 0;

    @include media-breakpoint-up(md) {
      font-size: 5rem;
      font-weight: 700;
    }

    .icon {
      display: none;

      @include media-breakpoint-up(md) {
        display: inline-flex;
        width: 5rem;
        height: 5rem;
        margin: -0.75rem 0;
      }

      svg {
        width: 100%;
        height: 100%;
      }
    }
  }

  .thankyou__subtitle {
    font-style: italic;
    text-align: center;
    font-weight: 400;
    font-size: 1.5rem;
    margin: 0 0 1.25rem 0;

    @include media-breakpoint-up(md) {
      font-size: 2.5rem;
      font-weight: 300;
    }
  }

  .thankyou__faces,
  .share__faces {
    max-width: 700px;
    margin: auto;
  }

  .confirm-button-container {
    text-align: center;
  }

  .bottom-back-link {
    margin-top: 1rem;

    @include media-breakpoint-up(md) {
      font-size: 1.5rem;
      margin-top: 1.5rem;
    }

    a {
      color: inherit;
      font-style: italic;
      text-decoration: underline;
      font-weight: 600;
    }
  }

  .avatar__title {
    font-size: 1.5rem;
    font-weight: 300;
    max-width: 250px;
    margin: 2rem auto 3rem;
    text-align: center;

    @include media-breakpoint-up(md) {
      max-width: initial;
      font-size: 2.5rem;
    }
  }

  .avatar__hr {
    @include media-breakpoint-up(md) {
      margin: 2rem 0;
    }
  }

  .avatar__info {
    max-width: 540px;
    margin: 0 auto;

    label[for='info-url'] {
      font-weight: 300;
      font-style: italic;
    }
  }

  .custom-checkbox {
    margin-bottom: 1rem;

    .custom-control-label {
      font-size: 1rem;
      line-height: 1.1;
      min-height: 2rem;
      display: flex;
      align-items: center;
    }
  }

  .share__faces {
    margin-top: 2rem;
  }

  .share__subtitle {
    font-size: 1.5rem;
    font-weight: 300;
    margin: 1.25rem 0 0.25rem 0;
    text-align: center;

    @include media-breakpoint-up(md) {
      font-size: 2.5rem;
    }
  }

  .share__title {
    font-size: 1.85rem;
    font-weight: 700;
    margin: 0 0 1.25rem 0;
    font-style: italic;
    text-align: center;

    @include media-breakpoint-up(md) {
      font-size: 5rem;
      font-weight: 700;
      line-height: 1.1;
    }
  }

  .share__buttons {
    display: flex;
    justify-content: center;
    margin: 2rem 0 1rem;
    overflow: hidden;

    @include media-breakpoint-up(md) {
      margin-top: 3.5rem;
    }

    button {
      display: block;
      border: 0;
      background: $color-red;
      margin: 0;
      padding: 1rem;
      width: 4rem;
      height: 4rem;
      color: #fff;
      margin: 0 1.5rem;
      transition: all 0.15s ease;

      &:first-child {
        margin-left: 0;
      }

      &:last-child {
        margin-right: 0;
      }

      @include media-breakpoint-up(md) {
        width: 8rem;
        height: 8rem;
        padding: 2rem;
      }

      &:hover {
        transform: scale(0.95);
      }

      svg {
        width: 100%;
        height: 100%;
      }
    }
  }

  .donation-scale-container {
    max-width: 900px;
    margin: auto;
    margin-top: 100px;
  }
}
</style>
