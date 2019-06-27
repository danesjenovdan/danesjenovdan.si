<template>
  <div class="filter">
    <button
      class="filter__title icon-arrow--dark"
      :tabindex="titleTabIndex"
      @click="dropdownOpen = !dropdownOpen"
      v-text="title"
    />
    <div :class="['filter__options', { open: dropdownOpen }]">
      <div v-for="item in value" :key="`type-${item.id}`" class="custom-control custom-checkbox">
        <input
          :id="`type-${item.id}`"
          v-model="item.active"
          type="checkbox"
          class="custom-control-input"
          @change="toggleItem($event, item.id)"
        >
        <label :for="`type-${item.id}`" class="custom-control-label" v-text="item.label"/>
      </div>
    </div>
  </div>
</template>

<script>
import resize from '~/mixins/resize.js';

export default {
  mixins: [resize],
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
  },
};
</script>

<style lang="scss" scoped>
.filter {
  flex: 1;
  padding: 0 0 0 2.5rem;

  @include media-breakpoint-up(md) {
    padding: 0 1.5rem;
  }

  .filter__title {
    display: block;
    width: 100%;
    text-align: left;
    font-weight: 700;
    background-color: transparent;
    border: 1px solid #333;
    padding: 0.25rem 0.75rem;
    margin-bottom: 1rem;
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
    display: none;

    &.open {
      display: block;
    }

    @include media-breakpoint-up(md) {
      display: block;
    }

    .custom-control {
      padding-left: 2rem;
      margin-bottom: 1rem;

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
