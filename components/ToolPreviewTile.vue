<template>
  <nuxt-link :to="localePath('tools')" class="tool-tile bg-white">
    <div class="row">
      <div class="left-col">
        <div class="d-flex flex-column justify-content-center h-100">
          <div class="d-flex align-items-center flex-column">
            <div
              :style="{ 'background-image': `url(/icons/tools/${icon}.svg` }"
              class="icon"
            />
            <div class="title d-flex flex-column">
              <h2 v-text="title" />
              <h3 v-text="text" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </nuxt-link>
</template>

<script>
export default {
  props: {
    icon: {
      type: String,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    text: {
      type: String,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.tool-tile {
  padding: 2.5rem 2rem;
  margin-bottom: 2rem;
  position: relative;
  display: block;
  text-decoration: none;
  color: inherit;

  .left-col {
    .icon {
      flex-shrink: 0;
      margin-bottom: 1.25rem;
      width: 100px;
      height: 100px;
    }

    .title {
      h2,
      h3 {
        padding: 0 1rem;
      }

      h2 {
        font-size: 2rem;
        font-weight: 600;
        text-align: center;
      }

      h3 {
        font-size: 1.2rem;
        font-weight: 300;
        font-style: italic;
        text-align: center;
      }
    }
  }
}
</style>
