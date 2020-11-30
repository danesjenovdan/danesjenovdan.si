<template>
  <div class="problem-tile">
    <h1>{{ title }}</h1>
    <p>{{ description }}</p>
  </div>
</template>

<script>
export default {
  name: 'ProblemTile',

  props: {
    title: {
      required: true,
      default: 'Naslov',
    },
    description: {
      required: true,
      default: 'Some description text that is long',
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

  h1 {
    color: #333333;
    font-size: 40px;
    font-weight: 500;
    font-style: italic;
    letter-spacing: normal;
    line-height: 50px;
    text-align: left;
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
