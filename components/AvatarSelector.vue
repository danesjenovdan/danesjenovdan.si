<template>
  <div class="avatar-selector">
    <div class="preset-scroller">
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
            @click="selectedIndex = i"
            type="button"
          ></button>
        </div>
      </div>
    </div>
    <div class="select-file">
      <div class="custom-file">
        <input id="customFile" type="file" class="custom-file-input" />
        <label class="custom-file-label" for="customFile"
          >naloži svojo fotko</label
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
        image: '/avatars/avatar_dinosaur.svg',
      },
      {
        image: '/avatars/avatar_ninja.svg',
      },
      {
        image: '/avatars/avatar_astronaut.svg',
      },
      {
        image: '/avatars/avatar_icecream.svg',
      },
      {
        image: '/avatars/avatar_ghost.svg',
      },
    ];
    return {
      selectedIndex: Math.floor(avatars.length / 2),
      avatars,
    };
  },
  computed: {
    imagesOffset() {
      // average of (big image + margin) and (small image + margin) + 8 (no idea why)
      const avg = (80 + 12 + 64 + 12 + 8) / 2;
      // this shifts 0...x indexes to -x/2...x/2 with 0 in the middle
      let shifted = this.selectedIndex - Math.floor(this.avatars.length / 2);
      if (this.avatars.length % 2 === 0) {
        // even number of avatars means center is between 2 avatars, so move over by half
        shifted += 0.5;
      }
      return shifted * avg * -1;
    },
  },
  methods: {
    handleUpload(cropper) {
      // TODO: use to blob and toblob polyfill
      const userAvatar = cropper
        .getCroppedCanvas({
          width: 400,
          height: 400,
          maxWidth: 2048,
          maxHeight: 2048,
          fillColor: '#fff',
        })
        .toDataURL('image/jpeg', 0.7);
      this.avatars.push({
        image: userAvatar,
      });
      this.selectedIndex = this.avatars.length - 1;
    },
  },
};
</script>

<style lang="scss" scoped>
.avatar-selector {
  .preset-scroller {
    margin: 0 -1.5rem;
    height: 8rem;
    background-image: linear-gradient(
      to right,
      rgba($color-yellow, 0.7) 0%,
      rgba($color-red, 0.7) 100%
    );
    position: relative;

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

          &:focus {
            outline: 0;
          }

          &.selected {
            width: 5rem;
            height: 5rem;
            border: 2px solid $color-red;
          }
        }
      }
    }
  }

  .select-file {
    margin-top: 2rem;

    .custom-file {
      width: 200px;
      margin: 0 auto;
      display: block;

      .custom-file-label {
        border: none;
        background: transparent;
        text-align: center;
        font-weight: 600;
        font-style: italic;
        text-decoration: underline;

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
  }
}
</style>
