<template>
  <div class="row product-tile">
    <div class="col-xl-6">
      <div class="product-tile__image">
        <div class="embed-responsive embed-responsive-1by1">
          <div class="embed-responsive-item d-flex align-items-center">
            <div
              :style="{ 'background-image': `url('${image}')` }"
              class="background-image"
            />
          </div>
        </div>
      </div>
    </div>
    <div class="col-xl-6 product-tile__title-col">
      <div class="product-tile__title">
        <h2>{{ title }}</h2>
      </div>
    </div>
    <div class="col-xl-9 offset-xl-1">
      <div class="product-tile__content">
        <p class="product-tile__text" v-text="text" />
        <more-button :to="buttonUrl" :text="buttonText" color="secondary" />
      </div>
    </div>
  </div>
</template>

<script>
import MoreButton from '~/components/MoreButton.vue';

export default {
  components: {
    MoreButton,
  },
  props: {
    color: {
      type: String,
      default: 'primary',
    },
    image: {
      type: String,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    text: {
      type: String,
      required: true,
    },
    buttonText: {
      type: String,
      default: null,
    },
    buttonUrl: {
      type: String,
      default: null,
    },
  },
};
</script>

<style lang="scss" scoped>
.product-tile {
  .product-tile__image {
    position: relative;
    z-index: 1;
    margin-right: 1rem;
    margin-left: -0.5rem;

    @include media-breakpoint-up(xl) {
      margin-right: 0rem;
      margin-left: 0rem;
    }

    .background-image {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-size: cover;
      background-repeat: no-repeat;
      background-position: center;
    }
  }

  .product-tile__title,
  .product-tile__content {
    margin-left: 0.5rem;
    margin-right: -0.5rem;
    background-color: #fff;

    @include media-breakpoint-up(xl) {
      margin-left: 0rem;
      margin-right: 0rem;
      background-color: transparent;
    }
  }

  .product-tile__title-col {
    $bg-offset: 4.5rem;
    margin-top: -$bg-offset + 1rem;
    z-index: -1;

    @include media-breakpoint-up(xl) {
      margin-top: 0;
      z-index: 1;
    }

    .product-tile__title {
      position: relative;
      z-index: 1;
      display: flex;
      flex-direction: column;
      height: 100%;
      justify-content: center;
      padding: 0 1.2rem 0.75rem 1.75rem;
      padding-top: $bg-offset;

      @include media-breakpoint-up(xl) {
        padding-top: $bg-offset / 2;
        padding-left: 0.5rem;
      }

      h2 {
        font-size: 2.5rem;
        font-weight: 600;

        @include media-breakpoint-up(xxl) {
          font-size: 3rem;
        }
      }
    }
  }

  .product-tile__content {
    padding: 0 1.2rem 1.5rem 1.75rem;

    @include media-breakpoint-up(xl) {
      padding-left: 2rem;
      padding-right: 2rem;
      background-color: #fff;

      $bg-offset: 50%;
      margin-top: -$bg-offset;
      padding-top: calc(2rem + #{$bg-offset});
    }

    p {
      font-size: 1.2rem;
      font-style: italic;
      line-height: 1.25;
      font-weight: 200;
      margin: 0;

      @include media-breakpoint-up(xl) {
        font-size: 1.5rem;
      }
    }

    .more-button {
      margin-top: 1.5rem;

      @include media-breakpoint-up(xl) {
        margin-top: 2rem;
      }
    }
  }
}
</style>
