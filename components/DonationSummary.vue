<template>
  <div class="donation-summary">
    <div class="row">
      <div class="col">
        <h1 class="donation-summary-title">ZBRANO ŽE</h1>
        <p class="donation-summary-number">{{ totalDonations }}&nbsp;€</p>
      </div>
      <div class="col">
        <h1 class="donation-summary-title">NAJVIŠJA&nbsp;DONACIJA</h1>
        <p class="donation-summary-number">{{ maxDonation }}&nbsp;€</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DonationSummary',

  props: {
    totalDonations: {
      type: Number,
      required: true,
      default: 0,
    },
    maxDonation: {
      type: Number,
      required: true,
      default: 0,
    },
  },
};
</script>

<style lang="scss" scoped>
.donation-summary {
  text-align: left;
  .donation-summary-title {
    font-size: 16px;
    font-style: italic;
    font-weight: 600;
    margin: 0;
  }
  .donation-summary-number {
    font-size: 50px;
    color: #df786c;
    font-weight: 900;
    line-height: 40px;
    margin-bottom: 30px;

    @include media-breakpoint-up(sm) {
      font-size: 90px;
      line-height: 50px;
    }
  }

  @include media-breakpoint-up(md) {
    .col:first-child::after {
      content: '';
      display: block;
      position: absolute;
      top: 24px;
      right: 0;
      width: 4px;
      height: 60px;
      border-right: 1px solid #333333;
      border-left: 1px solid #333333;
    }
    // .col:last-child::before {
    //   content: '';
    //   display: block;
    //   position: absolute;
    //   top: 20px;
    //   left: 1px;
    //   width: 1px;
    //   height: 50px;
    //   border-right: 1px solid #333333;
    // }
  }
}
</style>
