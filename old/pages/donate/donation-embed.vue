<template>
  <donation-embed :monthly="monthlyDonation" />
</template>

<script>
import DonationEmbed from '~/components/DonationEmbed.vue';

export default {
  components: {
    DonationEmbed,
  },

  layout: 'checkout',

  pageColor: 'secondary',

  nuxtI18n: {
    paths: {
      sl: '/doniraj/placaj/:monthly?',
      en: '/donate/checkout/:monthly?',
    },
  },

  data() {
    const monthlyDonation =
      this.$route.params.monthly === 'monthly' ||
      this.$route.params.monthly === 'mesecno';
    return {
      monthlyDonation,
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

  computed: {},

  async mounted() {},

  methods: {},
};
</script>

<style lang="scss" scoped></style>
