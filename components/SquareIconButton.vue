<template>
  <a
    :href="href"
    :class="[
      'square-icon-button',
      `square-icon-button--white`,
      'icon',
      `square-icon-${icon}--white`,
    ]"
    :style="{ 'background-color': `${color}` }"
    target="_blank"
    rel="noopener noreferrer"
  />
</template>

<script>
export default {
  props: {
    color: {
      type: String,
      default: 'primary',
    },
    icon: {
      type: String,
      required: true,
    },
    href: {
      type: String,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.square-icon-button {
  width: 150px;
  height: 150px;
  border-radius: 0;
  border: none;
  margin: 0 0.5rem;
  transition: all 0.15s ease;

  padding: 40px;
  background-size: 50%;

  &:hover {
    transform: scale(0.95);
  }

  &.square-icon-facebook--white {
    background-size: 25%;
  }
}
</style>
