<template>
  <input id="share-link" class="form-control" :value="link" onfocus="this.select()">
</template>

<script>
import axios from 'axios';

const SHORTENER_URL = 'https://djnd.si/yomamasofat/';

function fetchShortUrl(url) {
  return axios({
    method: 'POST',
    headers: { 'content-type': 'application/x-www-form-urlencoded' },
    data: `fatmama=${encodeURIComponent(url)}`,
    url: SHORTENER_URL,
  });
}

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
  mounted() {
    fetchShortUrl(this.value)
      .then(res => {
        this.shortLink = res.data;
      })
      .catch(error => {
        // eslint-disable-next-line no-console
        console.error('Error shortening link:', error);
      });
  },
};
</script>
