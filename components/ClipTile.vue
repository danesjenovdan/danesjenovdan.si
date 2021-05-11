<template>
  <div class="clip-tile">
    <dynamic-link :to="clip.url" class="clip-tile__link">
      <div class="clip-tile__image-container">
        <div class="embed-responsive embed-responsive-1200by630">
          <div class="embed-responsive-item d-flex align-items-center">
            <div
              :title="clip.alt"
              :style="{ 'background-image': `url('${clip.image}')` }"
              class="clip-tile__image"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="30 18 40 64"
                fill="currentColor"
              >
                <path
                  d="M50.005 82c.715-.028 1.542-.322 2.063-.812l17-16c.975-1.085 1.377-3.164.25-4.375-1.109-1.194-3.26-1.159-4.375.03l-11.938 11.25V21a3 3 0 0 0-6 0v51.094l-11.938-11.25c-1.025-1.024-3.253-1.213-4.375-.031-1.122 1.181-.764 3.335.25 4.375l17 16a2.885 2.885 0 0 0 2.063.812z"
                />
              </svg>
            </div>
          </div>
        </div>
      </div>
      <div class="clip-tile__content">
        <div class="clip-tile__info-container">
          <div class="clip-tile__icon">
            <div
              v-for="format in clip.formats"
              :key="format"
              :class="['icon', `icon-clip-${format}`]"
            />
          </div>
          <div class="clip-tile__info">
            {{ clip.publisher }}
            <span class="info-divider">/</span>
            {{ toSloDate(clip.date) }}
            <span class="info-divider">/</span>
            {{ types.join(', ') }}
          </div>
        </div>
        <h2 class="clip-tile__title" v-text="clip.title" />
        <div class="clip-tile__text">
          <p v-text="clip.desc" />
        </div>
      </div>
    </dynamic-link>
  </div>
</template>

<script>
import DynamicLink from '~/components/DynamicLink.vue';
import dateMixin from '~/mixins/date.js';

export default {
  components: {
    DynamicLink,
  },
  mixins: [dateMixin],
  props: {
    clip: {
      type: Object,
      required: true,
    },
  },
  computed: {
    types() {
      return (this.clip.types || []).map((type) =>
        this.$te(`clipping.tags.type.${type}`)
          ? this.$t(`clipping.tags.type.${type}`)
          : type,
      );
    },
  },
};
</script>

<style lang="scss" scoped>
.clip-tile {
  width: 100%;

  @include media-breakpoint-up(xl) {
    margin-bottom: 3rem;
  }

  .clip-tile__link {
    text-decoration: none;
    color: inherit;

    @include media-breakpoint-up(xl) {
      display: flex;
    }

    &:hover {
      .clip-tile__image-container {
        .clip-tile__image {
          &::before {
            opacity: 0.8;
          }

          svg {
            opacity: 1;
          }
        }
      }

      .clip-tile__title {
        color: $color-yellow;
      }
    }

    .clip-tile__image-container {
      @include media-breakpoint-up(xl) {
        flex: 1.25;
      }

      .clip-tile__image {
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
        background-color: #fff;

        &::before {
          content: '';
          width: 100%;
          height: 100%;
          position: absolute;
          top: 0;
          left: 0;
          background-color: $color-yellow;
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

    .clip-tile__content {
      padding: 1.25rem 0;

      @include media-breakpoint-up(xl) {
        flex: 2;
        padding: 0 0 0 2rem;
      }

      .clip-tile__info-container {
        display: flex;
        align-items: center;
        margin-bottom: 0.5rem;

        @include media-breakpoint-up(xl) {
          flex-direction: column;
          align-items: initial;
          justify-content: center;
        }

        .clip-tile__icon {
          display: flex;
          margin: 0 -0.25rem;

          .icon {
            width: 1.5rem;
            height: 2rem;
            margin: 0 0.25rem;
          }
        }

        .clip-tile__info {
          font-size: 0.85rem;
          font-weight: 400;
          font-style: italic;
          line-height: 1.2;
          margin-left: 0.75rem;

          @include media-breakpoint-up(xl) {
            margin-left: 0;
            margin-top: 0.75rem;
          }

          .info-divider {
            display: inline-block;
            margin: 0 0.3rem;
          }
        }
      }

      .clip-tile__title {
        font-size: 1.5rem;
        font-weight: 700;
        // margin-bottom: 1rem;
        transition: color 0.15s ease;
      }

      .clip-tile__text {
        font-size: 1.15rem;
        font-weight: 300;
        margin-top: 0.75rem;

        p {
          margin: 0 0 0.5rem;
        }
      }
    }
  }
}
</style>
