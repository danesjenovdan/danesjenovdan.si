<template>
  <div :class="['promoted-tile', `promoted-tile--${color}`]">
    <a :href="url" target="_blank" rel="noopener noreferrer" class="promoted-tile__link">
      <div class="row">
        <div class="col-xl-7">
          <div class="promoted-tile__image">
            <div class="embed-responsive embed-responsive-1200by630">
              <div class="embed-responsive-item d-flex align-items-center">
                <div
                  class="background-image"
                  :style="{'background-image': `url('${image}')`}"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="30 18 40 64"
                    fill="currentColor"
                  >
                    <path
                      d="M50.005 82c.715-.028 1.542-.322 2.063-.812l17-16c.975-1.085 1.377-3.164.25-4.375-1.109-1.194-3.26-1.159-4.375.03l-11.938 11.25V21a3 3 0 0 0-6 0v51.094l-11.938-11.25c-1.025-1.024-3.253-1.213-4.375-.031-1.122 1.181-.764 3.335.25 4.375l17 16a2.885 2.885 0 0 0 2.063.812z"
                    ></path>
                  </svg>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-xl-5 promoted-tile__content-col">
          <div class="promoted-tile__content">
            <h3 class="promoted-tile__title" v-text="title"/>
            <div v-if="byline" class="promoted-tile__byline">
              <i v-text="byline"/>
            </div>
            <div v-if="text" class="promoted-tile__text">
              <p v-text="text"/>
            </div>
          </div>
        </div>
      </div>
    </a>
  </div>
</template>

<script>
export default {
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
    byline: {
      type: String,
      default: null,
    },
    text: {
      type: String,
      default: null,
    },
    url: {
      type: String,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.promoted-tile {
  .promoted-tile__link {
    text-decoration: none;
    color: inherit;
    overflow: hidden;
    display: block;
    padding-bottom: 1.8rem;

    &:hover {
      .promoted-tile__image {
        .background-image {
          &::before {
            opacity: 0.8;
          }

          svg {
            opacity: 1;
          }
        }
      }

      .promoted-tile__title {
        color: $color-green;
      }
    }

    .promoted-tile__image {
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

        &::before {
          content: '';
          width: 100%;
          height: 100%;
          position: absolute;
          top: 0;
          left: 0;
          background-color: $color-green;
        }

        &::before,
        svg {
          opacity: 0;
          transition: opacity 0.15s ease;
        }

        svg {
          width: 3rem;
          height: 3rem;
          position: relative;
          color: #fff;
          transform: rotate(-90deg);
        }
      }
    }

    .promoted-tile__content-col {
      $bg-offset: 1.8rem;
      margin-top: -$bg-offset;
      z-index: -1;

      @include media-breakpoint-up(xl) {
        z-index: 1;
        margin-top: 0;
      }

      .promoted-tile__content {
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
          // padding-top: 2rem;
          // padding-bottom: 2rem;
        }

        .promoted-tile__title {
          font-size: 2.5rem;
          font-weight: 600;
          transition: color 0.15s ease;

          @include media-breakpoint-up(xl) {
            font-weight: 700;
            font-size: 3rem;
          }
        }

        .promoted-tile__byline {
          font-weight: 200;
        }

        .promoted-tile__text {
          font-size: 1.15rem;
          font-weight: 200;
          margin-top: 1rem;

          p {
            margin: 0 0 0.5rem;
          }
        }
      }
    }
  }

  @each $color-name, $color in $theme-colors {
    &--#{$color-name} {
      .promoted-tile__link {
        &:hover {
          .promoted-tile__title {
            color: $color;
          }
        }

        .promoted-tile__image {
          .background-image {
            &::before {
              background-color: $color;
            }
          }
        }
      }
    }
  }
}
</style>
