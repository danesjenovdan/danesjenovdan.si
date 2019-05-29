<template>
  <div :class="['product-tile', `product-tile--${color}`]">
    <div class="row">
      <div class="col-xl-7">
        <div class="product-tile__image">
          <div class="embed-responsive embed-responsive-1by1">
            <div class="embed-responsive-item d-flex align-items-center">
              <div class="background-image" :style="{'background-image': `url('${image}')`}"/>
            </div>
          </div>
        </div>
      </div>
      <div class="col-xl-5 product-tile__content-col">
        <div class="product-tile__content">
          <h3 class="product-tile__title" v-text="title"/>
          <div v-if="text || buttonText || buttonUrl" class="product-tile__text">
            <p v-if="text" v-text="text"/>
            <more-button v-if="buttonText && buttonUrl" color="secondary" :to="buttonUrl" :text="buttonText"/>
          </div>
        </div>
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
      default: null,
    },
    url: {
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
  computed: {
    isExternalUrl() {
      return this.url && /^https?:\/\//.test(this.url);
    },
  },
};
</script>

<style lang="scss" scoped>
.product-tile {
  padding-bottom: 1.8rem;

  .product-tile__image {
    position: relative;
    z-index: 1;
    margin-right: 1rem;
    margin-left: -0.5rem;

    @include media-breakpoint-up(xl) {
      margin-right: -1.8rem;
      margin-left: 0rem;
      z-index: 2;
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
      text-align: center;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: -2;
    }
  }

  .product-tile__content-col {
    $bg-offset: 1.8rem;
    margin-top: -$bg-offset;
    z-index: -1;

    @include media-breakpoint-up(xl) {
      z-index: 1;
      margin-top: 0;
    }

    .product-tile__content {
      position: relative;
      z-index: 1;
      display: flex;
      flex-direction: column;
      height: 100%;
      justify-content: center;
      padding: 0 1.2rem 1.5rem;
      padding-top: $bg-offset + 1.2rem;
      margin-left: 0.5rem;
      margin-right: -0.5rem;
      background-color: #fff;

      @include media-breakpoint-up(xl) {
        margin-left: -1.8rem;
        margin-right: 0rem;
        margin-top: 1.8rem;
        padding: 1.8rem 1.8rem 1.8rem;
        padding-left: 2rem + 1.8rem;
      }

      .product-tile__title {
        font-size: 2.5rem;
        font-weight: 600;
        transition: color 0.15s ease;

        @include media-breakpoint-up(xl) {
          font-weight: 700;
          font-size: 3rem;
        }
      }

      .product-tile__text {
        font-size: 1.25rem;
        font-weight: 200;
        margin-top: 0.5rem;

        p {
          margin: 0 0 0.5rem;
          font-style: italic;
        }

        .more-button {
          margin-top: 1rem;
        }
      }
    }
  }
}
</style>
