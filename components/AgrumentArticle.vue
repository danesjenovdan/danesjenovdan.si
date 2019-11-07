<template>
  <article class="row agrument-article">
    <div class="col-xl-7">
      <div class="article__image">
        <figure>
          <div class="embed-responsive embed-responsive-1200by630">
            <div class="embed-responsive-item d-flex align-items-center">
              <div
                class="background-image blurred"
                :style="{'background-image': `url('${post.image_url}')`}"
              />
              <img :src="post.image_url" class="img-fluid" />
            </div>
          </div>
          <figcaption>
            <a
              :href="post.image_source_url"
              target="_blank"
              rel="noopener noreferrer"
            >{{ post.image_source }}</a>
          </figcaption>
        </figure>
      </div>
    </div>
    <div class="col-xl-5 article__title-col">
      <div class="article__title">
        <h2>{{ post.title }}</h2>
        <div class="article__date">
          <time :datetime="isoDate">{{ sloDate }}</time>
        </div>
      </div>
    </div>
    <div class="col-xl-8 offset-xl-2">
      <div class="article__content">
        <!-- eslint-disable-next-line vue/no-v-html -->
        <div class="article__text" v-html="post.content_html" />
        <hr />
        <div class="article__share">
          <form class="form-inline">
            <div class="form-group">
              <label for="share-link">
                <em>Skopiraj povezavo!</em>
              </label>
              <ShortLinkInput :value="post.url" />
            </div>
            <div class="form-group">
              <more-button
                :to="localePath('support')"
                text="Podpri nas!"
                color="primary"
                icon="heart"
              />
            </div>
          </form>
        </div>
      </div>
    </div>
  </article>
</template>

<script>
import ShortLinkInput from './ShortLinkInput.vue';
import MoreButton from './MoreButton.vue';
import dateMixin from '~/mixins/date.js';

export default {
  name: 'AgrumentArticle',
  components: {
    ShortLinkInput,
    MoreButton,
  },
  mixins: [dateMixin],
  props: {
    post: {
      type: Object,
      required: true,
    },
  },
  computed: {
    isoDate() {
      return this.toIsoDate(this.post.datetime);
    },
    sloDate() {
      return this.toSloDate(this.post.datetime);
    },
  },
};
</script>

<style lang="scss" scoped>
article {
  margin-bottom: 3rem;
  margin-top: 2rem;

  @include media-breakpoint-up(md) {
    margin-top: 0;
  }

  .article__image {
    position: relative;
    z-index: 1;
    margin-right: 1rem;
    margin-left: -0.5rem;

    @include media-breakpoint-up(xl) {
      margin-right: 0rem;
      margin-left: 0rem;
    }

    .background-image {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-size: cover;
      background-repeat: no-repeat;
      background-position: center;
      z-index: -2;

      &.blurred {
        filter: blur(10px);
        z-index: -1;
        transform: scale(1.2);
      }
    }

    img {
      width: 100%;
      height: 100%;
      object-fit: contain;
    }

    figcaption {
      margin-top: 0.25rem;
      font-style: italic;
      text-align: right;

      @include media-breakpoint-up(xl) {
        margin-top: 0.75rem;
      }

      a {
        font-weight: 400;
        text-decoration: underline;
        color: inherit;

        &:hover {
          text-decoration: none;
        }
      }
    }
  }

  .article__title,
  .article__content {
    margin-left: 0.5rem;
    margin-right: -0.5rem;
    background-color: #fff;

    @include media-breakpoint-up(xl) {
      margin-left: 0rem;
      margin-right: 0rem;
      background-color: transparent;
    }
  }

  .article__title-col {
    $bg-offset: 4.5rem;
    margin-top: -$bg-offset;
    z-index: -1;

    @include media-breakpoint-up(xl) {
      z-index: 1;
    }

    .article__title {
      position: relative;
      z-index: 1;
      display: flex;
      flex-direction: column;
      height: 100%;
      justify-content: center;
      padding: 0 1.2rem 1.5rem 1.2rem;
      padding-top: $bg-offset;

      h2 {
        font-size: 2.5rem;
        font-weight: 600;

        @include media-breakpoint-up(xl) {
          font-size: 4.3rem;
        }
      }

      .article__date {
        font-style: italic;
      }
    }
  }

  .article__content {
    padding: 0 1.2rem 1.2rem 1.2rem;

    @include media-breakpoint-up(xl) {
      padding-left: 8rem;
      padding-right: 8rem;
      background-color: #fff;

      $bg-offset: 40%;
      margin-top: -$bg-offset;
      padding-top: calc(2rem + #{$bg-offset});
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
    }

    hr {
      border-top-color: #333;
      margin-top: 1.75rem;
      margin-bottom: 1.75rem;
    }

    .article__share {
      .form-group {
        margin-bottom: 0.25rem;
        margin-right: 1rem;
      }

      em {
        margin-right: 1rem;
      }

      .more-button {
        font-size: 1rem;
        height: calc(1.5rem + 0.75rem + 2px);
        padding: 0.375rem 1.25rem 0.375rem 1rem;
      }
    }
  }
}
</style>
