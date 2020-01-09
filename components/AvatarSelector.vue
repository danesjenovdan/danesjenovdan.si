<template>
  <div class="avatar-selector">
    <div ref="presetScroller" class="preset-scroller">
      <div class="arrow-top"></div>
      <div class="arrow-bottom"></div>
      <div class="images-container">
        <div
          :style="{ transform: `translateX(${imagesOffset}px)` }"
          class="images"
        >
          <button
            v-for="(avatar, i) in avatars"
            :key="avatar.image"
            :class="['avatar-image', { selected: i === selectedIndex }]"
            :style="{ backgroundImage: `url('${avatar.image}')` }"
            type="button"
            @click="selectedIndex = i"
          ></button>
        </div>
      </div>
    </div>
    <div class="select-file">
      <div class="custom-file">
        <input id="customFile" type="file" class="custom-file-input" />
        <label class="custom-file-label" for="customFile"
          >naloži sliko s svojega računalnika</label
        >
      </div>
      <client-only placeholder="Loading...">
        <avatar-cropper
          :labels="{ submit: 'Izberi', cancel: 'Prekliči' }"
          :upload-handler="handleUpload"
          :cropper-options="{
            background: false,
            aspectRatio: 1,
            autoCropArea: 1,
            viewMode: 0,
            movable: false,
            zoomable: false,
            dragMode: 'move',
          }"
          trigger="#customFile"
        />
      </client-only>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    const avatars = [
      {
        image: '/img/avatars/avatar_dinosaur.png',
      },
      {
        image: '/img/avatars/avatar_ninja.png',
      },
      {
        image: '/img/avatars/avatar_astronaut.png',
      },
      {
        image: '/img/avatars/avatar_icecream.png',
      },
      {
        image: '/img/avatars/avatar_ghost.png',
      },
      {
        image: '/img/avatars/avatar_gift.png',
      },
    ];
    return {
      selectedIndex: -1,
      avatars,
    };
  },
  computed: {
    imagesOffset() {
      // average of (big image + margin) and (small image + margin) + 8 (no idea why)
      let avg = (80 + 12 + 64 + 12 + 8) / 2;
      const ps = this.$refs.presetScroller;
      if (ps && ps.clientHeight > 150) {
        avg = (128 + 16 + 104 + 16 + 8) / 2;
      }

      // this shifts 0...x indexes to -x/2...x/2 with 0 in the middle
      let shifted = this.selectedIndex - Math.floor(this.avatars.length / 2);
      if (this.avatars.length % 2 === 0) {
        // even number of avatars means center is between 2 avatars, so move over by half
        shifted += 0.5;
      }
      return shifted * avg * -1;
    },
  },
  watch: {
    selectedIndex(newVal) {
      const selectedAvatar = this.avatars[newVal];
      if (!selectedAvatar.blob) {
        const that = this;
        const img = new Image();
        const c = document.createElement('canvas');
        const ctx = c.getContext('2d');
        img.onload = function() {
          c.width = this.naturalWidth; // update canvas size to match image
          c.height = this.naturalHeight;
          ctx.drawImage(this, 0, 0); // draw in image
          c.toBlob(
            function(blob) {
              selectedAvatar.blob = blob;
              that.$emit('change', selectedAvatar.blob);
            },
            'image/jpeg',
            0.7,
          );
        };
        img.src = selectedAvatar.image;
      } else {
        this.$emit('change', selectedAvatar.blob);
      }
    },
  },
  mounted() {
    // force recalculation of offset when we have dom
    this.selectedIndex = Math.floor(this.avatars.length / 2) - 1;
  },
  methods: {
    handleUpload(cropper) {
      // TODO: use to blob and toblob polyfill
      cropper
        .getCroppedCanvas({
          width: 400,
          height: 400,
          maxWidth: 2048,
          maxHeight: 2048,
          fillColor: '#fff',
        })
        .toBlob(
          (blob) => {
            const blobUrl = URL.createObjectURL(blob);
            this.avatars.push({
              image: blobUrl,
              blob,
            });
            this.selectedIndex = this.avatars.length - 1;
          },
          'image/jpeg',
          0.7,
        );
    },
  },
};
</script>

<style lang="scss" scoped>
.avatar-selector {
  @include media-breakpoint-up(md) {
    max-width: 750px;
    margin: 0 auto;
  }

  .preset-scroller {
    margin: 0 -1.5rem;
    height: 8rem;
    background-image: linear-gradient(
      to right,
      rgba($color-yellow, 0.7) 0%,
      rgba($color-red, 0.7) 100%
    );
    position: relative;

    @include media-breakpoint-up(md) {
      height: 12rem;
    }

    .arrow-top,
    .arrow-bottom {
      position: absolute;
      left: 50%;
      top: -0.5rem;
      transform: translateX(-50%);
      border-style: solid;
      border-width: 1.25rem 0.75rem 0 0.75rem;
      border-color: $color-red transparent transparent transparent;
    }

    .arrow-bottom {
      top: auto;
      bottom: -0.5rem;
      border-width: 0 0.75rem 1.25rem 0.75rem;
      border-color: transparent transparent $color-red transparent;
    }

    .images-container {
      display: flex;
      justify-content: center;
      overflow: hidden;
      max-width: 100vw;
      height: 100%;

      .images {
        display: flex;
        height: 100%;
        align-items: center;
        justify-content: center;
        transition: transform 0.25s ease;

        .avatar-image {
          width: 4rem;
          height: 4rem;
          border: none;
          background-color: #fff;
          background-size: 100% 100%;
          background-position: center center;
          background-repeat: no-repeat;
          margin: 0 0.75rem;
          padding: 0;

          @include media-breakpoint-up(md) {
            width: 6.5rem;
            height: 6.5rem;
            margin: 0 1rem;
          }

          &:focus {
            outline: 0;
          }

          &.selected {
            width: 5rem;
            height: 5rem;
            border: 2px solid $color-red;

            @include media-breakpoint-up(md) {
              width: 8rem;
              height: 8rem;
            }
          }
        }
      }
    }
  }

  .select-file {
    margin-top: 1.5rem;

    .custom-file {
      // width: 400px;
      margin: 0 auto;
      display: block;

      @include media-breakpoint-up(md) {
        // width: 600px;
        height: 3rem;
      }

      .custom-file-label {
        border: none;
        background: transparent;
        text-align: center;
        font-weight: 600;
        font-style: italic;
        text-decoration: underline;

        @include media-breakpoint-up(md) {
          font-size: 1.5rem;
          height: 3rem;
        }

        &::after {
          display: none;
        }
      }
    }
  }

  .avatar-cropper /deep/ {
    .avatar-cropper-mark {
      background-color: rgba(#000, 0.5);

      .avatar-cropper-close {
        display: none;
      }
    }

    .cropper-view-box {
      outline: 1px solid $color-red;
      outline-color: rgba($color-red, 0.75);
      background-color: #fff;
    }

    .cropper-line,
    .cropper-point {
      background-color: $color-red;
    }

    .avatar-cropper-btn:hover {
      background-color: $color-red;
    }
  }
}
</style>
