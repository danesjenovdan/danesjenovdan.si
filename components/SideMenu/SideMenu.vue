<template>
  <section
    :class="{ 'side-menu': true, 'open': menuOpen }"
    :style="{ 'visibility': menuVisible ? 'visible' : 'hidden' }"
  >
    <nav ref="sideMenu" class="side-menu__nav">
      <nav-logo/>
      <nav-menu/>
    </nav>
  </section>
</template>

<script>
import NavLogo from './NavLogo';
import NavMenu from './NavMenu';

export default {
  name: 'SideMenu',
  components: {
    NavLogo,
    NavMenu,
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
          this.$refs.sideMenu.querySelector('a').focus();
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
  top: 0;
  left: 0;
  bottom: 0;
  z-index: 120;
  width: $side-menu-width;
  background-color: #f6f6f6;
  padding: 2rem;
  display: flex;
  will-change: transform;
  transform: translateX(-102%);
  transition: transform 0.15s ease-in-out;
  overflow-y: scroll;

  &.open {
    transform: none;
    visibility: visible !important;
  }

  @include media-breakpoint-up(md) {
    transform: none;
    visibility: visible !important;
  }

  .side-menu__nav {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
}
</style>
