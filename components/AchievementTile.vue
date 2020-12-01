<template>
  <a
    :class="['achievement-tile', { empty, href: href === '#' }]"
    :style="{ 'z-index': zIndex }"
    @mouseover="hover"
    @mouseleave="deHover"
    :href="href"
    target="_blank"
  >
    <template v-if="!empty">
      <img class="achievement-icon" :src="`/icons/achievements/${icon}.svg`" />
      <p>{{ text }}</p>
    </template>
  </a>
</template>

<script>
export default {
  props: {
    icon: {
      required: true,
      default: 'agrument',
    },
    text: {
      required: true,
      default: 'Trajlala hopsasa',
    },
    empty: {
      required: false,
      default: false,
    },
    href: {
      required: false,
      default: '#',
    },
  },

  data() {
    return {
      zIndex: 0,
      timer: null,
    };
  },

  methods: {
    hover() {
      window.clearTimeout(this.timer);
      this.zIndex = 2;
    },
    deHover() {
      this.zIndex = 1;
      this.timer = window.setTimeout(() => {
        this.zIndex = 0;
      }, 700);
    },
  },
};
</script>

<style lang="scss">
.achievement-tile {
  display: block;
  float: left;
  padding: 30px;
  position: relative;
  width: 263px;
  height: 263px;
  background-color: #ffffff;
  transition: all 0.7s cubic-bezier(0.19, 1, 0.22, 1);
  cursor: pointer;

  &::before {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background-image: linear-gradient(to right, #cdac54 0%, #df786c 100%);
    opacity: 0.03;
    transition: all 0.7s cubic-bezier(0.19, 1, 0.22, 1);
    z-index: 0;
  }

  &:nth-child(8n + 2)::before,
  &:nth-child(8n + 4)::before,
  &:nth-child(8n + 5)::before,
  &:nth-child(8n + 7)::before {
    opacity: 0.08;
  }

  &:hover {
    transform: translate(0, -10%) scale(1.2);
    text-decoration: none;

    &::before {
      opacity: 1 !important;
    }
  }

  &.href {
    cursor: default;
  }

  &.empty {
    cursor: default;

    &::before {
      display: none;
    }

    &:hover {
      transform: scale(1);
    }

    @include media-breakpoint-down(lg) {
      display: none;

      &:last-child {
        display: flex;
      }
    }

    @include media-breakpoint-down(sm) {
      display: none;
    }
  }

  .achievement-icon {
    width: 70px;
    height: auto;
    position: relative;
  }

  p {
    position: relative;
    color: #333333;
    font-size: 17px;
    font-style: italic;
    letter-spacing: normal;
    line-height: 20px;
    text-align: left;
    margin-top: 26px;
    z-index: 3;
  }

  @include media-breakpoint-down(sm) {
    height: auto;
    overflow: hidden;
    position: relative;
    width: 100%;

    .achievement-icon {
      float: left;
      width: 15%;
      height: auto;
      margin-right: 5%;
    }

    p {
      float: left;
      width: 80%;
      margin-top: 16px;
    }

    &:nth-child(2n + 1)::before {
      opacity: 0.03;
    }

    &:nth-child(2n)::before {
      opacity: 0.08;
    }
  }
}
</style>
