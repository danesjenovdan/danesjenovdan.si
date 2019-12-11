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
            v-for="i in 5"
            :key="i"
            :class="['avatar-image', { selected: i === selectedIndex }]"
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
        <img :src="userAvatar" alt="" />
        <avatar-cropper
          :labels="{ submit: 'Izberi', cancel: 'Prekliči' }"
          :upload-handler="handleUpload"
          trigger="#customFile"
        />
      </client-only>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedIndex: 3,
      userAvatar: undefined,
      showCropper: true,
      imagesOffset: 0,
    };
  },
  watch: {
    selectedIndex(newValue) {
      // average of (big image + margin) and (small image + margin) + 8 (no idea why)
      const avg = (80 + 12 + 64 + 12 + 8) / 2;
      const centerIndex = newValue - 3;
      this.imagesOffset = centerIndex * avg * -1;
      console.log(this.imagesOffset);
    },
  },
  methods: {
    handleUpload(cropper) {
      // TODO: use to blob and toblob polyfill
      this.userAvatar = cropper
        .getCroppedCanvas({
          width: 200,
          height: 200,
          maxWidth: 2048,
          maxHeight: 2048,
        })
        .toDataURL('image/jpeg', 0.6);
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

        .avatar-image {
          width: 4rem;
          height: 4rem;
          border: none;
          background-color: #fff;
          background-size: 80% 80%;
          background-position: center bottom;
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

        .avatar-image:nth-of-type(1) {
          background-image: url('/avatars/avatar_dinosaur.svg');
        }
        .avatar-image:nth-of-type(2) {
          background-image: url('/avatars/avatar_ninja.svg');
        }
        .avatar-image:nth-of-type(3) {
          background-image: url('/avatars/avatar_astronaut.svg');
        }
        .avatar-image:nth-of-type(4) {
          background-image: url('/avatars/avatar_icecream.svg');
        }
        .avatar-image:nth-of-type(5) {
          background-image: url('/avatars/avatar_ghost.svg');
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
}
</style>
