<template>
  <div>
    <header class="row pb-0">
      <div class="col-12">
        <h1>{{ $t('error.title') }}</h1>
        <hr class="border-primary mb-0" />
      </div>
    </header>
    <div class="row">
      <div class="col-lg-6">
        <p>
          {{ $t('error.text') }}
        </p>
        <more-button to="/" :text="$t('error.button')" color="primary" />
      </div>
      <div class="col-lg-6 mt-5 mt-lg-0">
        <img src="/img/404.svg" alt="" />
      </div>
    </div>
  </div>
</template>

<script>
import MoreButton from '~/components/MoreButton.vue';

//                                                                            //
//             WARNING: this is treated as a page, not a layout!              //
//                                                                            //

export default {
  components: {
    MoreButton,
  },
  layout: 'default',
  props: {
    error: {
      type: Object,
      default: () => ({}),
    },
  },
};
</script>

<style lang="scss" scoped>
header {
  padding: 1.2rem 0 0.5rem;

  @include media-breakpoint-up(md) {
    padding: 3rem 0 2rem;
  }

  @include media-breakpoint-up(xl) {
    padding: 5rem 0 2rem;
  }

  h1 {
    font-size: 2.5rem;
    font-weight: 200;
    letter-spacing: 0.8px;

    @include media-breakpoint-up(xl) {
      font-size: 3.5rem;
      letter-spacing: 1.2px;
    }
  }

  hr {
    border-top-width: 18px;
    border-top-color: $color-red;
    max-width: 450px;
    margin-left: 0;
  }
}

p {
  // max-width: 630px;
  font-size: 1.5rem;
  font-weight: 300;
  font-style: italic;
  line-height: 1.2;
  margin-top: 3rem;
  margin-bottom: 1rem;

  @include media-breakpoint-up(xl) {
    margin-bottom: 3rem;
  }
}
</style>
