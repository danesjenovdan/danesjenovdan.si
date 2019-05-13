<template>
  <a class="box-link">
    <div class="box-link__content">
      <h3>
        POSADKA
        <span class="arrow">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="18 30 64 40"
            fill="currentColor"
          >
            <path
              d="M50.005 82c.715-.028 1.542-.322 2.063-.812l17-16c.975-1.085 1.377-3.164.25-4.375-1.109-1.194-3.26-1.159-4.375.03l-11.938 11.25V21a3 3 0 0 0-6 0v51.094l-11.938-11.25c-1.025-1.024-3.253-1.213-4.375-.031-1.122 1.181-.764 3.335.25 4.375l17 16a2.885 2.885 0 0 0 2.063.812z"
            ></path>
          </svg>
        </span>
      </h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.</p>
      <div
        class="box-link__image"
        :style="{'background-image': 'url(/img/about-people.svg)'}"
      />
    </div>
  </a>
</template>

<style lang="scss" scoped>
.box-link {
  display: block;
  height: 0;
  padding-top: 90%;
  position: relative;
  margin-bottom: 2.5rem;

  .box-link__content {
    border: 2px solid $color-green;
    padding: 1rem 1rem;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    h3 {
      margin: 0;
      font-weight: 700;
      font-size: 1.85rem;

      .arrow {
        margin-left: 0.5rem;

        svg {
          width: 2.5rem;
          height: 2.5rem;
          position: relative;
          top: -0.1em;
          transform: rotate(-90deg);
        }
      }
    }

    p {
      font-size: 1.25rem;
      font-weight: 200;
      font-style: italic;
      line-height: 1.25;
      margin-top: 0.75rem;
    }

    .box-link__image {
      position: absolute;
      background-size: contain;
      background-position: bottom center;
      background-repeat: no-repeat;
      bottom: -1.5rem;
      right: 0.5rem;
      width: 70%;
      height: 100%;
    }
  }
}
</style>
