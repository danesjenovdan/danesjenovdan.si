<template>
  <iframe
    id="odprti-racuni"
    frameborder="0"
    width="996"
    height="960"
    src="https://odprtiracuni-nvo.djnd.si/9/"
  ></iframe>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/iframe-resizer/4.3.2/iframeResizer.min.js"></script>
<script>
iFrameResize({{checkOrigin:false}},'#odprti-racuni');
</script>
<script>
export default {
  name: 'DonationDohodninaEmbed',
};
</script>
