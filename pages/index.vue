<template>
  <b-container>
    <div>
      {{ $t('welcome') }}
    </div>
  </b-container>
</template>

<script>
// import Logo from '~/components/Logo.vue'

export default {
  nuxtI18n: {
    paths: {
      sl: '/domov',
      en: '/home',
    },
  },
  components: {
    // Logo
  },
};
</script>

<style>
</style>
