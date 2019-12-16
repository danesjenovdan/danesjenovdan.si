<template>
  <div class="donation-scale-container">
    <div class="donation-images-container">
      <div
        v-for="image in images"
        :key="image.id"
        :ref="`tooltip_${image.id}`"
        class="donation-image"
      >
        <div class="donation-image-tooltip">
          <img :src="image.image || '/img/avatars/avatar_gift.png'" />
        </div>
        <a :href="image.url" target="_blank">
          <img :src="image.thumbnail || '/img/avatars/avatar_gift.png'" />
        </a>
      </div>
    </div>
    <div class="tehtnica">
      <div class="measure">
        <span class="measure-number">{{ images.length }}</span>
        <span class="measure-unit">{{ unitText }}</span>
      </div>
      <img src="/img/tehtnica2.svg" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'DonationImages',

  props: {
    images: {
      type: Array,
      required: true,
      default: () => [],
    },
  },

  computed: {
    unitText() {
      switch (this.images.length) {
        case 1:
          return 'donator';
        case 2:
          return 'donatorja';
        case 3:
          return 'donatorji';
        case 4:
          return 'donatorji';
        default:
          return 'donatorjev';
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.donation-scale-container {
  .donation-images-container {
    width: 100%;
    display: block;
    text-align: center;
    transform: rotate(180deg);

    .donation-image {
      display: inline-block;
      position: relative;
      // transform: rotate(180deg);

      img {
        transform: rotate(180deg);
        width: 50px;
        height: 50px;
      }

      .donation-image-tooltip {
        display: none;
        position: absolute;
        bottom: -195px;
        left: -75px;
        width: 210px;
        height: 210px;
        z-index: 100;
        overflow: hidden;

        img {
          border: 5px solid #df786c;
          border-radius: 3px;
          width: 200px;
          height: 200px;
        }
      }

      &:hover {
        & > .donation-image-tooltip {
          display: block;
        }
      }
    }
  }
  .tehtnica {
    width: 100%;
    position: relative;

    .measure {
      position: absolute;
      bottom: calc(40% - 45px);
      width: 100%;

      text-transform: uppercase;
      font-style: italic;
      font-weight: 700;
      text-align: center;

      .measure-number {
        font-size: 45px;
        font-weight: 800;
        display: inline-block;
        font-style: normal;
      }

      .measure-unit {
        transform: translate(0, -10px);
        display: inline-block;
        margin-left: 5px;
      }

      @include media-breakpoint-up(sm) {
        bottom: calc(40% - 90px);
        font-size: 30px;

        .measure-number {
          font-size: 90px;
        }

        .measure-unit {
          transform: translate(0, -20px);
        }
      }

      @include media-breakpoint-up(md) {
        bottom: calc(40% - 45px);
        font-size: 16px;

        .measure-number {
          font-size: 45px;
        }

        .measure-unit {
          transform: translate(0, -10px);
        }
      }

      @include media-breakpoint-up(lg) {
        bottom: calc(40% - 90px);
        font-size: 30px;

        .measure-number {
          font-size: 90px;
        }

        .measure-unit {
          transform: translate(0, -20px);
        }
      }
    }

    img {
      width: 100%;
    }
  }
}
</style>
