<template>
  <div class="agrument-subscribe-bar bg-white">
    <div class="d-flex justify-content-center">
      <form class="form-inline">
        <strong v-t="'agrument.subscribe-bar.subscribe-to'" class="my-2 mr-2"/>
        <span v-t="'agrument.subscribe-bar.deliver-it'"/>
        <div class="form-group my-2 mr-3 mx-md-3">
          <input
            id="subscribe-email"
            type="email"
            class="form-control"
            :placeholder="$t('agrument.subscribe-bar.email-address')"
          >
        </div>

        <button type="submit" class="btn btn-primary my-2 px-3">
          <span v-t="'agrument.subscribe-bar.subscribe-action'"/>
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.agrument-subscribe-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 100;
  padding: 0 $content-mobile-padding;
  box-shadow: $box-shadow-lg;

  @include media-breakpoint-up(md) {
    left: $side-menu-width;
  }

  strong {
    font-weight: 600;
  }

  .form-control {
    min-width: 220px;
  }

  button {
    text-transform: uppercase;
    font-weight: 600;
  }
}
</style>
