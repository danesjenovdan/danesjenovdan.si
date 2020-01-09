<template>
  <div :title="name" class="logo-box">
    <a
      :href="url"
      target="_blank"
      rel="noopener noreferrer"
      class="logo-box__content"
    >
      <div class="image-container" :class="[contentClass]">
        <img :src="image" :alt="`${name} logo`" />
      </div>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="30 18 40 64"
        fill="currentColor"
      >
        <path
          d="M50.005 82c.715-.028 1.542-.322 2.063-.812l17-16c.975-1.085 1.377-3.164.25-4.375-1.109-1.194-3.26-1.159-4.375.03l-11.938 11.25V21a3 3 0 0 0-6 0v51.094l-11.938-11.25c-1.025-1.024-3.253-1.213-4.375-.031-1.122 1.181-.764 3.335.25 4.375l17 16a2.885 2.885 0 0 0 2.063.812z"
        />
      </svg>
    </a>
  </div>
</template>

<script>
export default {
  props: {
    image: {
      type: String,
      required: true,
    },
    url: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
    contentClass: {
      type: String,
      default: undefined,
    },
  },
};
</script>

<style lang="scss" scoped>
.logo-box {
  display: block;
  width: 100%;
  height: 0;
  padding-top: 100%;
  position: relative;
  background-color: #fff;

  .logo-box__content {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;

    &:hover {
      &::before {
        opacity: 0.8;
      }

      svg {
        opacity: 1;
      }
    }

    .image-container {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 2rem;

      img {
        width: 100%;
        filter: grayscale(100%);
      }
    }

    svg {
      width: 3rem;
      height: 3rem;
      position: relative;
      color: #fff;
      transform: rotate(-90deg);
    }

    &::before {
      content: '';
      width: 100%;
      height: 100%;
      position: absolute;
      top: 0;
      left: 0;
      background-color: $color-green;
    }

    &::before,
    svg {
      opacity: 0;
      transition: opacity 0.15s ease;
      z-index: 2;
    }
  }
}
</style>
