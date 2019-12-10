<template>
  <section
    :class="{ 'side-menu': true, open: menuOpen }"
    :style="{ visibility: menuVisible ? 'visible' : 'hidden' }"
  >
    <nav ref="sideMenu" class="side-menu__nav">
      <nav-logo />
      <div>
        <nav-menu />
        <div class="lang-license">
          <!-- <language-switcher /> -->
          <hr />
          <license />
        </div>
      </div>
    </nav>
  </section>
</template>

<script>
import NavLogo from './NavLogo.vue';
import NavMenu from './NavMenu.vue';
import License from './License.vue';
// import LanguageSwitcher from './LanguageSwitcher.vue';

export default {
  name: 'SideMenu',
  components: {
    NavLogo,
    NavMenu,
    License,
    // LanguageSwitcher,
  },
  data() {
    return {
      menuOpen: false,
      menuVisible: false,
    };
  },
  mounted() {
    this.$nuxt.$on('toggle-menu', this.toggleMenu);
  },
  beforeDestroy() {
    this.$nuxt.$off('toggle-menu', this.toggleMenu);
  },
  methods: {
    toggleMenu(force = !this.menuOpen) {
      this.menuOpen = force;
      this.menuVisible = true;
      if (this.menuOpen) {
        // move focus to the menu
        this.$nextTick(() => {
          this.$refs.sideMenu.querySelector('li a').focus();
        });
      } else {
        setTimeout(() => {
          this.menuVisible = false;
        }, 200);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.side-menu {
  position: fixed;
  top: calc(#{$top-bar-height} + 2rem);
  left: 0;
  bottom: 0;
  z-index: 120;
  width: 100%;
  background-color: #f0efef;
  padding: 2rem;
  display: flex;
  will-change: transform;
  transform: translateX(-102%);
  transition: transform 0.15s ease-in-out;
  overflow-y: auto;

  &.open {
    transform: none;
    visibility: visible !important;
  }

  @include media-breakpoint-up(md) {
    top: 0;
    width: $side-menu-width;
    background-color: #f6f6f6;

    transform: none;
    visibility: visible !important;
  }

  .side-menu__nav {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 100%;

    .lang-license {
      margin-bottom: 2rem;

      @include media-breakpoint-up(md) {
        margin-bottom: 1rem;
      }
    }
  }
}
</style>
