<template>
  <div class="donation-campaign-progress row justify-content-center">
    <div class="col-sm-auto">
      <div class="circle-wrap">
        <div class="circle">
          <div class="mask full">
            <div
              :style="{ transform: `rotate(${firstHalfRotate}deg)` }"
              class="fill"
            ></div>
          </div>
          <div class="mask half">
            <div
              :style="{ transform: `rotate(${secondHalfRotate}deg)` }"
              class="fill"
            ></div>
          </div>
          <div class="inside-circle">{{ daysLeft }}</div>
        </div>
      </div>
    </div>
    <div class="col-sm-auto">
      <p class="countdown-text">dni do izteka kampanje</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DonationCampaignProgress',

  props: {
    endDate: {
      type: Date,
      required: true,
      default() {
        const someDate = new Date();
        someDate.setDate(someDate.getDate() + 10);
        return someDate;
      },
    },
    totalDays: {
      type: Number,
      required: true,
      default: 21,
    },
  },

  computed: {
    daysLeft() {
      const today = new Date();
      const timeinmilisec = this.endDate.getTime() - today.getTime();
      return Math.ceil(timeinmilisec / (1000 * 60 * 60 * 24));
    },

    percentage() {
      return (this.daysLeft / this.totalDays) * 100;
    },

    /* eslint-disable no-unreachable */
    firstHalfRotate() {
      // return 0; // after campaign is over
      if (this.percentage <= 50) {
        return this.percentageToDegrees(this.percentage);
      } else {
        return 180;
      }
    },

    secondHalfRotate() {
      // return 0; // after campaign is over
      if (this.percentage > 50) {
        return this.percentageToDegrees(this.percentage) - 180;
      } else {
        return 0;
      }
    },
    /* eslint-enable no-unreachable */
  },

  methods: {
    percentageToDegrees(percentage) {
      return (percentage / 100) * 360;
    },
  },
};
</script>

<style lang="scss" scoped>
.donation-campaign-progress {
  .circle-wrap {
    margin: 25px auto;
    width: 150px;
    height: 150px;
    background: #e6e2e7;
    border-radius: 50%;
  }

  .circle-wrap .circle .mask,
  .circle-wrap .circle .fill {
    width: 150px;
    height: 150px;
    position: absolute;
    border-radius: 50%;
  }

  .circle-wrap .circle .mask {
    clip: rect(0px, 150px, 150px, 75px);
  }

  .circle-wrap .circle .mask .fill {
    clip: rect(0px, 75px, 150px, 0px);
    // background-image: linear-gradient(
    //   to right,
    //   rgba(205, 172, 84, 1) 0%,
    //   rgba(223, 120, 108, 1) 100%
    // );
    background-color: $secondary;
  }
  .circle-wrap .circle .mask.full,
  .circle-wrap .circle .fill {
    // animation: fill ease-in-out 3s;
    // transform: rotate(126deg);
  }

  .circle-wrap .circle .mask.half {
    transform: rotate(-180deg);
    // TODO calculate appropriate linear gradient
    // .fill {
    //   background-image: linear-gradient(
    //     to left,
    //     rgba(205, 172, 84, 1) 0%,
    //     rgba(223, 120, 108, 1) 100%
    //   );
    // }
  }

  .circle-wrap .inside-circle {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    background: #fff;
    text-align: center;
    margin-top: 15px;
    margin-left: 15px;
    position: absolute;
    z-index: 100;
    font-weight: 400;
    font-size: 90px;
    line-height: 109px;
  }

  .countdown-text {
    height: 120px;
    text-transform: uppercase;
    font-style: italic;
    font-weight: 300;
    font-size: 30px;
    max-width: 300px;
    text-align: center;

    @include media-breakpoint-up(lg) {
      padding-top: 55px;
      text-align: left;
      margin-left: 30px;
    }
  }

  @include media-breakpoint-up(lg) {
    width: 600px;
  }
}
</style>
