<template>
  <div :title="name" class="logo-box">
    <a
      :href="url"
      target="_blank"
      rel="noopener noreferrer"
      class="logo-box__content"
    >
      <img :src="image" :alt="`${name} logo`" />
    </a>
  </div>
</template>

<script>
export default {
  props: {
    image: {
      type: String,
      required: true,
    },
    url: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.logo-box {
  display: block;
  width: 100%;
  height: 0;
  padding-top: 100%;
  position: relative;
  background-color: #fff;

  .logo-box__content {
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    padding: 2rem;

    img {
      width: 100%;
      mix-blend-mode: darken;
      filter: grayscale(100%);
    }
  }
}
</style>
