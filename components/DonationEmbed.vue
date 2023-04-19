<template>
  <iframe
    class="donation-embed"
    frameborder="0"
    :src="`https://doniraj.lb.djnd.si/danes-je-nov-dan/doniraj${monthlyParam}`"
  ></iframe>
</template>

<!-- <script src="https://cdnjs.cloudflare.com/ajax/libs/iframe-resizer/4.3.2/iframeResizer.min.js"></script> -->
<!-- <script>
iFrameResize({ checkOrigin: false }, '#enprocent_iframe');
</script> -->
<script>
export default {
  name: 'DonationEmbed',
  props: {
    monthly: {
      default: false,
    },
  },
  computed: {
    monthlyParam() {
      return this.monthly ? '?mesecna=true' : '';
    },
  },
};
</script>

<style lang="scss" scoped>
.donation-embed {
  width: 100%;
  height: 100%;
}
</style>
