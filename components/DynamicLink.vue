<template>
  <nuxt-link
    v-if="shouldUseNuxtLink"
    v-bind="$attrs"
    :to="to"
    v-on="{ ...$listeners, click: onClick }"
  >
    <slot />
  </nuxt-link>
  <a
    v-else
    v-bind="$attrs"
    :href="to"
    :target="isLinkExternal ? '_blank' : null"
    :rel="isLinkExternal ? 'noopener noreferrer' : null"
    v-on="{ ...$listeners, click: onClick }"
  >
    <slot />
  </a>
</template>

<script>
export default {
  props: {
    to: {
      type: String,
      default: '',
    },
  },
  computed: {
    isLinkEmpty() {
      return !this.to || this.to === '#';
    },
    isLinkExternal() {
      return !this.isLinkEmpty && /^https?:\/\//.test(this.to);
    },
    shouldUseNuxtLink() {
      return !this.isLinkEmpty && !this.isLinkExternal;
    },
  },
  methods: {
    onClick(event) {
      if (this.isLinkEmpty) {
        event.preventDefault();
      }
      this.$emit('click', event);
    },
  },
};
</script>
