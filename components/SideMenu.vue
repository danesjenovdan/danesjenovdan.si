<template>
  <section class="side-menu">
    <nav class="side-menu__nav">
      <header class="logo">
        <div class="logo__mark">
          <nuxt-link :to="localePath('index')">
            <img
              src="~/static/img/logo-circle.png"
              alt="danes je nov dan logo mark"
              class="img-fluid"
            >
          </nuxt-link>
        </div>
        <div class="logo__type">
          <nuxt-link :to="localePath('index')">DANES JE NOV DAN</nuxt-link>
        </div>
        <nuxt-link
          v-for="locale in availableLocales"
          :key="locale.code"
          :to="switchLocalePath(locale.code)"
        >{{ locale.name }}</nuxt-link>
      </header>
      <ul>
        <li
          v-for="item in menuItems"
          :key="item.label"
          :class="{ active: item.active, 'has-children': item.children && item.children.length }"
        >
          <nuxt-link :to="item.url">{{ item.label }}</nuxt-link>
          <ul v-if="item.children && item.children.length">
            <li
              v-for="childItem in item.children"
              :key="childItem.label"
              :class="{ active: childItem.active }"
            >
              <nuxt-link :to="childItem.url">{{ childItem.label }}</nuxt-link>
            </li>
          </ul>
        </li>
      </ul>
    </nav>
  </section>
</template>

<script>
const MENU_ITEMS = [
  {
    label: 'Vsebine',
    url: '/vsebine',
    active: true,
    children: [
      { label: 'One', url: '#' },
      { label: 'Two', url: '#' },
      { label: 'Three', url: '#' },
      { label: 'Four', url: '#' },
      { label: 'Five', url: '#' },
    ],
  },
  { label: 'About', url: '/about' },
  { label: 'Contact', url: '/contact' },
];

export default {
  name: 'SideMenu',
  data() {
    return {
      menuItems: MENU_ITEMS,
    };
  },
  computed: {
    availableLocales() {
      return this.$i18n.locales.filter(i => i.code !== this.$i18n.locale);
    },
  },
};
</script>

<style lang="scss" scoped>
@import '~/assets/scss/_variables.scss';

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

  @include media-breakpoint-up(md) {
    transform: none;
  }

  .side-menu__nav {
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    .logo {
      .logo__mark {
        width: 77px;
        height: 77px;
        margin-bottom: 2rem;
      }

      .logo__type {
        font-family: 'Titillium Web', sans-serif;
        font-weight: 700;
        font-size: 42px;
        line-height: 1;
        color: $color-green;

        a {
          color: inherit;
          text-decoration: none;
        }
      }
    }

    ul {
      padding: 0;
      margin: 0;
      list-style-type: none;

      li {
        font-family: 'Titillium Web', sans-serif;
        font-size: 1.5rem;
        text-transform: uppercase;
        color: #333;

        &.active {
          color: $color-green;
        }

        &.has-children {
          & > a::after {
            display: inline-block;
            content: '';
            width: 1em;
            height: 1em;

            background-image: url('data:image/svg+xml;charset=utf-8,%3Csvg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"%3E%3Cpath d="M50.005 82c.715-.028 1.542-.322 2.063-.812l17-16c.975-1.085 1.377-3.164.25-4.375-1.109-1.194-3.26-1.159-4.375.03l-11.938 11.25V21a3 3 0 0 0-6 0v51.094l-11.938-11.25c-1.025-1.024-3.253-1.213-4.375-.031-1.122 1.181-.764 3.335.25 4.375l17 16a2.885 2.885 0 0 0 2.063.812z" fill="%23#{str-slice("#{$color-green}", 2)}"/%3E%3C/svg%3E');
            background-position: center;
            background-repeat: no-repeat;
            background-size: 100% 100%;
            transform: translateY(0.2rem);
          }
        }

        a {
          &,
          &:hover,
          &:focus,
          &:active {
            color: inherit;
            text-decoration: none;
            transition: color 0.15s ease;
          }

          &:hover {
            color: $color-green;
          }
        }

        ul {
          margin-left: 1rem;
          margin-bottom: 0.5rem;

          li {
            font-size: 1.2rem;
            text-transform: none;
            font-weight: 300;
          }
        }
      }
    }
  }
}
</style>
