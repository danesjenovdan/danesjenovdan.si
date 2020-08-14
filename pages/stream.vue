<template>
  <div class="donation-landing-container">
    <donation-logo />
    <div class="row justify-content-center">
      <div class="limit-like-p">
        <h1 class="mega-header">
          #vladozlom
        </h1>
        <div class="embed-responsive embed-responsive-16by9">
          <div class="embed-responsive-item d-flex align-items-center">
            <iframe
              :src="
                embedUrl('https://www.youtube.com/watch?v=mPY0h_6qUww', false)
              "
              allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen
            />
          </div>
        </div>
      </div>
    </div>
    <div class="row" style="height: 90px;"></div>
  </div>
</template>

<script>
import videoMixin from '~/mixins/video.js';

export default {
  layout: 'default',

  pageColor: 'secondary',

  nuxtI18n: {
    paths: {
      sl: '/vladozlom',
      en: '/stream',
    },
  },

  mixins: [videoMixin],
};
</script>

<style lang="scss" scoped>
// .donation-landing-container {
//   @include media-breakpoint-up(xl) {
//     padding-left: 150px;
//     padding-right: 150px;
//   }
// }
/deep/ .logo {
  width: 230px;

  @include media-breakpoint-up(sm) {
    width: 300px;
  }
}
.donate-href {
  width: 100%;
  max-width: 250px;
  font-style: italic;
  font-size: 25px;
  font-weight: 500;
  line-height: 32px;
  text-decoration: underline;
  color: $black;

  margin: 20px;
  text-decoration: none;

  .underline {
    text-decoration: underline;
  }

  @include media-breakpoint-up(lg) {
    margin-left: 80px;
  }
}
.mega-header {
  position: relative;
  font-size: 50px;
  line-height: 60px;
  color: rgba(223, 120, 108, 0.98);
  font-weight: 700;
  font-style: italic;
  text-shadow: -1px 1px 0 #333333, 1px 1px 0 #333333, 1px -1px 0 #333333,
    -1px -1px 0 #333333;

  margin-bottom: -30px;
  padding-left: 50px;
  z-index: 200;

  .strikethrough {
    position: relative;
    &::after {
      content: '';
      display: block;
      width: 100%;
      height: 9px;
      background-color: #393939;
      position: absolute;
      left: 0;
      top: 55%;
    }
  }

  @include media-breakpoint-up(md) {
    font-size: 90px;
    line-height: 90px;
  }
}
.embed-responsive {
  z-index: 1;
}
h1 {
  font-size: 80px;
  font-weight: 600;
  line-height: 100px;
  font-style: italic;
  letter-spacing: -1px;
  margin-top: 50px;
  margin-bottom: 50px;
  text-align: left;
  width: 100%;
}
p {
  font-size: 20px;
  color: #333333;
  font-weight: 200;
  width: 100%;
  max-width: 872px;
  margin-top: 1em;
  margin-bottom: 1em;
  padding-left: 30px;
  padding-right: 30px;

  @include media-breakpoint-up(md) {
    font-size: 30px;
    padding: 0;
  }
}
.limit-like-p {
  width: 100%;
  max-width: 902px;
}
.donation-info-box {
  @include media-breakpoint-up(md) {
    margin-top: 40px;
    margin-bottom: 40px;
  }
}
.vec-nas-je-kot {
  margin-top: 50px;
  margin-bottom: 50px;
  margin-left: -1.5em;
  margin-right: -1.5em;
  background-image: linear-gradient(
    to right,
    rgba(205, 172, 84, 0.2) 0%,
    rgba(223, 120, 108, 0.2) 100%
  );
  padding: 40px 1.5em 20px 1.5em;

  @include media-breakpoint-up(md) {
    margin-left: -3em;
    margin-right: -3em;
    padding: 40px 3em 20px 3em;
  }
}
.under-vec-nas-je-kot {
  margin-top: 50px;
  margin-bottom: 70px;
  background-image: linear-gradient(
    to right,
    rgba(205, 172, 84, 0.2) 0%,
    rgba(223, 120, 108, 0.2) 100%
  );

  padding: 20px;

  h1 {
    width: auto;
    font-size: 60px;
    line-height: 140px;
    font-weight: 700;
    line-height: 100px;
    font-style: italic;
    @include media-breakpoint-up(xl) {
      margin-right: 60px;
    }
  }
}
.project-line {
  background-color: rgba(223, 120, 108, 0.05);
  padding: 30px;
  margin-bottom: 30px;
  display: flex;
  justify-content: center;

  img {
    width: 90px;
    height: auto;
    margin-right: 30px;
    margin-bottom: 20px;
  }

  h2 {
    font-weight: 600;
    font-style: italic;
    font-size: 40px;
    min-width: 250px;
  }

  p {
    font-size: 20px;
    padding-left: 0;
    padding-right: 0;
  }

  .partnerships {
    font-weight: 200;
    .partner {
      text-transform: uppercase;
      font-weight: 700;
    }
  }

  .partnership-images {
    img {
      margin-top: 20px;
      width: 50px;
      height: auto;
    }
  }

  @include media-breakpoint-up(md) {
    padding: 60px;
  }
}
.row-social {
  h1 {
    font-size: 50px;
    line-height: 60px;
    text-align: center;

    @include media-breakpoint-up(md) {
      font-size: 90px;
      line-height: 110px;
    }
  }
}
.square-icon-button {
  display: inline-block;
  width: 100px;
  height: 100px;

  @include media-breakpoint-up(md) {
    width: 150px;
    height: 150px;
  }
}
.donation-social {
  margin-top: 50px;
  padding-bottom: 50px;
  margin-bottom: 20px;
  position: relative;

  &::after {
    content: '';
    display: block;
    width: 100%;
    position: absolute;
    bottom: 0;
    border-bottom: 4px solid $black;
    opacity: 0.2;
  }
}
.confirm-button {
  height: 100px;
  margin-top: 22px;
  margin-bottom: 22px;

  @include media-breakpoint-up(md) {
    height: 150px;
    width: 500px;
    margin-top: 0;
    margin-bottom: 0;
  }
}
.donation-scale-container {
  margin-bottom: 150px;

  @include media-breakpoint-up(md) {
    // position: absolute;
    // bottom: 40px;
    margin-bottom: 0;
  }
}
</style>
