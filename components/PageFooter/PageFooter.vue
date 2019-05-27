<template>
  <footer class="footer row">
    <div class="footer-col mt-3 mt-xl-0 col-12 col-lg-6 col-xl-3">
      <div class="lead my-2">
        Uredi svoje email nastavitve
      </div>
      <div class="form-group">
        <div>
          <input class="form-control" placeholder="vpiši svoj e-naslov">
        </div>
        <div class="mt-2">
          <more-button block :to="'LOL'" :text="'Pošlji'" color="warning"/>
        </div>
      </div>
    </div>
    <div class="footer-col mt-3 mt-xl-0 col-12 col-lg-6 col-xl-3">
      <div class="lead my-2">
        A še kje nismo frendi?
      </div>
      <div class="buttons">
        <circle-icon-button
          color="warning"
          icon="facebook"
          href="https://facebook.com/danesjenovdan"
        />
        <circle-icon-button
          color="warning"
          icon="twitter"
          href="https://twitter.com/danesjenovdan"
        />
        <circle-icon-button
          color="warning"
          icon="youtube"
          href="https://youtube.com/danesjenovdan"
        />
        <circle-icon-button
          color="warning"
          icon="vimeo"
          href="https://vimeo.com/danesjenovdan"
        />
      </div>
    </div>
    <div class="footer-col mt-3 mt-xl-0 col-12 col-lg-6 col-xl-3">
      <div class="lead my-2">
        Vsa naša koda je online. Izvoli!
      </div>
      <div class="buttons">
        <circle-icon-button
          color="warning"
          icon="github"
          href="https://github.com/danesjenovdan"
        />
      </div>
    </div>
    <div class="footer-col mt-3 mt-xl-0 col-12 col-lg-6 col-xl-3">
      <div class="about mt-3 mt-lg-2">
        <strong>
          Danes je nov dan,<br>
          Inštitut za druga vprašanja<br>
        </strong>
        Tobačna ulica 5, 1000 Ljubljana<br>
        <br>
        <strong>vsi@danesjenovdan.si</strong><br>
        <strong>+386 64 147 823</strong> (med 10.0 in 16.00)
      </div>
    </div>
  </footer>
</template>

<script>
import MoreButton from '~/components/MoreButton.vue';
import CircleIconButton from '~/components/CircleIconButton.vue';

export default {
  name: 'PageFooter',
  components: {
    MoreButton,
    CircleIconButton,
  },
};
</script>

<style lang="scss" scoped>
.footer {
  @include media-breakpoint-up(xl) {
    margin-top: 2rem;
  }

  .footer-col {
    padding-bottom: 2rem;

    &::after {
      content: '';
      display: block;
      width: 30%;
      height: 1px;
      background-color: #333;
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
    }

    &:last-child::after {
      display: none;
    }

    @include media-breakpoint-up(lg) {
      &:nth-child(3)::after {
        display: none;
      }
    }

    @include media-breakpoint-up(xl) {
      &::after {
        display: none;
      }
    }

    .lead {
      font-size: 1.25rem;
      font-weight: 500;
      font-style: italic;
      text-align: center;
    }

    .form-group {
      margin-bottom: 0;
      max-width: 300px;
      margin: 0 auto;
    }

    .more-button {
      font-size: 1.25rem;
      padding: 0.2rem 1.5rem 0.2rem 0.75rem;
    }

    .buttons {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;

      .circle-icon-button {
        margin-bottom: 0.5rem;
        @include media-breakpoint-up(xl) {
          width: 3.5rem;
          height: 3.5rem;
        }
      }
    }

    .about {
      text-align: center;
      font-style: italic;

      @include media-breakpoint-up(xl) {
        text-align: left;
      }

      strong {
        font-weight: 600;
      }
    }
  }
}
</style>
