<template>
  <div>
    <page-title
      title="Preusmerjamo ..."
      text="Kmalu te bomo preusmerili na datoteko s priročnikom."
      color="secondary"
    />
  </div>
</template>

<script>
/* global plausible */

import PageTitle from '~/components/PageTitle.vue';

export default {
  pageColor: 'secondary',
  nuxtI18n: {
    paths: {
      sl: '/prirocnik',
      en: '/prirocnik',
    },
  },
  components: {
    PageTitle,
  },
  head() {
    return {
      title: 'Priročnik',
    };
  },
  mounted() {
    plausible('Project', {
      props: {
        title: 'Priročnik Transparentna, dostopna in vključujoča občina',
        url: 'https://drive.google.com/file/d/1DV6T-6x62AkiAunPnX7r_IMmn9S8DsX3/view?usp=share_link',
      },
    });
    window.setTimeout(() => {
      document.location.href =
        'https://drive.google.com/file/d/1DV6T-6x62AkiAunPnX7r_IMmn9S8DsX3/view?usp=share_link';
    }, 1000);
  },
};
</script>

<style lang="scss" scoped>
.wrapping-flex-tiles {
  @include wrapping-flex-tiles($width: 300px, $width-xl: 345px);
}
</style>
