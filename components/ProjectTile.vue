<template>
  <div class="landing-tile bg-white">
    <a href="#" target="_blank" class="landing-tile__link">
      <div
        class="landing-tile__image"
        style="background-image: url('https://api.djnd.si/static/media/images/og-image_1OVqM6O.png');"
      >
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="32 32 448 384" fill="currentColor">
          <path
            d="M311 41c-13-12-33-12-46 0-6 7-9 15-9 23s3 16 9 23l106 105H64c-18 0-32 14-32 32s14 32 32 32h307L265 361c-12 13-12 33 0 46 13 12 33 12 46 0l160-160c12-13 12-33 0-46z"
          ></path>
        </svg>
      </div>
      <div class="landing-tile__content">
        <h1 class="landing-tile__title">Botri sovraštva</h1>
        <div class="landing-tile__text">
          <p
            style="margin: 0px 0px 6px;"
          >Kampanja, v kateri zahtevamo umik oglaševanja v medijih, ki razpihujejo sovraštvo. Ne zgolj politika, temveč tudi neodgovorna podjetja so kriva za zaskrbljujoče stanje v naši državi.</p>
        </div>
      </div>
    </a>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.landing-tile {
  margin-bottom: 1.5rem;

  .landing-tile__link {
    text-decoration: none;
    color: #333;

    &:hover {
      .landing-tile__image {
        &::before {
          opacity: 0.8;
        }

        svg {
          opacity: 1;
        }
      }
    }

    .landing-tile__image {
      width: 100%;
      height: 220px;
      position: relative;
      background-size: cover;
      background-position: center;
      background-color: #fff;
      text-align: center;
      display: flex;
      align-items: center;
      justify-content: center;

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

      svg {
        width: 4rem;
        height: 4rem;
        position: relative;
      }
    }

    .landing-tile__content {
      padding: 2rem;

      .landing-tile__title {
        font-weight: 700;
        margin-bottom: 2rem;
      }

      .landing-tile__text {
        font-size: 1.5rem;
        font-weight: 200;
        line-height: 1.2;
      }
    }
  }
}
</style>
