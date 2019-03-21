<template>
  <div class="top-bar">
    <header class="logo">
      <div class="logo__mark">
        <nuxt-link :to="localePath('index')">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="73 69 300 300">
            <defs>
              <clipPath id="toplogoclip" transform="translate(65.03 61)">
                <circle cx="158.15" cy="157.81" r="150" fill="none"></circle>
              </clipPath>
            </defs>
            <g clip-path="url(#toplogoclip)">
              <path d="M-.005 292.286L127.993.004l64.762 28.361L64.757 320.647z" fill="#cfad54"></path>
              <path
                d="M64.765 320.632L192.764 28.351l64.762 28.361-127.999 292.281z"
                fill="#df786c"
              ></path>
              <path d="M129.53 349.012l128-292.281 64.762 28.36-127.999 292.282z" fill="#6ca89f"></path>
              <path
                d="M194.292 377.363L322.291 85.082l64.762 28.361-127.999 292.282z"
                fill="#cfad54"
              ></path>
              <path
                fill="#df786c"
                d="M259.053 405.733L387.052 113.45l64.762 28.361-127.999 292.282z"
              ></path>
            </g>
          </svg>
        </nuxt-link>
      </div>
      <div class="logo__type">
        <nuxt-link :to="localePath('index')">{{ $t('danes-je-nov-dan') }}</nuxt-link>
      </div>
      <div class="menu-toggle">
        <button class="btn" href="#menu" @click="toggleMenu">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="19.25 17.139999389648438 60.75 67.52999877929688"
            fill="currentColor"
          >
            <path
              d="M77.33 35.16H21.92a2.67 2.67 0 0 1-2.67-2.67V19.81a2.68 2.68 0 0 1 2.67-2.67h55.41A2.68 2.68 0 0 1 80 19.81v12.68a2.67 2.67 0 0 1-2.67 2.67zm-52.74-5.34h50.07v-7.34H24.59zm52.74 30.1H21.92a2.68 2.68 0 0 1-2.67-2.67V44.56a2.68 2.68 0 0 1 2.67-2.67h55.41A2.68 2.68 0 0 1 80 44.56v12.69a2.68 2.68 0 0 1-2.67 2.67zm-52.74-5.34h50.07v-7.35H24.59zm52.74 30.09H21.92A2.68 2.68 0 0 1 19.25 82V69.32a2.67 2.67 0 0 1 2.67-2.67h55.41A2.67 2.67 0 0 1 80 69.32V82a2.68 2.68 0 0 1-2.67 2.67zm-52.74-5.34h50.07V72H24.59z"
            ></path>
          </svg>
        </button>
      </div>
    </header>
  </div>
</template>

<script>
export default {
  name: 'TopBar',
  methods: {
    toggleMenu(event) {
      event.preventDefault();
      this.$nuxt.$emit('toggle-menu');
    },
  },
};
</script>


<style lang="scss" scoped>
.top-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  padding: 1.2rem $content-mobile-padding;
  background-color: #f6f6f6;
  transition: transform 0.15s ease-in-out;
  transform: none;

  @include media-breakpoint-up(md) {
    transform: translateY(-102%);
    visibility: hidden;
  }

  .logo {
    display: flex;
    align-items: center;

    .logo__mark {
      width: 66px;
      height: 66px;
      margin-right: 1.2rem;

      a {
        display: inline-block;

        svg {
          width: 100%;
          height: 100%;
        }
      }
    }

    .logo__type {
      font-weight: 700;
      font-size: 26px;
      text-transform: uppercase;
      line-height: 0.95;
      color: $color-green;
      max-width: 125px;
      display: flex;
      align-items: center;

      a {
        color: inherit;
        text-decoration: none;
      }
    }

    .menu-toggle {
      width: 36px;
      margin-left: auto;
      margin-right: 1rem;

      .btn {
        color: #333;
        padding: 0;

        svg {
          width: 100%;
          height: 100%;
        }
      }
    }
  }
}
</style>
