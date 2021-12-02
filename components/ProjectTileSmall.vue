<template>
  <div class="project-tile bg-white">
    <a
      :href="url"
      target="_blank"
      rel="noopener noreferrer"
      class="project-tile__link"
    >
      <div class="embed-responsive embed-responsive-1200by630">
        <div
          class="embed-responsive-item d-flex align-items-center justify-content-center"
        >
          <div :title="alt" class="project-tile__image">
            <img :src="image" :alt="alt" />
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
        </div>
      </div>
      <div class="project-tile__content">
        <h1 class="project-tile__title" v-text="title" />
        <div v-if="text" class="project-tile__text">
          <p v-text="text" />
        </div>
      </div>
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
    alt: {
      type: String,
      default: null,
    },
    title: {
      type: String,
      required: true,
    },
    text: {
      type: String,
      default: null,
    },
    url: {
      type: String,
      required: true,
    },
  },
  methods: {
    getImage(image) {
      return require(image);
    },
  },
};
</script>

<style lang="scss" scoped>
.project-tile {
  border: 2px solid #df786c;
  height: 100%;

  .project-tile__link {
    text-decoration: none;
    color: inherit;

    &:hover {
      .project-tile__image {
        &::before {
          opacity: 0.8;
        }
      }

      svg {
        opacity: 1;
      }

      .project-tile__title {
        color: $color-red;
      }
    }

    svg {
      width: 3rem;
      height: 3rem;
      position: relative;
      color: #fff;
      transform: rotate(-90deg);
      opacity: 0;
      transition: opacity 0.15s ease;
    }

    .project-tile__image {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;

      &::before {
        content: '';
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
        background-color: $color-red;
      }

      &::after {
        content: '';
        width: 0px;
        height: 0px;
        border-style: solid;
        border-width: 0 20px 20px 20px;
        border-color: transparent transparent #ffffff transparent;
        position: absolute;
        bottom: 0;
        left: 20px;
      }

      &::before,
      svg {
        opacity: 0;
        transition: opacity 0.15s ease;
      }

      img {
        object-fit: cover;
        height: 100%;
      }
    }

    .project-tile__content {
      padding: 1.75rem 2rem;

      .project-tile__title {
        font-weight: 700;
        // margin-bottom: 2rem;
        transition: color 0.15s ease;
      }

      .project-tile__text {
        font-size: 1.125rem;
        font-weight: 200;
        line-height: 1.2;
        margin-top: 1rem;

        p {
          margin: 0 0 0.5rem;
        }
      }
    }
  }
}
</style>
