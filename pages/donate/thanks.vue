<template>
  <div class="checkout">
    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <div v-else-if="stage === 'thankyou'" class="checkout__thankyou">
      <div class="thankyou__content">
        <div class="icon-container">
          <div class="icon icon-heart--secondary" />
        </div>
        <h1 class="checkout__title">Hvala za podporo!</h1>
        <h2 class="checkout__subtitle">S tvojo pomočjo smo močnejši.</h2>
        <div class="faces-container">
          <div style="height: 200px; background: #ccc">
            TEHTNICA
          </div>
        </div>
      </div>
      <div class="confirm-button-container">
        <confirm-button
          key="next-thankyou"
          @click.native="stage = 'select-avatar'"
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
    </div>

    <div v-else-if="stage === 'select-avatar'" class="checkout__select-avatar">
      <h2 class="checkout__subtitle">Dodaj svojo sliko ali izberi avatar!</h2>
      <avatar-selector />
      <div class="confirm-button-container">
        <confirm-button
          key="next-select-avatar"
          @click.native="stage = 'share'"
          text="Potrdi"
          color="secondary"
        />
      </div>
    </div>

    <div v-else-if="stage === 'share'" class="checkout__share">
      <div class="faces-container">
        <div style="height: 200px; background: #ccc">
          TEHTNICA
        </div>
      </div>
      <h2 class="checkout__subtitle">Več nas bo, prej bomo na cilju!</h2>
      <h1 class="checkout__title">POVEJ NAPREJ!</h1>
      <div class="social-buttons">
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
    </div>
  </div>
</template>

<script>
import ConfirmButton from '~/components/ConfirmButton.vue';
import AvatarSelector from '~/components/AvatarSelector.vue';
import DynamicLink from '~/components/DynamicLink.vue';

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
  },
  data() {
    return {
      error: null,
      // stage: 'thankyou',
      stage: 'thankyou',
      displayMySupport: false,
    };
  },
  asyncData({ query }) {
    const token = query.token === 'true' || query.token === '1';
    return {
      token,
    };
  },
  methods: {},
};
</script>

<style lang="scss" scoped>
.checkout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 1.5rem 0 1rem;

  .checkout__title {
    font-size: 1.85rem;
    text-align: center;
    font-weight: 600;
    text-transform: uppercase;
    font-style: italic;
    margin: 1.25rem 0 0 0;
  }

  .checkout__subtitle {
    font-style: italic;
    text-align: center;
    font-weight: 400;
    font-size: 1.5rem;
  }

  .confirm-button-container {
    margin-top: 2rem;
    text-align: center;
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

  .payment-switcher {
    margin-bottom: 2rem;
  }

  .checkout__thankyou {
    min-height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin: 0 auto;

    .thankyou__content {
      flex: 1;
      display: flex;
      flex-direction: column;

      .icon {
        margin: 0 auto;
        width: 3.5rem;
        height: 3.5rem;
      }

      .checkout__subtitle {
        margin-bottom: 2rem;
      }

      .faces-container {
        margin: auto 0;
      }
    }
  }

  .checkout__select-avatar {
    .checkout__subtitle {
      font-style: normal;
      font-weight: 300;
      max-width: 250px;
      margin: 0 auto 1.5rem;
    }
  }

  .checkout__share {
    min-height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin: 0 auto;

    .faces-container {
      margin: auto 0;
    }

    .checkout__subtitle {
      font-style: normal;
      font-weight: 300;
      margin: 2rem 0 0 0;
    }

    .checkout__title {
      margin: 0.25rem 0 0 0;
      font-weight: 700;
    }

    .social-buttons {
      display: flex;
      justify-content: space-evenly;
      margin-top: 2rem;
      margin-bottom: 1rem;

      button {
        display: block;
        border: 0;
        background: $color-red;
        margin: 0;
        padding: 1rem;
        width: 4rem;
        height: 4rem;
        color: #fff;

        svg {
          width: 100%;
          height: 100%;
        }
      }
    }
  }

  .bottom-back-link {
    margin-top: 1rem;

    a {
      color: inherit;
      font-style: italic;
      text-decoration: underline;
      font-weight: 600;
    }
  }
}
</style>
