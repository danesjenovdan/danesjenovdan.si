<template>
  <article class="row agrument-article">
    <div class="col-md-7">
      <div class="article__image">
        <figure>
          <div class="embed-responsive embed-responsive-16by9">
            <div class="embed-responsive-item d-flex align-items-center">
              <div
                class="background-image"
                :style="{'background-image': `url('${post.image_url}')`}"
              />
              <img :src="post.image_url" class="img-fluid">
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
    <div class="col-md-5">
      <div class="article__title">
        <h2>{{ post.title }}</h2>
        <div class="article__date">
          <time :datetime="isoDate">{{ sloDate }}</time>
        </div>
      </div>
    </div>
    <div class="col-md-8 offset-md-2">
      <div class="bg-white article__content">
        <!-- eslint-disable-next-line vue/no-v-html -->
        <div class="article__text" v-html="post.content_html"/>
        <hr>
        <div class="article__share">
          <form class="form-inline">
            <div class="form-group">
              <label for="share-link">
                <em>Skopiraj povezavo!</em>
              </label>
              <ShortLinkInput :value="`https://agrument.danesjenovdan.si/${urlDate}`"/>
            </div>
          </form>
        </div>
      </div>
    </div>
  </article>
</template>

<script>
import ShortLinkInput from './ShortLinkInput.vue';

export default {
  name: '',
  components: {
    ShortLinkInput,
  },
  props: {
    post: {
      type: Object,
      required: true,
    },
  },
  computed: {
    isoDate() {
      return this.post.datetime.split('T')[0];
    },
    sloDate() {
      return this.isoDate
        .split('-')
        .reverse()
        .join('. ');
    },
    urlDate() {
      return this.isoDate
        .split('-')
        .reverse()
        .join('.');
    },
  },
};
</script>

<style lang="scss" scoped>
article {
  margin-bottom: 6rem;
  margin-top: 2rem;

  @include media-breakpoint-up(md) {
    margin-top: 0;
  }

  .article__image {
    position: relative;
    z-index: 1;

    .background-image {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-size: cover;
      background-repeat: no-repeat;
      background-position: center;
      filter: blur(20px);
      z-index: -1;
    }

    img {
      width: 100%;
      height: 100%;
      object-fit: contain;
    }

    figcaption {
      margin-top: 0.75rem;
      font-style: italic;
      text-align: right;

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

  .article__title {
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    height: 100%;
    justify-content: center;

    h2 {
      font-size: 2.9rem;
      font-weight: 600;

      @include media-breakpoint-up(md) {
        font-size: 4.3rem;
      }
    }

    .article__date {
      font-style: italic;
      margin-top: 1rem;
    }
  }

  .article__content {
    margin-left: -$content-mobile-padding;
    margin-right: -$content-mobile-padding;
    padding-left: $content-mobile-padding;
    padding-right: $content-mobile-padding;
    padding-bottom: 2.5rem;

    $bg-offset: 75%;
    padding-top: calc(2.5rem + #{$bg-offset});
    margin-top: -$bg-offset;

    @include media-breakpoint-up(md) {
      padding-left: 8rem;
      padding-right: 8rem;

      $bg-offset: 45%;
      padding-top: calc(2.5rem + #{$bg-offset});
      margin-top: -$bg-offset;
    }

    /deep/ .article__text {
      font-size: 1.1rem;
      font-weight: 300;

      @include media-breakpoint-up(md) {
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
      margin-top: 3rem;
      margin-bottom: 2rem;
    }

    .article__share {
      em {
        margin-right: 2rem;
      }
    }
  }
}
</style>
