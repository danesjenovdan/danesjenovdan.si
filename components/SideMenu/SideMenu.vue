<template>
  <section :class="{ 'side-menu': true, 'open': menuOpen }">
    <nav class="side-menu__nav">
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
    };
  },
  mounted() {
    this.$nuxt.$on('toggle-menu', this.toggleMenu);
  },
  beforeDestroy() {
    this.$nuxt.$off('toggle-menu', this.toggleMenu);
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
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
  z-index: 1;
  width: $side-menu-width;
  background-color: #f6f6f6;
  padding: 2rem;
  display: flex;
  will-change: tranform;
  transform: translateX(-102%);
  transition: transform 0.15s ease-in-out;
  overflow-y: scroll;

  &.open {
    transform: none;
  }

  @include media-breakpoint-up(md) {
    transform: none;
  }

  .side-menu__nav {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
}
</style>
