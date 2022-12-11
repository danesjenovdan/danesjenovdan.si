<template>
  <div class="checkout">
    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <checkout-stage v-if="stage === 'thankyou'" no-header>
      <template slot="content">
        <div class="row justify-content-center my-5">
          <div class="col-md-6 col-lg-4">
            <!-- <img src="../../static/icons/donations/hvala.svg" /> -->
            <img
              class="img-fluid"
              src="../../static/icons/donations/2022/hvala.png"
            />
          </div>
        </div>
        <div class="row justify-content-center">
          <h2 class="thankyou__title">HVALA ZA DONACIJO!</h2>
          <!-- <p class="text-center">
            V letu 2022 bomo lahko delovali tudi na tvoj pogon!
          </p> -->
          <p class="text-center">
            Tvoja donacija predstavlja še en kamenček podpore v mozaiku našega
            delovanja. Iskreno upamo, da ti bodo naši projekti še naprej v
            veselje in ponos.
          </p>
        </div>
        <div class="row justify-content-center mt-5">
          <NuxtLink to="/doniraj" class="back">Nazaj na spletno mesto</NuxtLink>
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
      sl: '/doniraj/hvala',
      en: '/donate/thanks',
    },
  },
  components: {
    CheckoutStage,
  },
  layout: 'checkout',
  pageColor: 'secondary',
  // asyncData({ query }) {
  //   const token = query.token;
  //   return {
  //     token,
  //   };
  // },
  data() {
    return {
      error: null,
      stage: 'thankyou',
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
};
</script>

<style lang="scss" scoped>
.checkout {
  p {
    font-size: 20px;
    color: #333333;
    font-weight: 200;
    width: 100%;
    max-width: 872px;
    margin-top: 20px;
    margin-bottom: 20px;
    padding-left: 30px;
    padding-right: 30px;

    @include media-breakpoint-up(md) {
      font-size: 30px;
      padding: 0;
    }
  }

  .back {
    color: #333333;
    font-weight: 600;
    font-size: 20px;
    font-style: italic;
    text-decoration: underline;

    @include media-breakpoint-down(sm) {
      font-size: 16px;
    }

    &:hover {
      text-decoration: none;
    }
  }

  .thankyou__title {
    font-size: 1.85rem;
    text-align: center;
    font-weight: 600;
    text-transform: uppercase;
    font-style: italic;
    margin: 30px 0;

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
}
</style>
