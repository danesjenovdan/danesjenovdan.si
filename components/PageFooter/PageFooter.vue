<template>
  <footer class="footer row">
    <form
      v-if="$i18n.locale === 'sl'"
      class="footer-col mt-3 mt-xl-0 col-12 col-lg-6 col-xl-3"
      @submit.prevent="onEmailConfirm"
    >
      <div v-t="'footer.edit-email-settings'" class="lead my-2" />
      <div class="form-group">
        <div>
          <input
            v-model="email"
            type="email"
            class="form-control"
            placeholder="Vpiši svoj e-naslov"
          />
        </div>
        <div class="mt-2">
          <more-button
            :text="'Nadaljuj'"
            :color="color"
            block
            small
            to="#"
            @click.native="onEmailConfirm"
          />
        </div>
      </div>
    </form>
    <div class="footer-col mt-3 mt-xl-0 col-12 col-lg-6 col-xl-3">
      <div v-t="'footer.are-we-friends'" class="lead my-2" />
      <div class="buttons">
        <div class="button-row">
          <circle-icon-button
            :color="color"
            icon="facebook"
            href="https://facebook.com/danesjenovdan"
          />
          <circle-icon-button
            :color="color"
            icon="twitter"
            href="https://twitter.com/danesjenovdan"
          />
        </div>
        <div class="button-row">
          <circle-icon-button
            :color="color"
            icon="youtube"
            href="https://www.youtube.com/channel/UCWMqx3p_QtWjdDRq58Hfh_w"
          />
          <circle-icon-button
            :color="color"
            icon="vimeo"
            href="https://vimeo.com/user26914674"
          />
        </div>
      </div>
    </div>
    <div class="footer-col mt-3 mt-xl-0 col-12 col-lg-6 col-xl-3">
      <div v-t="'footer.our-code-is-online'" class="lead my-2" />
      <div class="buttons">
        <circle-icon-button
          :color="color"
          icon="github"
          href="https://github.com/danesjenovdan"
        />
      </div>
    </div>
    <div
      v-if="$i18n.locale === 'sl'"
      class="footer-col mt-3 mt-xl-0 col-12 col-lg-6 col-xl-3"
    >
      <div class="about mt-3 mt-lg-2">
        <strong>
          Danes je nov dan,
          <br />Inštitut za druga vprašanja
          <br />
        </strong>
        Tobačna ulica 5, 1000 Ljubljana
        <br />
        <br />
        <strong>vsi@danesjenovdan.si</strong>
        <br />
        <strong>+386 64 147 823</strong> (med 10. in 16. uro)
      </div>
    </div>
    <div v-else class="footer-col mt-3 mt-xl-0 col-12 col-lg-12 col-xl-6">
      <div class="about mt-3 mt-lg-2">
        <strong>
          Danes je nov dan (Today is a new day),
          <br />Inštitut za druga vprašanja (Institute for other studies)
          <br />
        </strong>
        Tobačna ulica 5, 1000 Ljubljana, Slovenia
        <br />
        <br />
        <strong>vsi@danesjenovdan.si</strong>
        <br />
        <strong>+386 64 147 823</strong> (10 am - 4 pm CET)
      </div>
    </div>
  </footer>
</template>

<script>
import MoreButton from '~/components/MoreButton.vue';
import CircleIconButton from '~/components/CircleIconButton.vue';

export default {
  components: {
    MoreButton,
    CircleIconButton,
  },
  props: {
    color: {
      type: String,
      default: 'primary',
    },
  },
  data() {
    return {
      email: '',
    };
  },
  methods: {
    onEmailConfirm() {
      this.$router.push(
        this.localePath({ name: 'me', query: { email: this.email } }),
      );
    },
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

    .buttons {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;

      .button-row {
        display: flex;

        .circle-icon-button {
          display: inline-block;
          margin: 0 0.25rem 0.5rem;
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
