<template>
  <div>
    <page-title :title="$t('support.title')" :text="$t('support.description')" color="primary" />
    <div class="support-drawing">
      <img src="/img/support-drawing.png" alt="support drawing" />
    </div>
    <div class="section-header-container">
      <section-header text="Oglej si video!" />
    </div>
    <div class="embed-responsive embed-responsive-16by9">
      <div class="embed-responsive-item d-flex align-items-center">
        <iframe
          src="https://player.vimeo.com/video/92594621"
          allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
        />
      </div>
    </div>
    <div class="section-header-container">
      <section-header text="Podpri projekt!" />
    </div>
    <progress-rocket />
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';
import SectionHeader from '~/components/SectionHeader.vue';
import ProgressRocket from '~/components/ProgressRocket.vue';

export default {
  pageColor: 'primary',
  components: {
    PageTitle,
    SectionHeader,
    ProgressRocket,
  },
};
</script>

<style lang="scss" scoped>
.support-drawing {
  img {
    width: 100%;
    max-width: 100%;
  }
}

.section-header-container {
  padding-top: 3rem;
  padding-right: 0.75rem;
  padding-bottom: 1.5rem;
  text-align: center;

  .section-header {
    font-size: 1.5rem;
  }
}
</style>
