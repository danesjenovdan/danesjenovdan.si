<template>
  <div class="donation-info-box justify-content-center">
    <span :class="['icon', `icon-section-${icon}--black`]"></span>
    <p>{{ text }}</p>
  </div>
</template>

<script>
export default {
  name: 'DonationInfoBox',

  props: {
    icon: {
      type: String,
      required: true,
      default: 'agrument',
    },
    text: {
      type: String,
      required: true,
      default: 'agrument',
    },
  },
};
</script>

<style lang="scss" scoped>
.donation-info-box {
  margin: 15px;

  width: 280px;
  height: 280px;
  max-width: 280px;
  max-height: 280px;
  position: relative;
  display: flex;
  flex-wrap: wrap;
  padding: 20px;

  .icon {
    display: block;
    min-width: 100%;
    height: 100px;
    margin-top: 25px;
  }

  p {
    width: 100%;
    text-align: center;
    font-style: italic;
    font-size: 22px;
    font-weight: 600;
    line-height: 30px;
    padding: 13px;
  }

  &::before {
    content: '';
    width: 100%;
    height: 100%;
    display: block;
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background-image: linear-gradient(to right, #cdac54 0%, #df786c 100%);
    opacity: 0.2;
  }
}
</style>
