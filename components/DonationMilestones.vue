<template>
  <div class="donation-milestones-container">
    <h1>Nas je že več kot</h1>
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
          'background-image': `url(/icons/mejniki/${milestone.icon}.svg)`,
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
          number: 5,
          text:
            'slovenskih EU poslancev, ki so glasovali za Direktivo o avtorski pravici na digitalnem enotnem trgu.',
          icon: '1_euposlanci',
        },
        {
          number: 10,
          text:
            'mednarodnih voditeljev (vključujoč Janšo), ki so podprli Trumpovo kandidaturo.',
          icon: '2_trump',
        },
        {
          number: 14,
          text:
            'poslancev DeSUS in SMC, ki so podprli Janeza Janšo za predsednika vlade',
          icon: '3_jansa',
        },
        {
          number: 32,
          text:
            'rumenih jopičev na antiproslavi ob letošnjem dnevu državnosti.',
          icon: '4_rumenijopici',
        },
        {
          number: 48,
          text:
            'poslancev, ki so glasovali za 780-milijonsko investicijo v vojsko.',
          icon: '5_vojska',
        },
        {
          number: 71,
          text: 'lobistov, ki so obiskali Toninovo Ministrstvo za obrambo.',
          icon: '6_lobisti',
        },
      ],
    };
  },

  computed: {
    reachedMilestones() {
      return this.milestones.filter((m) => m.number <= this.numberOfDonations);
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
  padding-left: 15px;

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
      width: 100%;
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
