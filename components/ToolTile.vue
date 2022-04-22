<template>
  <div class="tool-tile bg-white">
    <div class="row">
      <div :class="['left-col', { open }]">
        <div class="d-flex flex-column justify-content-center h-100">
          <div class="d-flex align-items-center flex-column flex-lg-row">
            <div
              v-if="icon"
              :aria-label="alt"
              :style="{ 'background-image': `url(/icons/tools/${icon}.svg)` }"
              class="icon"
            />
            <div class="title d-flex flex-column">
              <h2 v-text="title" />
              <h3 v-text="description" />
            </div>
          </div>
          <div class="d-none d-xxl-flex">
            <div class="icon" />
            <div class="links">
              <ul v-if="links.length">
                <li v-for="link in links" :key="link.url">
                  <a :href="link.url" target="_blank">{{
                    $t(`tools.tools.${icon}.links.${link.tag}`)
                  }}</a>
                </li>
              </ul>
              <ul
                v-if="
                  email && email.address && email.address.indexOf('@') !== -1
                "
                class="contact"
              >
                <li>
                  <a :href="`mailto:${email.address}`" target="_blank">
                    {{ email.label }}
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="open-arrow-container">
        <button
          :class="['btn', 'btn-warning', 'open-arrow', { open }]"
          @click="open = true"
        />
      </div>
      <div :class="['right-col', { open }]">
        <p
          v-for="paragraph in paragraphs"
          :key="paragraph"
          v-text="paragraph"
        />
        <div class="d-flex flex-column d-xxl-none">
          <div v-if="links.length" class="links">
            <ul>
              <li v-for="link in links" :key="link.url">
                <a :href="link.url" target="_blank">{{
                  $t(`tools.tools.${icon}.links.${link.tag}`)
                }}</a>
              </li>
            </ul>
          </div>
          <div
            v-if="email && email.address && email.address.indexOf('@') !== -1"
            class="links contact"
          >
            <ul>
              <li>
                <a :href="`mailto:${email.address}`" target="_blank">
                  {{ email.label }}
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ToolTile',
  props: {
    title: {
      type: String,
      required: true,
    },
    alt: {
      type: String,
      default: null,
    },
    description: {
      type: String,
      required: true,
    },
    paragraphs: {
      type: Array,
      required: true,
    },
    links: {
      type: Array,
      default: () => [],
    },
    email: {
      type: Object,
      default: null,
    },
    icon: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      open: false,
    };
  },
};
</script>

<style lang="scss" scoped>
.tool-tile {
  padding: 2.5rem 2rem;
  margin-bottom: 2rem;
  position: relative;

  @include media-breakpoint-up(lg) {
    padding: 2.5rem 4rem;
  }

  .left-col,
  .right-col {
    flex: 1 1 100%;
    max-width: initial;
    padding: 0;

    @include media-breakpoint-up(lg) {
      padding: 1.5rem 0;
    }

    @include media-breakpoint-up(xxl) {
      flex-basis: 0%;
    }
  }

  .left-col {
    flex-grow: 1.25;
    padding-bottom: 3.5rem;

    &.open {
      padding-bottom: 0rem;
    }

    @include media-breakpoint-up(lg) {
      padding-bottom: 0;
    }

    @include media-breakpoint-up(xxl) {
      padding-bottom: 1.5rem !important;
      border-right: 1px solid #686d6e;
      padding-right: 2.5rem;
    }

    .icon {
      flex-shrink: 0;
      color: $color-yellow;
      margin-bottom: 1.25rem;
      width: 100px;
      height: 100px;

      @include media-breakpoint-up(lg) {
        margin-right: 2rem;
        margin-bottom: 0;
      }

      @include media-breakpoint-up(xxl) {
        margin-left: 2rem;
      }
    }

    .title {
      h2,
      h3 {
        padding: 0 1rem;
      }

      h2 {
        font-size: 2rem;
        font-weight: 600;
        text-align: center;

        @include media-breakpoint-up(lg) {
          font-size: 3.5rem;
          text-align: left;
        }
      }

      h3 {
        font-size: 1.2rem;
        font-weight: 300;
        font-style: italic;
        text-align: center;

        @include media-breakpoint-up(lg) {
          font-size: 1.5rem;
          text-align: left;
        }
      }
    }

    .links {
      padding: 0 1rem;
    }
  }

  .open-arrow-container {
    width: 100%;
    position: absolute;
    left: 0;
    bottom: 0;
    display: flex;
    justify-content: center;

    .open-arrow {
      display: block;
      width: 64px;
      height: 64px;
      border: none;
      background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 38 62" fill="%23fff"><path d="M19 62c.463 0 1.077-.28 1.376-.564l17-16c.772-.747.862-1.957.078-2.828-.7-.778-2.067-.798-2.828-.078L21 55.374V2a2 2 0 1 0-4 0v53.374L3.375 42.53c-.76-.72-2.094-.669-2.828.078-.775.789-.706 2.093.078 2.828l17 16c.46.47.905.556 1.375.564z"/></svg>');
      background-repeat: no-repeat;
      background-position: center;
      background-size: 50% 50%;

      @include media-breakpoint-up(lg) {
        display: none;
      }

      &.open {
        display: none;
      }
    }
  }

  .right-col {
    padding-top: 1.5rem;
    display: none;

    &.open {
      display: block;
    }

    @include media-breakpoint-up(lg) {
      display: block;
    }

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

  .links {
    margin-top: 1rem;
    padding: 2rem 1rem 0 1rem;
    border-top: 1px solid #686d6e;
    width: 100%;

    @include media-breakpoint-up(xxl) {
      padding: 0;
      border-top: none;
    }

    ul {
      list-style: none;
      margin: 0;
      padding: 0;
      display: flex;
      flex-wrap: wrap;
      line-height: 1.2;

      li {
        flex-basis: 100%;
        margin-bottom: 0.75rem;

        @include media-breakpoint-up(sm) {
          flex-basis: 50%;
        }

        @include media-breakpoint-up(xl) {
          flex-basis: 33%;
        }

        @include media-breakpoint-up(xxl) {
          flex-basis: 50%;
        }

        a {
          color: inherit;
          text-decoration: underline;
          font-style: italic;
          display: block;
          position: relative;
          padding-left: 1.75rem;

          &:hover {
            text-decoration: none;
          }

          &::before {
            content: '';
            display: block;
            width: 1.7rem;
            height: calc(1em * 1.2); // font size * line height
            background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path d="M89.333 30.938l-20.271-20.27a5.54 5.54 0 0 0-3.892-1.613 5.553 5.553 0 0 0-3.886 1.613L41.958 29.995a5.455 5.455 0 0 0-1.612 3.889 5.458 5.458 0 0 0 1.611 3.89 5.46 5.46 0 0 0 3.889 1.611c1.47 0 2.851-.572 3.888-1.611l15.439-15.439 12.493 12.492-15.438 15.439c-1.039 1.039-1.611 2.42-1.611 3.89s.572 2.851 1.61 3.887a5.462 5.462 0 0 0 3.89 1.614h.003a5.472 5.472 0 0 0 3.886-1.613l19.328-19.326a5.508 5.508 0 0 0-.001-7.78zm-2.121 5.658L67.883 55.923c-.938.942-2.585.95-3.535-.002a2.478 2.478 0 0 1-.731-1.766c0-.668.26-1.296.732-1.769l16.499-16.5a1.5 1.5 0 0 0 0-2.122L66.233 19.152c-.293-.293-.677-.439-1.061-.439s-.768.146-1.061.439l-16.5 16.501c-.942.944-2.588.944-3.534-.002a2.483 2.483 0 0 1-.731-1.768c0-.667.26-1.295.732-1.767l19.327-19.328c.933-.931 2.603-.933 3.535 0l20.271 20.27c.976.975.976 2.562.001 3.538zM54.155 60.615a5.455 5.455 0 0 0-3.889 1.611l-15.439 15.44-12.493-12.492 15.438-15.438a5.457 5.457 0 0 0 1.612-3.889 5.465 5.465 0 0 0-1.61-3.89c-1.038-1.039-2.42-1.611-3.89-1.611s-2.852.572-3.889 1.611L10.667 61.285a5.464 5.464 0 0 0-1.611 3.889c0 1.47.573 2.851 1.612 3.889l20.269 20.269a5.474 5.474 0 0 0 3.888 1.614h.006a5.462 5.462 0 0 0 3.886-1.613l19.327-19.327a5.454 5.454 0 0 0 1.611-3.89c0-1.469-.572-2.85-1.61-3.888a5.46 5.46 0 0 0-3.89-1.613zm1.768 7.268l-19.33 19.33a2.499 2.499 0 0 1-3.535-.002L12.788 66.94c-.465-.465-.732-1.109-.732-1.767s.267-1.302.732-1.768l19.329-19.329c.471-.472 1.099-.731 1.767-.731s1.296.26 1.769.732c.472.473.731 1.101.731 1.769 0 .667-.26 1.295-.732 1.767l-16.499 16.5a1.5 1.5 0 0 0 0 2.122l14.614 14.613a1.5 1.5 0 0 0 2.121 0l16.501-16.501c.941-.942 2.589-.944 3.533.001.473.473.732 1.101.733 1.769 0 .667-.259 1.294-.732 1.766zm-26.979-2.327c0 1.469.571 2.851 1.61 3.89s2.42 1.611 3.89 1.611c1.469 0 2.85-.572 3.889-1.611l31.11-31.112c1.04-1.038 1.612-2.42 1.612-3.89s-.572-2.852-1.61-3.888a5.46 5.46 0 0 0-3.89-1.612 5.462 5.462 0 0 0-3.889 1.611l-31.11 31.112a5.461 5.461 0 0 0-1.612 3.889zm3.733-1.767l31.111-31.113c.473-.473 1.1-.732 1.768-.732s1.296.26 1.769.733c.472.471.731 1.099.731 1.767s-.26 1.296-.732 1.768L36.212 67.324c-.946.946-2.592.944-3.536 0a2.483 2.483 0 0 1-.731-1.769 2.476 2.476 0 0 1 .732-1.766z"/></svg>');
            background-repeat: no-repeat;
            background-size: contain;
            background-position: left center;
            position: absolute;
            top: 0;
            left: 0;
          }

          &[href^='https:\/\/github.com']::before {
            background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="1363.2 -4345.45 325.79 317.749"><path d="M1526.08-4345.45c-89.94 0-162.88 72.93-162.88 162.9 0 71.96 46.67 133.02 111.4 154.57 8.15 1.49 11.12-3.54 11.12-7.86 0-3.87-.14-14.11-.22-27.7-45.31 9.84-54.87-21.84-54.87-21.84-7.41-18.82-18.09-23.83-18.09-23.83-14.79-10.1 1.12-9.9 1.12-9.9 16.35 1.15 24.95 16.79 24.95 16.79 14.53 24.89 38.13 17.7 47.41 13.53 1.48-10.52 5.69-17.7 10.34-21.77-36.17-4.12-74.2-18.09-74.2-80.51 0-17.79 6.35-32.32 16.77-43.71-1.68-4.12-7.27-20.68 1.6-43.11 0 0 13.67-4.38 44.79 16.69 12.99-3.61 26.93-5.41 40.78-5.48 13.84.07 27.77 1.87 40.78 5.48 31.1-21.07 44.75-16.69 44.75-16.69 8.89 22.43 3.3 38.99 1.63 43.11 10.44 11.39 16.74 25.92 16.74 43.71 0 62.58-38.09 76.35-74.37 80.38 5.84 5.03 11.05 14.97 11.05 30.17 0 21.77-.2 39.34-.2 44.68 0 4.36 2.94 9.43 11.2 7.84 64.68-21.59 111.31-82.6 111.31-154.55 0-89.97-72.94-162.9-162.91-162.9" fill-rule="evenodd"/></svg>');
            background-size: 80% 80%;
            background-position: left center;
          }

          &[href^='mailto:']::before {
            background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="11.026 11.026 77.949 77.949"><path d="M50 11.026c-21.525 0-38.974 17.449-38.974 38.974 0 12.283 5.688 23.232 14.567 30.376l-14.567 8.599H50c21.525 0 38.975-17.449 38.975-38.975 0-21.525-17.452-38.974-38.975-38.974zm-.001 74.481H23.961l8.242-4.786C21.617 74.574 14.493 63.123 14.493 50c0-19.61 15.896-35.506 35.506-35.506S85.506 30.39 85.506 50c0 19.609-15.897 35.507-35.507 35.507z"/><path d="M50 31.062c-10.459 0-18.938 8.479-18.938 18.938S39.541 68.938 50 68.938c3.921 0 7.655-1.319 10.688-3.374.2-.088.38-.21.535-.359l.009-.006-.001-.001a1.833 1.833 0 00-1.277-3.148c-.362 0-.698.108-.982.289l-.007-.009c-2.52 1.836-5.608 2.938-8.965 2.938-8.432 0-15.267-6.836-15.267-15.268S41.568 34.733 50 34.733 65.268 41.568 65.268 50c0 1.274-.158 2.511-.455 3.692-.059.234-.146.456-.216.686-.446 1.17-1.21 1.825-2.368 1.825a2.48 2.48 0 01-2.479-2.479c0-.011.003-.021.003-.031h-.003V43.132h-.011a1.753 1.753 0 00-1.748-1.657c-.752 0-1.389.473-1.641 1.136a9.685 9.685 0 00-6.35-2.36c-5.384 0-9.749 4.365-9.749 9.749s4.365 9.749 9.749 9.749a9.717 9.717 0 007.049-3.025 6.049 6.049 0 0010.271.337c1.227-1.828 1.617-4.563 1.617-7.062.001-10.458-8.478-18.937-18.937-18.937zm0 25.168a6.23 6.23 0 110-12.46 6.23 6.23 0 010 12.46z"/></svg>');
            background-size: 80% 80%;
            background-position: left center;
          }
        }
      }
    }
  }

  .links.contact,
  .links ul + ul.contact {
    padding-top: 1.75rem;
  }

  .links.contact,
  .links ul.contact {
    li {
      flex-basis: 100%;
    }
  }
}
</style>
