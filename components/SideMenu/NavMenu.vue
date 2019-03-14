<template>
  <ul>
    <li
      v-for="item in menuItems"
      :key="item.key"
      :class="{ 'has-children': item.children && item.children.length }"
    >
      <nuxt-link :to="localePath(item.key)">
        {{ $t(`menu.${item.key}`) }}
        <svg
          v-if="item.children && item.children.length"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="30 18 40 64"
        >
          <path
            d="M50.005 82c.715-.028 1.542-.322 2.063-.812l17-16c.975-1.085 1.377-3.164.25-4.375-1.109-1.194-3.26-1.159-4.375.03l-11.938 11.25V21a3 3 0 0 0-6 0v51.094l-11.938-11.25c-1.025-1.024-3.253-1.213-4.375-.031-1.122 1.181-.764 3.335.25 4.375l17 16a2.885 2.885 0 0 0 2.063.812z"
            fill="currentColor"
          ></path>
        </svg>
      </nuxt-link>
      <ul v-if="item.children && item.children.length">
        <li v-for="childItem in item.children" :key="childItem.key">
          <nuxt-link :to="localePath(childItem.key)">
            {{ $t(`menu.${childItem.key}`) }}
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="18 30 64 40"
            >
              <path
                d="M50.005 82c.715-.028 1.542-.322 2.063-.812l17-16c.975-1.085 1.377-3.164.25-4.375-1.109-1.194-3.26-1.159-4.375.03l-11.938 11.25V21a3 3 0 0 0-6 0v51.094l-11.938-11.25c-1.025-1.024-3.253-1.213-4.375-.031-1.122 1.181-.764 3.335.25 4.375l17 16a2.885 2.885 0 0 0 2.063.812z"
                fill="currentColor"
              ></path>
            </svg>
          </nuxt-link>
        </li>
      </ul>
    </li>
    <li>
      <form :action="localePath('search')" class="search-form">
        <input
          class="form-control search-input"
          type="text"
          name="q"
          :placeholder="$t('menu.search')"
        >
        <button>
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
            <path
              fill="none"
              d="M55.384 18.244a19.062 19.062 0 0 0-5.424-.793c-3.115 0-6.199.775-9.015 2.301-9.194 4.986-12.619 16.521-7.634 25.715a18.847 18.847 0 0 0 11.276 9.143 18.853 18.853 0 0 0 14.439-1.508 18.843 18.843 0 0 0 9.143-11.276 18.84 18.84 0 0 0-1.508-14.438 18.843 18.843 0 0 0-11.277-9.144z"
            ></path>
            <path
              fill="none"
              d="M57.839 9.976a27.728 27.728 0 0 0-7.891-1.154c-4.532 0-9.017 1.128-13.113 3.348-6.479 3.512-11.203 9.338-13.301 16.403-3.684 12.41 1.887 25.9 13.247 32.077a1.915 1.915 0 0 1 .921 2.227l-7.208 24.276a2.082 2.082 0 0 0 1.402 2.586l4.526 1.344c.528.156 1.09.095 1.581-.17a2.062 2.062 0 0 0 1.005-1.232l7.236-24.37a1.918 1.918 0 0 1 1.961-1.366c12.936.858 24.542-7.239 28.231-19.663 2.098-7.065 1.318-14.525-2.194-21.004-3.512-6.481-9.338-11.205-16.403-13.302zm14.001 32.94a22.648 22.648 0 0 1-10.989 13.552 22.673 22.673 0 0 1-10.835 2.767 22.87 22.87 0 0 1-6.519-.953 22.656 22.656 0 0 1-13.553-10.989c-5.991-11.05-1.875-24.915 9.176-30.906 5.353-2.902 11.516-3.549 17.354-1.813a22.646 22.646 0 0 1 13.553 10.989 22.643 22.643 0 0 1 1.813 17.353z"
            ></path>
            <path
              fill="currentColor"
              d="M77.61 21.451c-4-7.379-10.635-12.758-18.681-15.146-16.61-4.937-34.135 4.569-39.067 21.178-4.047 13.632 1.714 28.409 13.739 35.752l-6.778 22.828a5.916 5.916 0 0 0 3.984 7.347l4.526 1.344a5.879 5.879 0 0 0 4.497-.474 5.87 5.87 0 0 0 2.851-3.509l6.811-22.941c.192.004.383.006.574.006 13.868-.001 26.043-8.994 30.043-22.465 2.388-8.046 1.501-16.541-2.499-23.92zm-1.173 22.83c-3.689 12.425-15.296 20.522-28.231 19.663a1.918 1.918 0 0 0-1.961 1.366l-7.236 24.37a2.056 2.056 0 0 1-1.005 1.232 2.07 2.07 0 0 1-1.581.17l-4.526-1.344a2.082 2.082 0 0 1-1.402-2.586l7.208-24.276a1.915 1.915 0 0 0-.921-2.227c-11.36-6.177-16.932-19.667-13.247-32.077 2.098-7.065 6.821-12.891 13.301-16.403a27.436 27.436 0 0 1 13.113-3.348c2.638 0 5.292.382 7.891 1.154 7.065 2.097 12.891 6.821 16.404 13.301 3.511 6.48 4.291 13.94 2.193 21.005z"
            ></path>
            <path
              fill="currentColor"
              d="M56.474 14.573c-5.838-1.736-12.001-1.089-17.354 1.813-11.051 5.991-15.166 19.856-9.176 30.906a22.646 22.646 0 0 0 13.553 10.989c2.148.638 4.34.953 6.519.953 3.744 0 7.451-.932 10.835-2.767A22.644 22.644 0 0 0 71.84 42.915a22.648 22.648 0 0 0-1.813-17.353 22.65 22.65 0 0 0-13.553-10.989zm11.694 27.252a18.843 18.843 0 0 1-9.143 11.276 18.853 18.853 0 0 1-14.439 1.508 18.843 18.843 0 0 1-11.276-9.143c-4.985-9.194-1.56-20.729 7.634-25.715a18.873 18.873 0 0 1 9.015-2.301c1.813 0 3.637.263 5.424.793a18.839 18.839 0 0 1 11.276 9.144 18.832 18.832 0 0 1 1.509 14.438z"
            ></path>
          </svg>
        </button>
      </form>
    </li>
  </ul>
</template>

<script>
export default {
  name: 'NavMenu',
  data() {
    return {
      menuItems: [
        {
          key: 'content',
          children: [
            { key: 'agrument' },
            { key: 'obcasnik' },
            { key: 'videos' },
            { key: 'clippings' },
          ],
        },
        { key: 'calls-to-action' },
        { key: 'tools' },
        { key: 'shop' },
        { key: 'sign-up' },
        {
          key: 'about',
          children: [{ key: 'crew' }, { key: 'values' }],
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
ul {
  padding: 0;
  margin: 0;
  list-style-type: none;

  li {
    font-size: 1.5rem;
    font-weight: 300;
    text-transform: uppercase;
    color: #333;

    a {
      &,
      &:hover,
      &:focus,
      &:active {
        color: inherit;
        text-decoration: none;
        transition: color 0.15s ease;
      }

      &.nuxt-link-exact-active {
        color: $color-green;
      }

      &:hover {
        color: $color-green;
      }

      svg {
        width: 1.1rem;
        height: 1.1rem;
        position: relative;
        top: -0.1em;
      }
    }

    ul {
      margin-left: 1rem;
      margin-bottom: 0.5rem;

      li {
        font-size: 1.15rem;
        text-transform: none;

        a {
          svg {
            opacity: 0;
            transform: rotate(-90deg);
          }

          &.nuxt-link-exact-active {
            svg {
              opacity: 1;
            }
          }
        }
      }
    }
  }

  .search-form {
    position: relative;

    .search-input {
      margin-top: 2rem;
      border-radius: 0;
      background: transparent;
      border: 1px solid #333;

      &::placeholder {
        font-style: italic;
      }

      &:focus {
        border: 1px solid $color-green;
      }
    }

    button {
      position: absolute;
      top: 0;
      right: 0;
      background: transparent;
      border: 0;
      margin: 0;
      width: 2rem;
      padding: 0.3rem;
      height: 100%;
      display: flex;
      transition: color 0.15s ease;

      &:hover {
        color: $color-green;
      }

      svg {
        width: 100%;
        height: 100%;
      }
    }
  }
}
</style>
