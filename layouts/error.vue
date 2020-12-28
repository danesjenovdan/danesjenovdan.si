<template>
  <div>
    <page-title :title="'Error'" :text="JSON.stringify(error)" />
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
  layout: 'default',
  props: {
    error: {
      type: Object,
      default: () => ({}),
    },
  },
};
</script>
