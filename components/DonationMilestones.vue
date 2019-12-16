<template>
  <div class="donation-milestones-container">
    <h1>Več nas je kot</h1>
    <div
      v-for="milestone in reachedMilestones"
      :key="milestone.icon"
      class="donation-milestone"
    >
      <div
        class="donation-milestone-number"
        :style="{
          'margin-left': `-${30 * milestone.number.toString().length}px`,
        }"
      >
        {{ milestone.number }}
      </div>
      <div class="donation-milestone-text">
        {{ milestone.text }}
      </div>
      <div
        :style="{
          'background-image': `url(/img/milestones/${milestone.icon}.svg)`,
        }"
        class="donation-milestone-icon"
      ></div>
    </div>
    <div class="donation-milestone donation-milestone--locked">
      <div
        class="donation-milestone-number"
        :style="{
          'margin-left': `-${30 * nextMilestone.number.toString().length}px`,
        }"
      >
        {{ nextMilestone.number }}
      </div>
      <div
        :style="{
          'background-image': `url(/img/milestones/lock.svg)`,
        }"
        class="donation-milestone-icon"
      ></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DonationMilestones',

  props: {
    numberOfDonations: {
      type: Number,
      required: true,
      default: 1200,
    },
  },

  data() {
    return {
      milestones: [
        {
          number: 10,
          text: 'število ljudi potrebnih za vzpostavitev verske skupnosti',
          icon: '1_verskaskupnost',
        },
        {
          number: 26,
          text:
            'znanih Slovencev, ki je oktobra 2011 podprlo Jankovićevo kandidaturo na parlamentarnih volitvah',
          icon: '2_jankovic',
        },
        {
          number: 50,
          text: 'članov štajerske varde',
          icon: '3_varda',
        },
        {
          number: 70,
          text: 'ustanovnih delničarjev podjetja NOVATV24',
          icon: '4_nova24',
        },
        {
          number: 99,
          text: 'članov skupščine GZS',
          icon: '5_gzs',
        },
        {
          number: 134,
          text: 'ljudi, ki imajo vsaj 3 stanovanja na Airbnb v Ljubljani',
          icon: '6_lastniki',
        },
      ],
    };
  },

  computed: {
    reachedMilestones() {
      return this.milestones.filter((m) => m.number < this.numberOfDonations);
    },
    nextMilestone() {
      const potentialNextMilestone = this.milestones
        .filter((m) => m.number > this.numberOfDonations)
        .sort((a, b) => a.number - b.number);

      return potentialNextMilestone.length > 0
        ? potentialNextMilestone[0]
        : { number: '?' };
    },
  },
};
</script>

<style lang="scss" scoped>
.donation-milestones-container {
  padding: 30px;

  h1 {
    font-size: 60px;
    color: rgba(223, 120, 108, 0.98);
    font-weight: 700;
    font-style: italic;
    text-shadow: -1px 1px 0 #333333, 1px 1px 0 #333333, 1px -1px 0 #333333,
      -1px -1px 0 #333333;
    margin-top: -90px;
  }

  .donation-milestone {
    background-color: #ffffff;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
    padding-left: 20px;

    .donation-milestone-number {
      font-size: 80px;
      line-height: 150px;
      font-weight: 800;
    }

    .donation-milestone-text {
      font-size: 12px;
      font-style: italic;
      font-weight: 600;
      padding-left: 30px;
      padding-right: 30px;
      max-width: 400px;

      @include media-breakpoint-up(md) {
        font-size: 16px;
      }
    }

    .donation-milestone-icon {
      width: 60px;
      height: 60px;
      background-position: center;
      background-size: contain;
      background-repeat: no-repeat;
      flex-shrink: 0;
      margin-right: 20px;

      @include media-breakpoint-up(md) {
        width: 115px;
        height: 115px;
      }
    }
  }
  .donation-milestone--locked {
    background-color: rgba(255, 255, 255, 0.5);

    .donation-milestone-number {
      opacity: 0.5;
    }

    .donation-milestone-icon {
      margin-right: calc(50% - 57px);
    }
  }
}
</style>
