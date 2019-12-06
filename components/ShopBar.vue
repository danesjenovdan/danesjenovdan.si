<template>
  <div class="shop-bar bg-white">
    <div class="bar-container">
      <strong v-t="'shop.promo-bar.support-us'" class="my-xl-3" />
      <img
        src="/img/shop-banner.jpg"
        alt="shirts from our shop"
        class="img-fluid d-block d-xl-none"
      />
      <more-button
        :to="localePath('shop')"
        :text="$t('shop.promo-bar.button-text')"
        color="secondary"
        small
      />
    </div>
  </div>
</template>

<script>
import MoreButton from '~/components/MoreButton.vue';

export default {
  components: {
    MoreButton,
  },
};
</script>


<style lang="scss" scoped>
.shop-bar {
  padding: 1rem $content-mobile-padding 1.2rem;
  overflow: hidden;

  @include media-breakpoint-up(xl) {
    padding: 0.75rem 3rem;
    background-image: url('/img/shop-banner.jpg');
    background-position: center;
    background-size: auto 160px;
    background-repeat: no-repeat;
  }

  .bar-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-direction: column;

    @include media-breakpoint-up(xl) {
      flex-direction: row;
    }

    strong {
      text-align: center;
      max-width: 270px;
      margin-bottom: 1rem;

      @include media-breakpoint-up(xl) {
        max-width: initial;
        margin-bottom: 0;
      }
    }

    img {
      width: calc(100% + #{$content-mobile-padding * 2});
      max-width: calc(100% + #{$content-mobile-padding * 2});
      margin: 0 #{-$content-mobile-padding};
    }
  }
}
</style>
