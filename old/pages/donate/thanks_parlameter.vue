<template>
  <div class="checkout">
    <checkout-stage no-header>
      <template slot="content">
        <div class="thankyou">
          <div class="thankyou__icon">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="12.01 16.03 75.99 67.93"
              fill="currentColor"
            >
              <path
                d="M31.76 16.03c-5.08 0-10.13 2-13.97 6.03a21.15 21.15 0 00-.03 29.04l30.78 32.28c.74.78 2.16.78 2.9 0l30.79-32.25a21.15 21.15 0 000-29.04 19.21 19.21 0 00-27.97 0L50 26.5l-4.25-4.44a18.98 18.98 0 00-14-6.03zm0 3.94c4 0 8.01 1.63 11.12 4.88l5.69 5.97c.74.78 2.16.78 2.9 0l5.66-5.94c6.21-6.5 16-6.5 22.22 0 6.21 6.5 6.21 17 0 23.5L50.01 79.09 20.66 48.34c-6.2-6.5-6.21-17 0-23.5a15.3 15.3 0 0111.1-4.87z"
              />
              <path
                fill="transparent"
                d="M37.34 67.77C18.1 46.83 18.14 46.87 16.97 44.4a18.04 18.04 0 01-1.91-8.14c0-4.56 1.5-8.7 4.32-11.92 3.3-3.8 6.99-5.55 11.62-5.55 5.24 0 7.87 1.48 13.85 7.77 3.35 3.53 4.1 4.17 4.85 4.17s1.61-.73 5.48-4.67c4.83-4.91 6.29-5.98 9.33-6.8 5.3-1.43 10.83.2 14.9 4.43a17 17 0 014.44 8.15 19 19 0 01-1.55 13.07 28.3 28.3 0 01-3.64 4.8 23370.95 23370.95 0 01-28.6 31.17c-.24.27-3.39-2.97-12.72-13.12z"
              />
            </svg>
          </div>
          <p v-if="campaign === 1" class="lead text-center thankyou__text">
            Hvala za donacijo!
          </p>
          <p v-else class="lead text-center thankyou__text">
            Tvoja donacija vrijedan je kamenčić potpore mozaiku naših
            aktivnosti. Iskreno se nadamo da će ti Parlametar i nadalje biti
            koristan i zabavan.
          </p>
        </div>
      </template>
    </checkout-stage>
  </div>
</template>

<script>
import CheckoutStage from '~/components/CheckoutStage.vue';

export default {
  nuxtI18n: {
    paths: {
      sl: '/doniraj_parlameter/hvala',
      en: '/donate_parlameter/thanks',
    },
  },
  components: {
    CheckoutStage,
  },
  layout: 'checkout',
  pageColor: 'secondary',
  data() {
    const campaignStringId = this.$route.query.campaign;
    const campaign = ['1', '2', '3'].includes(campaignStringId)
      ? Number(campaignStringId)
      : 1;
    return {
      campaign,
    };
  },
};
</script>

<style lang="scss" scoped>
.checkout {
  .thankyou {
    max-width: 750px;
    margin: 0 auto;

    .thankyou__icon {
      height: 4em;
      color: $color-red;
      margin-bottom: 1em;

      svg {
        width: 100%;
        height: 100%;
      }
    }

    .thankyou__text {
      font-size: 24px;
    }
  }
}
</style>
