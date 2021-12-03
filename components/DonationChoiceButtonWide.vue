<template>
  <a class="wide-donation-button" :href="href" target="_blank">
    <div class="icon-wrapper">
      <div :class="['icon', `icon-donation-${donationType}`]"></div>
    </div>
    <div class="text-wrapper">
      <h1 v-t="`donate.donations.${donationType}.title`"></h1>
      <p v-t="`donate.donations.${donationType}.subtitle`"></p>
    </div>
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

  computed: {
    iconSrc() {
      if (this.donationType === 'once')
        return require('../static/icons/donations/enkratna.svg');
      if (this.donationType === 'monthly')
        return require('../static/icons/donations/veckratna.svg');
      if (this.donationType === 'tax-return')
        return require('../static/icons/donations/en-procent.svg');
      return '';
    },
  },
};
</script>

<style lang="scss">
@import '../assets/scss/variables';
@import '../assets/scss/icons';

.wide-donation-button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  border: 1px solid #df786c;
  position: relative;
  margin-top: 20px;
  margin-bottom: 20px;
  padding: 24px 16px;
  transition: background-color 0.6s cubic-bezier(0.215, 0.61, 0.355, 1);
  cursor: pointer;

  .text-wrapper {
    margin-right: 15px;
    margin-left: 30px;
  }

  h1 {
    color: #333333;
    font-family: $font-family-sans-serif;
    font-size: 33px;
    font-weight: 700;
    font-style: normal;
    letter-spacing: normal;
    line-height: 33.33px;

    @include media-breakpoint-down(sm) {
      font-size: 24px;
    }

    // &::after {
    //   content: '';
    //   display: inline-block;
    //   position: relative;
    //   background-image: url('../static/icons/arrow.svg');
    //   transform: rotate(-90deg);
    //   width: 22px;
    //   height: 36px;
    //   margin-left: 20px;
    //   top: 8px;
    //   transition: margin-left 0.6s cubic-bezier(0.215, 0.61, 0.355, 1);
    // }
  }

  p {
    color: #333333;
    font-family: $font-family-sans-serif;
    font-size: 20px;
    font-weight: 400;
    font-style: italic;
    letter-spacing: normal;
    line-height: 24px;
    text-align: left;
  }

  .icon-wrapper {
    min-width: 150px;
    display: flex;
    justify-content: center;
    align-items: center;

    @include media-breakpoint-down(sm) {
      min-width: 100px;
    }
  }

  .icon-donation-monthly {
    background-image: url('../static/icons/donations/veckratna.svg') !important;
    // position: absolute;
    bottom: -13px;
    right: 21px;
    width: 77px;
    height: 93px;
    @include media-breakpoint-down(sm) {
      height: 80px;
    }
  }

  .icon-donation-once {
    background-image: url('../static/icons/donations/enkratna.svg') !important;
    // position: absolute;
    bottom: -33px;
    right: 20px;
    width: 150px;
    height: 93px;
    transform: rotate(15deg);
    @include media-breakpoint-down(sm) {
      height: 64px;
    }
  }

  .icon-donation-tax-return {
    background-image: url('../static/icons/donations/en-procent.svg') !important;
    // position: absolute;
    bottom: -13px;
    right: 21px;
    width: 99px;
    height: 93px;
    @include media-breakpoint-down(sm) {
      height: 80px;
    }
  }

  &:hover {
    background-color: rgba(223, 120, 108, 0.6);
    text-decoration: none !important;

    &::after {
      left: 20px;
    }
  }
}

.wide-donation-button::after {
  content: '';
  display: inline-block;
  position: relative;
  background-image: url('../static/icons/arrow.svg');
  background-repeat: no-repeat;
  transform: rotate(-90deg);
  width: 22px;
  height: 36px;
  left: 10px;
  top: 8px;
  margin-right: 20px;
  transition: left 0.6s cubic-bezier(0.215, 0.61, 0.355, 1);
}
</style>
