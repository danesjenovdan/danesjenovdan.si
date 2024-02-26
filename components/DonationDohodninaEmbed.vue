<template>
  <iframe id="enprocent_iframe" frameborder="0" width="800" height="537" style="max-width: 100%"
    src="https://www.cnvos.si/enprocent/embed/v2/?address=RESLJEVA%20CESTA%2025&city=Ljubljana&name=DANES%20JE%20NOV%20DAN%2C%20IN%C5%A0TITUT%20ZA%20DRUGA%20VPRA%C5%A0ANJA&percent=1.0&postalCode=1000&taxNumber=54561710"></iframe>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/iframe-resizer/4.3.2/iframeResizer.min.js"></script>
<script>
iFrameResize({ checkOrigin: false }, '#enprocent_iframe');
</script>
<script>
export default {
  name: 'DonationDohodninaEmbed',
};
</script>

<style lang="scss" scoped>
#enprocent_iframe {
  border: 1px solid #df786c;
}
</style>
