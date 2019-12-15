<template>
  <div class="checkout">
    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <checkout-stage v-if="stage === 'thankyou'" no-header>
      <template slot="content">
        <div class="thankyou__icon">
          <div class="icon icon-heart--secondary" />
        </div>
        <h1 class="thankyou__title">
          <div class="icon icon-heart--secondary" />
          Hvala za podporo!
        </h1>
        <h2 class="thankyou__subtitle">S tvojo pomočjo smo močnejši.</h2>
        <div class="thankyou__faces">
          <div style="height: 200px; background: #ccc">
            TEHTNICA
          </div>
        </div>
      </template>
      <template slot="footer">
        <div class="confirm-button-container">
          <confirm-button
            key="next-thankyou"
            @click.native="stage = 'avatar'"
            text="Dodaj svoj obraz"
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
        <h2 class="avatar__title">Dodaj svojo sliko ali izberi avatar!</h2>
        <avatar-selector @change="onAvatarChange" />
        <hr class="avatar__hr" />
        <div class="avatar__info">
          <div class="form-group">
            <label for="info-url"
              >TODO: prilepi link ki bo pri tvojem avatarju.</label
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
              >Prikažite me na seznamu podpornikov</label
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
              >TODO: image is legal, we're not liable etc.</label
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
          <div style="height: 200px; background: #ccc">
            TEHTNICA
          </div>
        </div>
        <h2 class="share__subtitle">Več nas bo, prej bomo na cilju!</h2>
        <h1 class="share__title">POVEJ NAPREJ!</h1>
        <div class="share__buttons">
          <button type="button">
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
          <button type="button">
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
          <button type="button">
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
  methods: {
    onAvatarChange(blob) {
      this.imageBlob = blob;
    },
    async uploadImage() {
      if (this.canUploadImage) {
        this.imageUploading = true;
        const formData = new FormData();
        formData.append('url', this.url);
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
      }
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
}
</style>
