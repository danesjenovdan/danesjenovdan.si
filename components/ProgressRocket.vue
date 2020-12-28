<template>
  <div class="progress-rocket">
    <div class="progress">
      <div
        class="progress-bar"
        role="progressbar"
        style="width: 75%"
        aria-valuenow="75"
        aria-valuemin="0"
        aria-valuemax="100"
      />
      <i class="icon icon-rocket--secondary" />
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.progress-rocket {
  .progress {
    border-radius: 1rem;
    overflow: visible;

    .progress-bar {
      border-top-left-radius: 1rem;
      border-bottom-left-radius: 1rem;
      background-color: #fff;
      background-image: linear-gradient(
        to right,
        scale-color($color-green, $lightness: 35%) 0%,
        scale-color($color-red, $lightness: 35%) 100%
      );
      z-index: 1;
    }

    .icon {
      flex-shrink: 0;
      width: 3.25rem;
      height: 3rem;
      margin-top: -1rem;
      margin-bottom: 1rem;
      margin-left: -1.3rem;
      opacity: 0.65;
    }
  }
}
</style>
