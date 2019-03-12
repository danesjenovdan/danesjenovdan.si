<template>
  <section class="side-menu">
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
};
</script>

<style lang="scss" scoped>
.side-menu {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: $side-menu-width;
  background-color: #f6f6f6;
  padding: 2rem;
  display: flex;
  will-change: tranform;
  transform: translateX(-102%);
  transition: transform 0.15s ease-in-out;
  overflow-y: scroll;

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
