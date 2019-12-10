<template>
  <button
    :class="[
      'donation-option',
      { 'donation-option--selected': donationPreset.selected },
    ]"
    @click.prevent="$emit('select')"
    type="button"
  >
    <div class="donation-option__content">
      <div class="donation-option__amount">
        <div v-if="donationPreset.custom" class="custom-amount">
          <input
            id="custom-amount"
            v-model="donationPreset.amount"
            type="number"
            class="form-control"
          />
          <label for="custom-amount">€</label>
        </div>
        <span v-else>{{ donationPreset.amount }} €</span>
      </div>
      <div class="donation-option__description">
        {{ donationPreset.description }}
      </div>
    </div>
    <div class="donation-option__icon">
      <div class="icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 95 95">
          <path
            d="M47.9 1.6a44.3 44.3 0 100 88.5 44.3 44.3 0 000-88.5z"
            fill="none"
            stroke="currentColor"
            stroke-width="6"
          />
          <path
            d="M72.9 35.7L40 68.7a1.4 1.4 0 01-2 0L18.6 49a1.4 1.4 0 010-2l6.8-6.8c.3-.2.6-.4 1-.4s.7.2 1 .5L39.2 52l25-25c.6-.6 1.4-.6 2 0l6.8 6.8a1.4 1.4 0 010 2z"
            fill="none"
            stroke="currentColor"
            stroke-width="6"
          />
        </svg>
      </div>
    </div>
  </button>
</template>

<script>
export default {
  props: {
    donationPreset: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.donation-option {
  display: flex;
  align-items: stretch;
  width: 100%;
  padding: 1rem 1.25rem;
  margin-bottom: 1.5rem;
  text-align: left;
  border: 2px solid rgba($color-red, 0.2);
  background-color: transparent;
  background-image: linear-gradient(
    to right,
    rgba($color-yellow, 0.2) 0%,
    rgba($color-red, 0.2) 100%
  );

  &:focus {
    border: 2px solid $color-red !important;
    outline: none !important;
  }

  &.donation-option--selected {
    border: 2px solid rgba($color-red, 1);
    background-image: linear-gradient(
      to right,
      rgba($color-yellow, 1) 0%,
      rgba($color-red, 1) 100%
    );
  }

  .donation-option__content {
    flex: 1;

    .donation-option__amount {
      font-size: 2rem;
      font-weight: 600;
      line-height: 1;

      .custom-amount {
        margin-top: 0.5rem;
        position: relative;
        width: 75%;

        .form-control {
          background-color: transparent;
          font-size: 1.75rem;
          font-weight: 600;
          font-style: normal;
          color: inherit;
          padding-right: 1.75rem;
        }

        label {
          position: absolute;
          top: 0.7rem;
          right: 0.5rem;
          font-size: 2rem;
        }
      }
    }

    .donation-option__description {
      font-size: 1rem;
      font-weight: 300;
      font-style: italic;
      margin-top: 0.5rem;
    }
  }

  .donation-option__icon {
    display: flex;
    align-items: center;

    .icon {
      width: 2.5rem;
      color: mix($color-red, #fff, 70%);

      svg {
        width: 100%;
        height: 100%;
      }
    }
  }
}
</style>
