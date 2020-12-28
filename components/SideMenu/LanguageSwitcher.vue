<template>
  <div class="language-switcher">
    <i class="icon icon-language--dark" />
    <select
      class="form-control custom-select icon-dropdown-arrow--dark"
      @change="onLocaleChange"
    >
      <option
        v-for="locale in $i18n.locales"
        :key="locale.code"
        :value="locale.code"
        :selected="locale.code === $i18n.locale"
      >
        {{ locale.name }}
      </option>
    </select>
  </div>
</template>

<script>
export default {
  methods: {
    onLocaleChange(event) {
      const locale = this.$i18n.locales[event.target.selectedIndex];
      this.$router.push(this.switchLocalePath(locale.code));
    },
  },
};
</script>

<style lang="scss" scoped>
.language-switcher {
  display: flex;
  align-items: center;

  .icon {
    display: inline-block;
    width: 1.125rem;
    height: 1.125rem;
    margin-right: 0.5rem;
  }

  .custom-select {
    display: inline-block;
    width: auto;
    background-color: transparent;
    background-position: right 0.25rem top 60%;
    background-size: 0.5rem 0.5rem;
    background-repeat: no-repeat;
    font-style: normal;
    font-weight: 300;
    font-size: 1.1rem;
    padding: 0 1.25rem 0 0.25rem;
    line-height: 1.4;
    height: 1.75rem;

    &:not(:focus) {
      border: 0;
    }

    option {
      font-weight: 300;
      font-size: 1rem;
    }
  }
}
</style>
