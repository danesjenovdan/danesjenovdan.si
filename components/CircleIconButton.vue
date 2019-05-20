<template>
  <a
    :href="href"
    target="_blank"
    rel="noopener noreferrer"
    :class="['circle-icon-button', 'icon', `icon-${icon}--${color}`]"
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
.circle-icon-button {
  width: 4rem;
  height: 4rem;
  border-radius: 50%;
  background-color: transparent;
  border: none;
  margin: 0 0.5rem;

  @include media-breakpoint-up(xl) {
    width: 2.5rem;
    height: 2.5rem;
  }
}
</style>
