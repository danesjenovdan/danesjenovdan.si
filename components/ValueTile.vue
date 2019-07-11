<template>
  <div class="value-tile bg-white">
    <div class="row">
      <div class="col-lg-12 col-xxl-6 left-col">
        <div class="d-flex flex-column justify-content-center h-100">
          <div class="d-flex align-items-center flex-column flex-lg-row">
            <div :class="['icon', `icon-${icon}--warning`]" />
            <div class="title d-flex flex-column">
              <h2 v-text="title" />
            </div>
          </div>
        </div>
      </div>
      <div class="col-lg-12 col-xxl-6 right-col">
        <p v-text="description" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    icon: {
      type: String,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
  },
};
</script>


<style lang="scss" scoped>
.value-tile {
  padding: 2.5rem 2rem;
  margin-bottom: 2rem;

  @include media-breakpoint-up(lg) {
    padding: 2.5rem 4rem;
  }

  .left-col,
  .right-col {
    padding: 0;

    @include media-breakpoint-up(lg) {
      padding: 1.5rem 0;
    }
  }

  .left-col {
    border-bottom: 1px solid #686d6e;
    padding-bottom: 1.5rem;

    @include media-breakpoint-up(xxl) {
      border-bottom: none;
      border-right: 1px solid #686d6e;
      padding-right: 2.5rem;
    }

    .icon {
      flex-shrink: 0;
      color: $color-yellow;
      margin-bottom: 2rem;
      width: 100px;
      height: 100px;

      @include media-breakpoint-up(lg) {
        margin-right: 2rem;
        margin-bottom: 0;
      }

      @include media-breakpoint-up(xxl) {
        margin-left: 2rem;
      }

      svg {
        width: 100%;
        height: 100%;
      }
    }

    .title {
      h2 {
        padding: 0 1rem;
        font-size: 2rem;
        font-weight: 600;
        text-align: center;

        @include media-breakpoint-up(lg) {
          text-align: left;
          font-size: 2.5rem;
        }
      }
    }
  }

  .right-col {
    padding-top: 1.5rem;

    @include media-breakpoint-up(xxl) {
      padding-left: 2.5rem;
    }

    /deep/ p {
      font-size: 1.1rem;
      font-weight: 300;
      padding: 0 1rem;

      @include media-breakpoint-up(lg) {
        padding: 0;
      }

      &:last-child {
        margin-bottom: 0;
      }
    }
  }
}
</style>
