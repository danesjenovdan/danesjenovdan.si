<template>
  <div>
    <page-title :title="'Error'" :text="error" />
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';

//                                                                            //
//             WARNING: this is treated as a page, not a layout!              //
//                                                                            //

export default {
  components: {
    PageTitle,
  },
  props: {
    error: {
      type: Object,
      default: () => ({}),
    },
  },
};
</script>
