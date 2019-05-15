<template>
  <div :class="['preview-tile', `preview-tile--${color}`]">
    <a href="#" target="_blank" class="preview-tile__link">
      <div class="embed-responsive embed-responsive-1200by630">
        <div class="embed-responsive-item d-flex align-items-center">
          <div
            class="preview-tile__image"
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
      <div class="preview-tile__content">
        <h3 class="preview-tile__title" v-text="title"/>
        <div v-if="byline" class="preview-tile__byline">
          <i v-text="byline"/>
        </div>
        <div v-if="text" class="preview-tile__text">
          <p v-text="text"/>
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
  },
};
</script>

<style lang="scss" scoped>
.preview-tile {
  .preview-tile__link {
    text-decoration: none;
    color: #333;

    &:hover {
      .preview-tile__image {
        &::before {
          opacity: 0.8;
        }

        svg {
          opacity: 1;
        }
      }

      .preview-tile__title {
        color: $color-green;
      }
    }

    .preview-tile__image {
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

    .preview-tile__content {
      padding: 1.5rem 0;

      .preview-tile__title {
        font-size: 1.5rem;
        font-weight: 700;
        // margin-bottom: 1rem;
        transition: color 0.15s ease;
      }

      .preview-tile__byline {
        font-weight: 200;
      }

      .preview-tile__text {
        font-size: 1.15rem;
        font-weight: 200;
        margin-top: 1rem;

        p {
          margin: 0 0 0.5rem;
        }
      }
    }
  }

  @each $color-name, $color in $theme-colors {
    &--#{$color-name} {
      .preview-tile__link {
        &:hover {
          .preview-tile__title {
            color: $color;
          }
        }

        .preview-tile__image {
          &::before {
            background-color: $color;
          }
        }
      }
    }
  }
}
</style>
