<template>
  <a
    :href="href"
    target="_blank"
    rel="noopener noreferrer"
    :class="['circle-icon-button', `circle-icon-button--${color}`, 'icon', `icon-${icon}--${color}`]"
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
  width: 3.5rem;
  height: 3.5rem;
  border-radius: 50%;
  background-color: transparent;
  border: none;
  margin: 0 0.5rem;
  transition: all 0.15s ease;

  &:hover {
    transform: scale(0.95);
  }
}
</style>
