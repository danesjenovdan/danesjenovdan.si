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
            <svg viewBox="12.005 16.033 75.99 67.934" fill="#dd786b">
              <path
                d="M31.756 16.033c-5.075 0-10.122 2.005-13.969 6.031-7.693 8.051-7.715 20.974-.03 29.031l30.78 32.282c.746.787 2.162.787 2.907 0 10.268-10.746 20.513-21.504 30.781-32.25 7.693-8.052 7.693-20.98 0-29.032-7.694-8.051-20.275-8.051-27.969 0l-4.25 4.407-4.25-4.438c-4.147-4.357-9.286-6.052-14-6.031zm0 3.937c3.999 0 8.019 1.625 11.125 4.875l5.687 5.97c.746.787 2.162.787 2.907 0l5.656-5.938c6.212-6.502 16.007-6.501 22.219 0 6.212 6.5 6.212 16.999 0 23.5C69.57 58.61 59.786 68.86 50.006 79.095l-29.344-30.75c-6.207-6.509-6.212-16.999 0-23.5 3.106-3.25 7.095-4.875 11.094-4.875z"
                id="path2"
              />
              <path
                style="fill:transparent;stroke-width:0.30070534"
                d="M 37.342652,67.767099 C 18.090047,46.826364 18.134724,46.877597 16.973735,44.409678 c -1.344773,-2.85859 -1.920544,-5.305628 -1.915189,-8.139595 0.0086,-4.56069 1.508983,-8.704631 4.317498,-11.924728 3.302805,-3.786823 6.989467,-5.546676 11.61956,-5.546676 5.242144,0 7.873474,1.476455 13.852388,7.772658 3.348548,3.526253 4.10063,4.173099 4.851999,4.173099 0.749401,0 1.611575,-0.735442 5.483968,-4.677862 4.822118,-4.909325 6.28592,-5.976108 9.328474,-6.798363 5.302958,-1.433133 10.830326,0.210955 14.897861,4.431292 2.249881,2.334398 3.625629,4.861192 4.435424,8.146396 1.06796,4.332548 0.507725,9.059656 -1.549861,13.077342 C 81.742592,46.003554 80.187686,48.058365 78.6601,49.7279 77.19211,51.332301 70.230527,58.916512 63.189912,66.581706 56.1493,74.246899 50.243163,80.683736 50.065167,80.885788 49.821604,81.162266 46.674044,77.916694 37.342652,67.767099 Z"
                id="path12"
                inkscape:connector-curvature="0"
              />
            </svg>
          </div>
          Hvala za donacijo!
        </h1>
        <h2 class="thankyou__subtitle">Skupaj bomo prevagali.</h2>
        <div class="thankyou__faces">
          <donation-images :images="images" />
        </div>
      </template>
      <template slot="footer">
        <div class="confirm-button-container">
          <confirm-button
            key="next-thankyou"
            @click.native="stage = 'avatar'"
            text="Dodaj svoj obraz na tehtnico"
            color="secondary"
            arrow
          />
          <div class="bottom-back-link">
            <dynamic-link @click="stage = 'share'">
              Preskoči
            </dynamic-link>
          </div>
        </div>
      </template>
    </checkout-stage>

    <checkout-stage v-if="stage === 'avatar'" no-header>
      <template slot="content">
        <h2 class="avatar__title">Dodaj svojo sliko ali si izberi avatar!</h2>
        <avatar-selector @change="onAvatarChange" />
        <hr class="avatar__hr" />
        <div class="avatar__info">
          <div class="form-group">
            <label for="info-url"
              >Lahko dodaš URL do svoje spletne strani ali profila na družbenih
              medijih</label
            >
            <input
              id="info-url"
              v-model="url"
              type="text"
              class="form-control form-control-lg"
              placeholder="URL"
            />
          </div>
          <div class="custom-control custom-checkbox">
            <input
              id="info-display-support"
              v-model="displayMySupport"
              type="checkbox"
              name="displayMySupport"
              class="custom-control-input"
            />
            <label class="custom-control-label" for="info-display-support"
              >Dovolim, da moj avatar dodate na seznam donatorjev.</label
            >
          </div>
          <div class="custom-control custom-checkbox">
            <input
              id="info-image-legal"
              v-model="imageIsLegal"
              type="checkbox"
              name="imageIsLegal"
              class="custom-control-input"
            />
            <label class="custom-control-label" for="info-image-legal"
              >Razumem, da lahko naložim le sliko, ki je izdana pod CC licenco
              ali katere avtorske pravice nosim sam/-a. DJND zavrača odgovornost
              za vsebine, ki jih naložijo uporabniki.</label
            >
          </div>
        </div>
      </template>
      <template slot="footer">
        <div class="confirm-button-container">
          <confirm-button
            key="next-avatar"
            :disabled="!canUploadImage"
            :loading="imageUploading"
            @click.native="uploadImage"
            text="Potrdi"
            color="secondary"
          />
          <div class="bottom-back-link">
            <dynamic-link @click="stage = 'share'">
              Preskoči
            </dynamic-link>
          </div>
        </div>
      </template>
    </checkout-stage>

    <checkout-stage v-if="stage === 'share'" no-header>
      <template slot="content">
        <div class="share__faces">
          <donation-images :images="images" />
        </div>
        <h2 class="share__subtitle">Več nas bo, prej bomo na cilju ...</h2>
        <h1 class="share__title">POVEJ NAPREJ!</h1>
        <div class="share__buttons">
          <button @click="onShareClick($event, 'fb')" type="button">
            <svg
              fill="currentColor"
              viewBox="0 0 1792 1792"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M1343 12v264h-157q-86 0-116 36t-30 108v189h293l-39 296h-254v759h-306v-759h-255v-296h255v-218q0-186 104-288.5t277-102.5q147 0 228 12z"
              ></path>
            </svg>
          </button>
          <button @click="onShareClick($event, 'tw')" type="button">
            <svg
              fill="currentColor"
              viewBox="0 0 1792 1792"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M1684 408q-67 98-162 167 1 14 1 42 0 130-38 259.5t-115.5 248.5-184.5 210.5-258 146-323 54.5q-271 0-496-145 35 4 78 4 225 0 401-138-105-2-188-64.5t-114-159.5q33 5 61 5 43 0 85-11-112-23-185.5-111.5t-73.5-205.5v-4q68 38 146 41-66-44-105-115t-39-154q0-88 44-163 121 149 294.5 238.5t371.5 99.5q-8-38-8-74 0-134 94.5-228.5t228.5-94.5q140 0 236 102 109-21 205-78-37 115-142 178 93-10 186-50z"
              ></path>
            </svg>
          </button>
          <button @click="onShareClick($event, 'mail')" type="button">
            <svg
              fill="currentColor"
              viewBox="0 0 1792 1792"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M1792 710v794q0 66-47 113t-113 47h-1472q-66 0-113-47t-47-113v-794q44 49 101 87 362 246 497 345 57 42 92.5 65.5t94.5 48 110 24.5h2q51 0 110-24.5t94.5-48 92.5-65.5q170-123 498-345 57-39 100-87zm0-294q0 79-49 151t-122 123q-376 261-468 325-10 7-42.5 30.5t-54 38-52 32.5-57.5 27-50 9h-2q-23 0-50-9t-57.5-27-52-32.5-54-38-42.5-30.5q-91-64-262-182.5t-205-142.5q-62-42-117-115.5t-55-136.5q0-78 41.5-130t118.5-52h1472q65 0 112.5 47t47.5 113z"
              ></path>
            </svg>
          </button>
        </div>
      </template>
    </checkout-stage>
  </div>
</template>

<script>
import ConfirmButton from '~/components/ConfirmButton.vue';
import AvatarSelector from '~/components/AvatarSelector.vue';
import DynamicLink from '~/components/DynamicLink.vue';
import CheckoutStage from '~/components/CheckoutStage.vue';
import DonationImages from '~/components/DonationImages.vue';

export default {
  nuxtI18n: {
    paths: {
      sl: '/doniraj/hvala',
      en: '/donate/thanks',
    },
  },
  layout: 'checkout',
  pageColor: 'secondary',
  components: {
    ConfirmButton,
    AvatarSelector,
    DynamicLink,
    CheckoutStage,
    DonationImages,
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
  asyncData({ query }) {
    const token = query.token;
    return {
      token,
    };
  },
  created() {
    if (!this.token) {
      this.stage = 'share';
    }
  },
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
};
</script>

<style lang="scss" scoped>
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
        display: inline-block;
        width: 5rem;
        height: 5rem;
        margin: -0.75rem 0;
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
