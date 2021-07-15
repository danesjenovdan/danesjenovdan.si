<template>
  <article class="row news-article justify-content-center">
    <div class="col col-xl-9">
      <div v-if="logoSrc" class="article-top-logo">
        <a :href="logoLink" target="_blank">
          <img
            :src="logoSrc"
            :alt="logoAlt"
            class="img-fluid"
            style="max-width: 270px"
          />
        </a>
      </div>
      <div class="article__title">
        <h2>{{ title }}</h2>
        <div v-if="date" class="article__date">
          <time :datetime="toIsoDate(date)">{{ toSloDate(date) }}</time>
        </div>
      </div>
      <div class="article__content">
        <div class="article__text">
          <slot />
        </div>
      </div>
    </div>
  </article>
</template>

<script>
import dateMixin from '~/mixins/date.js';

export default {
  mixins: [dateMixin],
  props: {
    title: {
      type: String,
      required: true,
    },
    date: {
      type: String,
      default: null,
    },
    logoSrc: {
      type: String,
      default: null,
    },
    logoAlt: {
      type: String,
      default: null,
    },
    logoLink: {
      type: String,
      default: null,
    },
  },
};
</script>

<style lang="scss" scoped>
.news-article {
  margin-bottom: 2rem;
  margin-top: 2rem;

  .article-top-logo {
    padding-top: 2rem;
  }

  .article-top-logo + .article__title {
    padding-top: 2rem;
  }

  .article__title,
  .article__content,
  .article-top-logo {
    background-color: #fff;
    padding-left: 1.2rem;
    padding-right: 1.2rem;

    @include media-breakpoint-up(xl) {
      padding-left: 8rem;
      padding-right: 8rem;
    }
  }

  .article__title {
    padding-top: 1.2rem;
    padding-bottom: 1.5rem;

    @include media-breakpoint-up(xl) {
      padding-top: 4rem;
    }

    h2 {
      font-size: 2.25rem;
      font-weight: 600;
      line-height: 1;

      @include media-breakpoint-up(xl) {
        font-size: 3.5rem;
        margin-bottom: 1.5rem;
      }
    }

    .article__date {
      font-style: italic;
    }
  }

  .article__content {
    padding-bottom: 0.2rem;

    @include media-breakpoint-up(xl) {
      padding-bottom: 4rem;
    }

    /deep/ .article__text {
      font-size: 1.125rem;
      font-weight: 300;
      line-height: 1.4;

      @include media-breakpoint-up(xl) {
        font-size: 1.25rem;
      }

      a {
        font-weight: 500;
        text-decoration: underline;
        color: inherit;

        &:hover {
          text-decoration: none;
        }
      }

      b,
      strong {
        font-weight: 600;
      }

      hr {
        // border-top-color: #333;
        margin: 3rem 0;
      }
    }
  }
}
</style>
