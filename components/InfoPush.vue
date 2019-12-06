<template>
  <div :class="['info-push', `info-push--${color}`]">
    <div class="row">
      <div class="col-xl-7">
        <div class="info-push__content">
          <h3 v-if="title" v-text="title" class="info-push__title" />
          <div v-if="text || buttonText || buttonUrl" class="info-push__text">
            <p v-if="text" v-text="text" />
            <more-button
              v-if="buttonText && buttonUrl"
              :to="buttonUrl"
              :text="buttonText"
            />
          </div>
        </div>
      </div>
      <div class="col-xl-5 info-push__image-col">
        <div class="info-push__image">
          <div class="embed-responsive embed-responsive-16by9">
            <div class="embed-responsive-item d-flex align-items-center">
              <div
                :style="{ 'background-image': `url('${image}')` }"
                class="background-image"
              />
            </div>
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
.info-push {
  padding-bottom: 1.8rem;

  .info-push__content {
    position: relative;
    z-index: 1;
    margin-right: 1rem;
    margin-left: -0.5rem;
    justify-content: center;
    padding: 1.2rem 1.2rem 1.5rem;
    background-color: #fff;

    @include media-breakpoint-up(xl) {
      margin-right: -1.8rem;
      margin-left: 0rem;
      padding: 1.8rem 1.8rem 1.8rem;
      padding-right: 2rem + 1.8rem;
      z-index: 2;
    }

    .info-push__title {
      font-size: 2rem;
      font-weight: 600;
      transition: color 0.15s ease;

      @include media-breakpoint-up(xl) {
        font-weight: 700;
        font-size: 2.5rem;
      }
    }

    .info-push__text {
      font-size: 1.1rem;
      font-weight: 200;
      margin-top: 1rem;

      p {
        margin: 0 0 0.5rem;
        font-style: italic;
      }

      .more-button {
        margin-top: 1rem;
      }
    }
  }

  .info-push__image-col {
    $bg-offset: 1.8rem;
    margin-top: -$bg-offset;
    z-index: -1;

    @include media-breakpoint-up(xl) {
      z-index: 1;
      margin-top: 0;
    }

    .info-push__image {
      position: relative;
      z-index: 1;
      display: flex;
      flex-direction: column;
      height: 100%;

      margin-left: 0.5rem;
      margin-right: -0.5rem;

      @include media-breakpoint-up(xl) {
        margin-left: -1.8rem;
        margin-right: 0rem;
        margin-top: 1.8rem;
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
  }
}
</style>
