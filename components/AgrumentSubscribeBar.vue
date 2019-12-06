<template>
  <div class="agrument-subscribe-bar bg-white">
    <div class="bar-container">
      <form @submit.prevent="onSubscribe" class="form-inline">
        <strong v-t="'agrument.subscribe-bar.subscribe-to'" />
        <span v-t="'agrument.subscribe-bar.deliver-it'" class="description" />
        <div class="email-controls d-flex">
          <div class="form-group my-2 mr-2">
            <input
              id="subscribe-email"
              v-model="email"
              :placeholder="$t('agrument.subscribe-bar.email-address')"
              type="email"
              class="form-control"
            />
          </div>
          <button
            :disabled="loading || !email || email.indexOf('@') === -1"
            type="submit"
            class="btn btn-primary my-2 px-3"
          >
            <span
              v-if="!loading"
              v-t="'agrument.subscribe-bar.subscribe-action'"
            />
            <div v-else class="lds-dual-ring" />
          </button>
          <a
            href="https://agrument.danesjenovdan.si/rss/"
            target="_blank"
            class="rss btn btn-outline-primary my-2 px-0 d-none d-lg-block d-xl-none"
          >
            <span>RSS</span>
            <span class="icon">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 81.25 81.18"
                fill="currentColor"
              >
                <path
                  d="M13 81.18a13 13 0 1 1 13-13 13 13 0 0 1-13 13zm0-22.05a9 9 0 1 0 9 9 9 9 0 0 0-9-9z"
                />
                <path
                  d="M53.53 81.18h-14.7a2 2 0 0 1-2-2A34.79 34.79 0 0 0 2.08 44.43a2 2 0 0 1-2-2v-14.7a2 2 0 0 1 2-2 53.51 53.51 0 0 1 53.45 53.45 2 2 0 0 1-2 2zm-12.75-4h10.71A49.51 49.51 0 0 0 4.08 29.77v10.71a38.8 38.8 0 0 1 36.7 36.7z"
                />
                <path
                  d="M79.25 81.18H64.56a2 2 0 0 1-2-2A60.55 60.55 0 0 0 2.08 18.7a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2 79.26 79.26 0 0 1 79.17 79.18 2 2 0 0 1-2 2zm-12.72-4h10.7A75.26 75.26 0 0 0 4.08 4v10.7a64.56 64.56 0 0 1 62.45 62.48z"
                />
              </svg>
            </span>
          </a>
        </div>
      </form>
      <a
        href="https://agrument.danesjenovdan.si/rss/"
        target="_blank"
        class="rss btn btn-outline-primary my-xl-2 px-0 d-block d-lg-none d-xl-block"
      >
        <span>RSS</span>
        <span class="icon">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 81.25 81.18"
            fill="currentColor"
          >
            <path
              d="M13 81.18a13 13 0 1 1 13-13 13 13 0 0 1-13 13zm0-22.05a9 9 0 1 0 9 9 9 9 0 0 0-9-9z"
            />
            <path
              d="M53.53 81.18h-14.7a2 2 0 0 1-2-2A34.79 34.79 0 0 0 2.08 44.43a2 2 0 0 1-2-2v-14.7a2 2 0 0 1 2-2 53.51 53.51 0 0 1 53.45 53.45 2 2 0 0 1-2 2zm-12.75-4h10.71A49.51 49.51 0 0 0 4.08 29.77v10.71a38.8 38.8 0 0 1 36.7 36.7z"
            />
            <path
              d="M79.25 81.18H64.56a2 2 0 0 1-2-2A60.55 60.55 0 0 0 2.08 18.7a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2 79.26 79.26 0 0 1 79.17 79.18 2 2 0 0 1-2 2zm-12.72-4h10.7A75.26 75.26 0 0 0 4.08 4v10.7a64.56 64.56 0 0 1 62.45 62.48z"
            />
          </svg>
        </span>
      </a>
    </div>
    <transition name="fade-modal">
      <div
        v-if="showSuccessModal"
        class="modal show"
        tabindex="-1"
        role="dialog"
        style="display:block"
      >
        <div role="document" class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="embed-responsive embed-responsive-1by1">
              <div class="embed-responsive-item">
                <video
                  v-if="!videoEnded"
                  @ended="onVideoEnded"
                  muted
                  autoplay
                  src="/img/success-rocket.mp4"
                />
                <div v-else class="modal-body text-center">
                  <button
                    @click="toggleModal(false)"
                    type="button"
                    class="close"
                    data-dismiss="modal"
                    aria-label="Close"
                  >
                    <span aria-hidden="true">&times;</span>
                  </button>
                  <h2>Hvala!</h2>
                  <p>Sporočilo poslano na e-naslov!</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </transition>
    <transition name="fade-backdrop">
      <div v-if="showSuccessModal" class="modal-backdrop show" />
    </transition>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loading: false,
      email: '',
      showSuccessModal: false,
      videoEnded: false,
    };
  },
  beforeDestroy() {
    this.toggleModal(false);
  },
  methods: {
    toggleModal(show = !this.showSuccessModal) {
      if (typeof window !== 'undefined' && document.body.classList) {
        if (show) {
          document.body.classList.add('modal-open');
        } else {
          document.body.classList.remove('modal-open');
        }
      }
      this.showSuccessModal = show;
      this.videoEnded = false;
    },
    async onSubscribe(event) {
      if (!this.loading && this.email && this.email.includes('@')) {
        this.loading = true;
        try {
          const response = await this.$axios.$get(
            'https://spam.djnd.si/deliver-email/',
            {
              params: {
                email: this.email,
              },
            },
          );
          // axios can return a number, so cast to string just in case
          if (String(response) === '1') {
            await this.toggleModal(true);
          }
        } catch {
        } finally {
          this.loading = false;
        }
      }
    },
    onVideoEnded(event) {
      this.videoEnded = true;
    },
  },
};
</script>

<style lang="scss" scoped>
.agrument-subscribe-bar {
  padding: 1rem $content-mobile-padding 1.2rem;

  @include media-breakpoint-up(xl) {
    padding: 0.75rem 3rem;
  }

  .bar-container {
    display: flex;
    justify-content: space-between;
    flex-direction: column;

    @include media-breakpoint-up(xl) {
      flex-direction: row;
    }

    .form-inline {
      flex-direction: column;
      align-items: initial;

      @include media-breakpoint-up(xl) {
        flex-direction: row;
        align-items: center;
      }

      strong {
        font-weight: 600;
      }

      .description {
        line-height: 1.25;
        margin-bottom: 0.25rem;

        @include media-breakpoint-up(xl) {
          margin: 0 0.75rem 0 0.5rem;
        }
      }

      .email-controls {
        width: 100%;

        @include media-breakpoint-up(xl) {
          width: auto;
        }

        .rss {
          margin-left: auto;
        }

        .form-group {
          flex: 1 0 auto;

          @include media-breakpoint-up(lg) {
            max-width: 300px;
          }

          .form-control {
            width: 100%;
          }
        }
      }
    }

    .btn {
      text-transform: uppercase;
      font-weight: 600;
      width: 100px;

      .lds-dual-ring {
        margin-top: -0.25rem;
        margin-bottom: -0.25rem;

        &,
        &::after {
          width: 1.25em;
          height: 1.25em;
          border-color: #fff transparent #fff transparent;
          border-width: 2px;
        }
      }

      &.rss {
        width: 80px;
        flex-shrink: 0;

        @include media-breakpoint-up(lg) {
          align-self: flex-end;
        }
      }

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
}

.modal {
  .modal-content {
    video {
      object-fit: cover;
    }

    .modal-body {
      display: flex;
      flex-direction: column;
      height: 100%;
      justify-content: center;

      .close {
        position: absolute;
        right: 0;
        top: 0;
        font-size: 2rem;
        opacity: 1;
        color: #333;
        width: 2rem;
        height: 2rem;
        line-height: 1;
        display: inline-block;
        overflow: hidden;
      }

      h2 {
        font-size: 3rem;
        font-weight: 200;
      }

      p {
        font-size: 1.5rem;
        font-weight: 200;
      }
    }
  }
}

// transition styles
.fade-backdrop-enter-active,
.fade-backdrop-leave-active {
  transition: opacity 0.15s linear;
}
.fade-backdrop-leave-active {
  transition-delay: 0.15s;
}
.fade-backdrop-enter,
.fade-backdrop-leave-to {
  opacity: 0;
}
.fade-modal-enter-active,
.fade-modal-leave-active {
  transition: opacity 0.15s linear;
}
.fade-modal-enter-active {
  transition-delay: 0.15s;
}
.fade-modal-enter,
.fade-modal-leave-to {
  opacity: 0;
}
</style>
