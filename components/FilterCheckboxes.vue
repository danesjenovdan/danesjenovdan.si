<template>
  <div v-click-outside="() => dropdownOpen = false" class="filter">
    <button
      class="filter__title icon-arrow--dark"
      :tabindex="titleTabIndex"
      @click="toggleDropdown"
      v-text="title"
    />
    <div
      ref="filterOptions"
      :class="['filter__options', { open: dropdownOpen }]"
      @focusout="onFocusOut"
    >
      <div v-for="item in value" :key="`type-${item.id}`" class="custom-control custom-checkbox">
        <input
          :id="`type-${item.id}`"
          v-model="item.active"
          type="checkbox"
          class="custom-control-input"
          @change="toggleItem($event, item.id)"
        />
        <label :for="`type-${item.id}`" class="custom-control-label" v-text="item.label" />
      </div>
    </div>
  </div>
</template>

<script>
import resize from '~/mixins/resize.js';
import clickOutside from '~/mixins/clickOutside.js';

export default {
  mixins: [resize, clickOutside],
  props: {
    title: {
      type: String,
      required: true,
    },
    value: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      dropdownOpen: false,
      titleTabIndex: 0,
    };
  },
  methods: {
    toggleDropdown() {
      this.dropdownOpen = !this.dropdownOpen;
      if (this.dropdownOpen) {
        // move focus to the first item
        this.$nextTick(() => {
          this.$refs.filterOptions.querySelector('input[type="checkbox"]').focus();
        });
      }
    },
    toggleItem(event, itemId) {
      const newItems = this.value.map(item => ({
        ...item,
        active: item.id === itemId ? event.target.checked : item.active,
      }));
      this.$emit('input', newItems);
    },
    onResize() {
      const w = window.innerWidth;
      this.titleTabIndex = w <= 767 ? 0 : -1;
    },
    onFocusOut(event) {
      if (event.relatedTarget && !event.currentTarget.contains(event.relatedTarget)) {
        this.dropdownOpen = false;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.filter {
  flex: 1;
  margin: 0 0 0 2.5rem;
  position: relative;

  @include media-breakpoint-up(md) {
    margin: 0 1.5rem;
  }

  .filter__title {
    display: block;
    width: 100%;
    text-align: left;
    font-weight: 700;
    background-color: transparent;
    border: 1px solid #333;
    padding: 0.25rem 0.75rem;
    margin-bottom: 0.75rem;
    background-repeat: no-repeat;
    background-position: right 10px center;
    background-size: 10px;

    @include media-breakpoint-up(md) {
      border: 0;
      padding: 0;
      margin-bottom: 1.25rem;
      background-image: none;
      pointer-events: none;
    }
  }

  .filter__options {
    border: 1px solid #333;
    padding: 0.75rem 0.75rem 0 0.75rem;
    margin-bottom: 0.75rem;
    margin-top: calc(-0.75rem - 1px);
    background: #fff;
    position: absolute;
    left: 0;
    right: 0;
    z-index: 1;
    display: none;

    &.open {
      display: block;
    }

    @include media-breakpoint-up(md) {
      border: 0;
      padding: 0.5rem 0 0 0;
      margin-bottom: 0;
      display: block;
      position: static;
    }

    .custom-control {
      padding-left: 2rem;
      margin-bottom: 0.75rem;

      @include media-breakpoint-up(md) {
        margin-bottom: 1rem;
      }

      .custom-control-label {
        font-size: 1rem;
        font-weight: 300;
        line-height: 1.5rem;
      }

      .custom-control-label::before,
      .custom-control-label::after {
        width: 1.5rem;
        height: 1.5rem;
        top: 0;
        left: -2rem;
      }

      .custom-control-label::before {
        border-color: #333;
      }
    }
  }
}
</style>
