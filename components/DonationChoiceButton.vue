<template>
  <a class="square-donation-button" :href="href">
    <h1 v-t="`donate.donations.${donationType}.title`"></h1>
    <p v-t="`donate.donations.${donationType}.subtitle`"></p>
    <div :class="['icon', `icon-donation-${donationType}`]"></div>
  </a>
</template>

<script>
export default {
  name: 'DonationChoiceButton',

  props: {
    donationType: {
      type: String,
      default: 'monthly',
    },
    href: {
      type: String,
      default: '#',
      required: true,
    },
  },
};
</script>

<style lang="scss">
@import '../assets/scss/variables';
@import '../assets/scss/icons';

.square-donation-button {
  width: 100%;
  max-width: 317px;
  height: 300px;
  border: 1px solid #df786c;
  position: relative;
  margin: auto;
  margin-top: 20px;
  padding: 16px;
  padding-bottom: 100px;
  transition: background-color 0.6s cubic-bezier(0.215, 0.61, 0.355, 1);
  cursor: pointer;

  h1 {
    color: #333333;
    font-family: $font-family-sans-serif;
    font-size: 33px;
    font-weight: 700;
    font-style: normal;
    letter-spacing: normal;
    line-height: 33.33px;

    &::after {
      content: '';
      display: inline-block;
      position: relative;
      background-image: url('../static/icons/arrow.svg');
      transform: rotate(-90deg);
      width: 22px;
      height: 36px;
      margin-left: 20px;
      top: 8px;

      transition: margin-left 0.6s cubic-bezier(0.215, 0.61, 0.355, 1);
    }
  }

  p {
    color: #333333;
    font-family: $font-family-sans-serif;
    font-size: 27px;
    font-weight: 400;
    font-style: italic;
    letter-spacing: normal;
    line-height: 33.33px;
    text-align: left;
  }

  .icon-donation-monthly {
    background-image: url('../static/icons/donations/veckratna.svg') !important;
    position: absolute;
    bottom: -13px;
    right: 21px;
    width: 99px;
    height: 138px;
  }

  .icon-donation-once {
    background-image: url('../static/icons/donations/enkratna.svg') !important;
    position: absolute;
    bottom: -33px;
    right: -50px;
    width: 241px;
    height: 117px;
  }

  &:hover {
    background-color: rgba(223, 120, 108, 0.6);
    text-decoration: none !important;

    h1::after {
      margin-left: 35px;
    }
  }
}
</style>
