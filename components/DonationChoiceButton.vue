<template>
  <div class="square-donation-button">
    <h1>Mesečno</h1>
    <p>Some words, ker imaš veliko plačo.</p>
    <div class="icon icon-donation-monthly"></div>
  </div>
</template>

<script>
export default {
  name: 'DonationChoiceButton',
};
</script>

<style lang="scss">
@import '../assets/scss/variables';
@import '../assets/scss/icons';

.square-donation-button {
  width: 100%;
  max-width: 634px;
  border: 3px solid #df786c;
  position: relative;

  h1 {
    color: #333333;
    font-family: $font-family-sans-serif;
    font-size: 67px;
    font-weight: 700;
    font-style: normal;
    letter-spacing: normal;
    line-height: 66.67px;
  }

  .icon-donation-monthly {
    background-image: url('../static/icons/donations/veckratna.svg') !important;
    position: absolute;
    bottom: -10px;
    right: 41px;
    width: 197px;
    height: 277px;
  }
}
</style>
