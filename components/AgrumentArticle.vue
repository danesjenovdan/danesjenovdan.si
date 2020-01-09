<template>
  <article class="row justify-content-center agrument-article">
    <div class="col-xl-7">
      <div class="article__image">
        <figure>
          <div class="embed-responsive embed-responsive-1200by630">
            <div class="embed-responsive-item d-flex align-items-center">
              <div
                :style="{ 'background-image': `url('${post.image_url}')` }"
                class="background-image blurred"
              />
              <img :src="post.image_url" class="img-fluid" />
            </div>
          </div>
          <figcaption>
            <a
              :href="post.image_source_url"
              target="_blank"
              rel="noopener noreferrer"
              >{{ post.image_source }}</a
            >
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
    <div class="col-xl-9">
      <div class="article__content">
        <!-- eslint-disable-next-line vue/no-v-html -->
        <div class="article__text" v-html="post.content_html" />
        <hr />
        <div class="article__share">
          <div class="share__link">
            <label :for="`share-link-${post.id}`">
              <em>Skopiraj povezavo!</em>
            </label>
            <short-link-input :id="`share-link-${post.id}`" :value="post.url" />
          </div>
          <div class="share__support">
            <more-button
              :to="localePath('donate')"
              text="Podpri nas!"
              color="primary"
              icon="heart"
              small
            />
          </div>
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
        font-size: 2.25rem;
        font-weight: 600;
        line-height: 1;

        @include media-breakpoint-up(xl) {
          font-size: 3.5rem;

          // clamp to max 8 lines
          display: -webkit-box;
          -webkit-line-clamp: 8;
          -webkit-box-orient: vertical;
          overflow: hidden;
          // fix overflow: hidden cutting off overhang letters like jgq
          padding-bottom: 0.175em;
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

      $bg-offset: 35%;
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
      display: flex;
      flex-wrap: wrap;

      .share__link,
      .share__support {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 0.5rem;
      }

      .share__link {
        flex: 1.6;

        label {
          margin: 0;
          margin-right: 1rem;
        }

        input {
          width: 180px;
        }
      }

      .share__support {
        flex: 1;

        .more-button {
          white-space: nowrap;
        }
      }
    }
  }
}
</style>
