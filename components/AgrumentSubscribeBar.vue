<template>
  <div class="agrument-subscribe-bar bg-white">
    <div class="d-flex justify-content-between">
      <span/>
      <form class="form-inline">
        <strong v-t="'agrument.subscribe-bar.subscribe-to'" class="my-2 mr-2"/>
        <span v-t="'agrument.subscribe-bar.deliver-it'"/>
        <div class="form-group my-2 mr-3 mx-md-3">
          <input
            id="subscribe-email"
            type="email"
            class="form-control"
            :placeholder="$t('agrument.subscribe-bar.email-address')"
          >
        </div>

        <button type="submit" class="btn btn-primary my-2 px-3">
          <span v-t="'agrument.subscribe-bar.subscribe-action'"/>
        </button>
      </form>
      <a href="https://agrument.danesjenovdan.si/rss/" target="_blank" class="btn btn-outline-primary my-2 px-3">
        <span>RSS</span>
        <span class="icon">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 81.25 81.18" fill="currentColor">
            <path
              d="M13 81.18a13 13 0 1 1 13-13 13 13 0 0 1-13 13zm0-22.05a9 9 0 1 0 9 9 9 9 0 0 0-9-9z"
            ></path>
            <path
              d="M53.53 81.18h-14.7a2 2 0 0 1-2-2A34.79 34.79 0 0 0 2.08 44.43a2 2 0 0 1-2-2v-14.7a2 2 0 0 1 2-2 53.51 53.51 0 0 1 53.45 53.45 2 2 0 0 1-2 2zm-12.75-4h10.71A49.51 49.51 0 0 0 4.08 29.77v10.71a38.8 38.8 0 0 1 36.7 36.7z"
            ></path>
            <path
              d="M79.25 81.18H64.56a2 2 0 0 1-2-2A60.55 60.55 0 0 0 2.08 18.7a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2 79.26 79.26 0 0 1 79.17 79.18 2 2 0 0 1-2 2zm-12.72-4h10.7A75.26 75.26 0 0 0 4.08 4v10.7a64.56 64.56 0 0 1 62.45 62.48z"
            ></path>
          </svg>
        </span>
      </a>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.agrument-subscribe-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 100;
  padding: 0 $content-mobile-padding;
  box-shadow: $box-shadow-lg;

  @include media-breakpoint-up(md) {
    left: $side-menu-width;
  }

  strong {
    font-weight: 600;
  }

  .form-control {
    min-width: 220px;
  }

  .btn {
    text-transform: uppercase;
    font-weight: 600;

    .icon {
      vertical-align: text-bottom;
      display: inline-block;
      width: 1.1em;
      height: 1.4em;
      line-height: 1;
      margin-left: 0.25rem;

      svg {
        width: 100%;
        height: 100%;
      }
    }
  }
}
</style>
