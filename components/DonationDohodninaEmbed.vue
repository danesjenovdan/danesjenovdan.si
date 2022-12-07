<template>
  <iframe
    id="enprocent_iframe"
    frameborder="0"
    width="800"
    height="600"
    style="max-width: 100%"
    src="https://www.cnvos.si/enprocent/embed/v2_alt/?address=Parmova%20ulica%2020&city=Ljubljana&name=Danes%20je%20nov%20dan%2C%20In%C5%A1titut%20za%20druga%20vpra%C5%A1anja&percent=1.0&postalCode=1000&taxNumber=54561710"
  ></iframe>
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
