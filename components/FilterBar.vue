<template>
  <div class="bg-white filter-bar">
    <div class="scroll-container">
      <div class="icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="24 27 52 46" fill="currentColor">
          <path
            d="M38 39.4c-3.3 0-6-2.7-6-5.9 0-3.3 2.7-5.9 6-5.9s6 2.7 6 5.9-2.7 5.9-6 5.9zm0-8.9c-1.7 0-3 1.3-3 2.9 0 1.6 1.3 2.9 3 2.9s3-1.3 3-2.9c0-1.6-1.3-2.9-3-2.9z"
          ></path>
          <path
            d="M33.5 34.8H26c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5h7.5c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5zm40.5 0H42.5c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5H74c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5zm-9 21.1c-3.3 0-6-2.7-6-5.9 0-3.3 2.7-5.9 6-5.9s6 2.7 6 5.9c0 3.3-2.7 5.9-6 5.9zm0-8.8c-1.7 0-3 1.3-3 2.9 0 1.6 1.3 2.9 3 2.9s3-1.3 3-2.9c0-1.6-1.3-2.9-3-2.9z"
          ></path>
          <path
            d="M60.5 51.4H26c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5h34.5c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5zm13.5 0h-4.5c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5H74c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5zM45.9 72.5c-3.3 0-6-2.7-6-5.9s2.7-5.9 6-5.9 6 2.7 6 5.9-2.7 5.9-6 5.9zm0-8.8c-1.7 0-3 1.3-3 2.9s1.3 2.9 3 2.9 3-1.3 3-2.9-1.4-2.9-3-2.9z"
          ></path>
          <path
            d="M41.4 68H26c-.8 0-1.5-.7-1.5-1.5S25.2 65 26 65h15.4c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5zM74 68H50.4c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5H74c.8 0 1.5.7 1.5 1.5S74.8 68 74 68z"
          ></path>
        </svg>
      </div>
      <ul class="filter-list">
        <li v-for="item in items" :key="item.key" :class="{ active: item.active }">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="currentColor">
            <path
              d="M13.94 25.94a1.09 1.09 0 0 1-.77-.32l-9.45-9.45a1.09 1.09 0 0 1 0-1.54l3.37-3.37a1.12 1.12 0 0 1 1.54 0L14 16.63 24.24 6.39a1.09 1.09 0 0 1 1.52 0l3.46 3.28a1.09 1.09 0 0 1 0 1.56L14.87 25.59a1.08 1.08 0 0 1-.68.32 1.09 1.09 0 0 1-.26 0M6 15.4l8 8 12.91-12.94L25 8.68 14.77 18.94a1.12 1.12 0 0 1-1.54 0l-5.37-5.37z"
            ></path>
          </svg>
          <a :href="`#${item.key}`" @click="toggleFilter(item)">{{ item.label }}</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FilterBar',
  props: {
    items: {
      type: Array,
      required: true,
    },
  },
  methods: {
    toggleFilter(item) {
      item.active = !item.active;
    },
  },
};
</script>

<style lang="scss" scoped>
.filter-bar {
  margin-left: -$content-mobile-padding;
  margin-right: -$content-mobile-padding;
  position: relative;
  height: 3.2rem;

  @include media-breakpoint-up(md) {
    margin-left: 0;
    margin-right: 0;
  }

  .scroll-container {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    overflow-y: visible;
    overflow-x: auto;
    display: flex;
    padding: 0.8rem 1rem;

    .icon {
      width: 1.5rem;
      height: 1.5rem;
      display: flex;
      align-items: center;
      flex-shrink: 0;
      color: $color-red;

      svg {
        width: 100%;
        height: 100%;
      }
    }

    .filter-list {
      display: flex;
      font-size: 1.1rem;
      white-space: nowrap;
      margin: 0;
      padding: 0;

      li {
        margin: 0 1rem;
        display: inline-flex;
        align-items: center;
        font-weight: 300;

        &.active {
          font-weight: 500;

          svg {
            visibility: visible;
          }
        }

        svg {
          height: 1.25em;
          margin-right: 0.25rem;
          visibility: hidden;
        }

        a {
          color: inherit;
        }
      }
    }
  }
}
</style>
