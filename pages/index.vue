<template>
  <div>
    <div class="row">
      <div class="col-12">
        <section-header text="Agrument" icon="keyboard"/>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <section-header text="Pojavljanja" icon="keyboard"/>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <section-header text="Akcije" color="secondary" icon="keyboard"/>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <section-header text="Videogalerija" color="warning" icon="keyboard"/>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <section-header text="Orodja" color="warning" icon="keyboard"/>
      </div>
    </div>
  </div>
</template>

<script>
import SectionHeader from '~/components/SectionHeader.vue';

export default {
  components: {
    SectionHeader,
  },
};
</script>

<style>
</style>
