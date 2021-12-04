<template>
  <div class="problem-tile">
    <div class="header">
      <h1>{{ title }}</h1>
      <img v-if="icon" :src="imgSrc" />
    </div>
    <p>{{ description }}</p>
  </div>
</template>

<script>
export default {
  name: 'ProblemTile',

  props: {
    title: {
      required: true,
      type: String,
      default: 'Naslov',
    },
    description: {
      required: true,
      type: String,
      default: 'Some description text that is long',
    },
    icon: {
      required: false,
      type: String,
      default: null,
    },
  },

  computed: {
    imgSrc() {
      return require(`../static/icons/donations/${this.icon}`);
    },
  },
};
</script>

<style lang="scss">
.problem-tile {
  border-style: solid;
  border-width: 3px;
  border-image-source: linear-gradient(to bottom, #cdac54 0%, #df786c 100%);
  border-image-slice: 1;
  padding: 38px;
  margin-bottom: 57px;

  .header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
  }

  img {
    max-width: 80px;
    max-height: 80px;
  }

  h1 {
    color: #333333;
    font-size: 40px;
    font-weight: 600;
    font-style: italic;
    letter-spacing: normal;
    line-height: 50px;
    text-align: left;

    @include media-breakpoint-down(sm) {
      font-size: 25px;
      line-height: 30px;
    }
  }

  p {
    color: #333333;
    font-size: 20px;
    font-weight: 300;
    font-style: normal;
    letter-spacing: normal;
    line-height: 26.67px;
    text-align: left;
  }
}
</style>
