<template>
  <div class="person-tile bg-white">
    <div
      :style="`background-image: url('/img/people/${person.id}.jpg')`"
      class="person-tile__image"
    />
    <div
      :style="`background-image: url('/img/people/${person.id}_hover.jpg')`"
      class="person-tile__image-hover"
    />
    <div class="person-tile__content">
      <h1 v-text="person.name" class="person-tile__name" />
      <div class="person-tile__text">
        <a
          v-if="person.mail"
          :href="`mailto:${person.mail}`"
          v-text="person.mail"
          class="person-tile__email"
        />
        <span v-else class="person-tile__email">&nbsp;</span>
        <p v-t="`people.people.${person.id}.description`" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    person: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.person-tile {
  position: relative;
  width: 100%;

  &:hover {
    .person-tile__image-hover {
      opacity: 1;
    }
  }

  .person-tile__image,
  .person-tile__image-hover {
    width: 100%;
    height: 0;
    padding-top: 100%;
    position: relative;
    background-size: cover;
    background-position: center;
    background-color: #fff;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;

    &::after {
      content: '';
      width: 0px;
      height: 0px;
      border-style: solid;
      border-width: 0 20px 20px 20px;
      border-color: transparent transparent #ffffff transparent;
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
    }
  }

  .person-tile__image-hover {
    position: absolute;
    top: 0;
    left: 0;
    opacity: 0;
  }

  .person-tile__content {
    padding: 2rem;

    .person-tile__name {
      font-size: 1.25rem;
      font-weight: 600;
      text-transform: uppercase;
      text-align: center;
      margin: 0;
    }

    .person-tile__text {
      font-size: 1.4rem;
      font-weight: 200;
      line-height: 1.2;
      text-align: center;

      .person-tile__email {
        display: inline-block;
        font-size: 0.9rem;
        margin-bottom: 0.75rem;
        font-weight: 300;
        text-decoration: underline;
        color: inherit;

        &:hover {
          text-decoration: none;
        }
      }

      span.person-tile__email {
        text-decoration: none;
      }

      p {
        margin: 0;
      }
    }
  }
}
</style>
