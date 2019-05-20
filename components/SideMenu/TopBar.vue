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
        <button class="btn" href="#menu" @click="emitToggleMenu">
          <svg
            v-if="!menuOpen"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="19.25 17.139999389648438 60.75 67.52999877929688"
            fill="currentColor"
          >
            <path
              d="M77.33 35.16H21.92a2.67 2.67 0 0 1-2.67-2.67V19.81a2.68 2.68 0 0 1 2.67-2.67h55.41A2.68 2.68 0 0 1 80 19.81v12.68a2.67 2.67 0 0 1-2.67 2.67zm-52.74-5.34h50.07v-7.34H24.59zm52.74 30.1H21.92a2.68 2.68 0 0 1-2.67-2.67V44.56a2.68 2.68 0 0 1 2.67-2.67h55.41A2.68 2.68 0 0 1 80 44.56v12.69a2.68 2.68 0 0 1-2.67 2.67zm-52.74-5.34h50.07v-7.35H24.59zm52.74 30.09H21.92A2.68 2.68 0 0 1 19.25 82V69.32a2.67 2.67 0 0 1 2.67-2.67h55.41A2.67 2.67 0 0 1 80 69.32V82a2.68 2.68 0 0 1-2.67 2.67zm-52.74-5.34h50.07V72H24.59z"
            ></path>
          </svg>
          <svg
            v-else
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 100 100"
            fill="currentColor"
          >
            <path
              d="M70.282 50.003l24.013-23.689a2.368 2.368 0 0 0 .012-3.361L77.514 6.156a2.368 2.368 0 0 0-3.338-.012l-24.175 23.85L25.829 6.145a2.368 2.368 0 0 0-3.338.012L5.694 22.953a2.366 2.366 0 0 0 .011 3.361L29.72 50.003 5.705 73.695a2.372 2.372 0 0 0-.011 3.362l16.797 16.788a2.36 2.36 0 0 0 1.674.693 2.36 2.36 0 0 0 1.663-.682L50.001 70.01l24.174 23.846a2.363 2.363 0 0 0 1.663.682c.606 0 1.212-.231 1.675-.693l16.792-16.788a2.37 2.37 0 0 0-.011-3.361L70.282 50.003zm5.546 38.828L51.664 64.995a2.385 2.385 0 0 0-.291-.234c-.021-.015-.04-.035-.062-.05a2.346 2.346 0 0 0-.356-.19c-.018-.008-.035-.02-.054-.028a2.334 2.334 0 0 0-.39-.118c-.016-.004-.032-.011-.048-.014a2.278 2.278 0 0 0-.404-.041c-.016 0-.032-.004-.048-.004a2.327 2.327 0 0 0-.39.035c-.021.003-.043.003-.064.007a2.368 2.368 0 0 0-.356.103c-.028.01-.057.015-.085.026a2.308 2.308 0 0 0-.308.16c-.035.02-.072.034-.106.057-.087.057-.166.129-.247.199-.039.034-.083.06-.12.097l-.018.018-.004.003-.002.003-24.135 23.808L10.73 75.393l24.027-23.704c.59-.582.808-1.397.656-2.154-.003-.017-.011-.033-.015-.051a2.376 2.376 0 0 0-.116-.383c-.016-.038-.039-.073-.057-.11-.048-.101-.096-.202-.158-.296-.037-.056-.086-.105-.128-.159-.053-.066-.098-.136-.159-.197-.004-.004-.01-.007-.014-.012-.004-.004-.007-.01-.012-.014L10.73 24.616l13.447-13.447 24.161 23.838c.054.053.115.092.172.139.063.051.123.108.189.152.063.041.13.07.196.105.072.038.142.082.217.112.064.026.13.039.195.059.081.025.161.055.244.071.061.012.123.012.184.019.09.01.179.024.269.024.056 0 .111-.011.167-.015.096-.007.192-.011.286-.029.051-.01.099-.03.149-.043.098-.026.195-.049.29-.088.049-.02.093-.05.141-.073.092-.045.184-.087.27-.144.049-.032.091-.075.138-.111.074-.058.151-.11.22-.177L75.828 11.17l13.443 13.447-24.026 23.7-.018.022-.003.002c-.012.012-.02.027-.032.04a2.375 2.375 0 0 0-.267.331c-.009.014-.015.03-.024.045a2.25 2.25 0 0 0-.19.368c-.007.019-.01.038-.017.057a2.343 2.343 0 0 0-.11.382c-.004.024-.004.047-.007.071-.02.126-.034.253-.034.38 0 .03.007.059.008.089.005.121.014.242.037.362.007.038.023.073.032.111.027.11.056.22.099.325.019.047.048.09.07.136.045.093.088.186.146.273.036.054.083.102.124.154.054.068.101.14.164.204l.015.012.01.012 24.022 23.7-13.442 13.438z"
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
  data() {
    return {
      menuOpen: false,
    };
  },
  mounted() {
    this.$nuxt.$on('toggle-menu', this.toggleMenu);
  },
  beforeDestroy() {
    this.$nuxt.$off('toggle-menu', this.toggleMenu);
  },
  methods: {
    emitToggleMenu(event) {
      event.preventDefault();
      this.$nuxt.$emit('toggle-menu');
    },
    toggleMenu(force = !this.menuOpen) {
      this.menuOpen = force;
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
        color: inherit;
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
