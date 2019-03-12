<template>
  <div class="landing-tile bg-white">
    <a href="#" target="_blank" class="landing-tile__link">
      <div
        class="landing-tile__image"
        style="background-image: url('https://api.djnd.si/static/media/images/og-image_1OVqM6O.png');"
      >
        <span class="icon-arrow-right"/>
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

    .landing-tile__image {
      width: 100%;
      height: 220px;
      position: relative;
      background-size: cover;
      background-position: center;
      background-color: #fff;
      text-align: center;
    }

    .landing-tile__image::before {
      content: '';
      width: 100%;
      height: 100%;
      position: absolute;
      top: 0;
      left: 0;
      background-color: $color-red;
      opacity: 0;
    }

    .landing-tile__image::after {
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

// .landing-tile__link,
// .landing-tile__link:hover,
// .landing-tile__link:active,
// .landing-tile__link:focus,
// .landing-tile__link:visited {
//   display: block;
//   height: 100%;
//   text-decoration: none;
//   color: inherit;
// }

// .landing-tile--square .landing-tile__link {
//   position: absolute;
//   top: 0;
//   left: 0;
//   bottom: 0;
//   right: 0;
// }

// .landing-tile__image::before,
// .landing-tile__image .icon-arrow-right,
// .landing-tile__cover--hover {
//   opacity: 0;
//   -webkit-transition: opacity 0.3s;
//   -moz-transition: opacity 0.3s;
//   -o-transition: opacity 0.3s;
//   -ms-transition: opacity 0.3s;
//   transition: opacity 0.3s;
// }

// .landing-tile__image .icon-arrow-right {
//   position: absolute;
//   top: 63px;
//   left: 0;
//   width: 100%;
//   color: #272727;
//   z-index: 2;
//   font-size: 56px;
// }

// .landing-tile__link:hover .landing-tile__image::before,
// .landing-tile__link:hover .landing-tile__cover--hover {
//   opacity: 0.8;
// }

// .landing-tile__link:hover .landing-tile__image .icon-arrow-right {
//   opacity: 1;
// }

// .landing-tile__separator {
//   border-top-width: 6px;
//   border-top-color: #f0efef;
//   margin: 0 8px;
// }

// .landing-tile__text ul {
//   list-style: none;
//   padding: 0;
// }

// .landing-tile__text ul li {
//   margin-bottom: 12px;
//   position: relative;
//   padding-left: 30px;
// }

// .landing-tile__text ul li::before {
//   content: '\e605';
//   display: block;
//   color: #f0efef;
//   position: absolute;
//   left: 2px;
//   top: 4px;

//   font-family: 'icomoon';
//   speak: none;
//   font-style: normal;
//   font-weight: normal;
//   font-variant: normal;
//   text-transform: none;
//   line-height: 1;
//   -webkit-font-smoothing: antialiased;
//   -moz-osx-font-smoothing: grayscale;
// }

// .landing-tile__cover {
//   position: absolute;
//   top: 0;
//   left: 0;
//   bottom: 0;
//   right: 0;
//   font-size: 24px;
//   font-weight: 700;
//   text-transform: uppercase;
//   text-align: center;
//   padding: 50px;
//   padding-bottom: 0px;
// }

// .landing-tile__link:hover .icon-arrow-down-right,
// .landing-tile__link-more:hover .icon-arrow-down-right,
// .landing-section__header h2 a:hover + .icon-arrow-down-right {
//   -webkit-transform: rotate(-45deg);
//   -moz-transform: rotate(-45deg);
//   -o-transform: rotate(-45deg);
//   -ms-transform: rotate(-45deg);
//   transform: rotate(-45deg);
// }

// .landing-tile--news .landing-tile__title {
//   font-size: 24px;
//   line-height: 35px;
//   color: #525252;
//   text-transform: none;
//   font-weight: 600;
// }

// .landing-tile--news .landing-tile__date {
//   font-size: 12px;
//   line-height: 20px;
//   margin-bottom: 16px;
//   font-style: italic;
//   font-weight: 400;
// }

// .landing-tile--news .landing-tile__text p {
//   font-size: 16px;
//   line-height: 24px;
// }

// .landing-tile__link-more,
// .landing-tile__link-more:hover,
// .landing-tile__link-more:active,
// .landing-tile__link-more:focus,
// .landing-tile__link-more:visited {
//   text-decoration: none;
//   font-weight: 600;
//   color: #525252;
//   /* margin-left: 10px; */
//   display: inline-block;
// }

// .landing-tile__link-more:hover {
//   text-decoration: underline;
// }

// .landing-tile__link-more .icon-arrow-down-right,
// .landing-section__header h2 a + .icon-arrow-down-right {
//   display: inline-block;
// }
</style>
