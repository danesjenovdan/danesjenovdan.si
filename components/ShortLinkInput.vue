<template>
  <input id="share-link" class="form-control" :value="link" onfocus="this.select()">
</template>

<script>
const SHORTENER_URL = 'https://djnd.si/yomamasofat/';

export default {
  name: 'ShortLinkInput',
  props: {
    value: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      shortLink: null,
    };
  },
  computed: {
    link() {
      return this.shortLink || this.value;
    },
  },
  async mounted() {
    try {
      this.shortLink = await this.fetchShortUrl(this.value);
    } catch (error) {
      // eslint-disable-next-line no-console
      console.error('Error shortening link:', error);
    }
  },
  methods: {
    fetchShortUrl(url) {
      return this.$axios.$get(`${SHORTENER_URL}?fatmama=${encodeURIComponent(url)}`);
    },
  },
};
</script>
