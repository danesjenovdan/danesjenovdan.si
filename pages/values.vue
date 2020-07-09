<template>
  <div>
    <page-title
      :title="$t('menu.values')"
      :text="$t('values.description')"
      color="warning"
    />
    <div class="row">
      <div v-for="value in values" :key="value.id" class="col-12">
        <value-tile
          :icon="`value-${value.id}`"
          :title="$t(`values.values.${value.id}.title`)"
          :description="$t(`values.values.${value.id}.description`)"
        />
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';
import ValueTile from '~/components/ValueTile.vue';
import valuesJson from '~/assets/values.json';

export default {
  pageColor: 'warning',
  nuxtI18n: {
    paths: {
      sl: '/vrednote',
      en: '/ethics',
    },
  },
  components: {
    PageTitle,
    ValueTile,
  },
  data() {
    return {
      values: valuesJson.values,
    };
  },
  head() {
    return {
      title: this.$t('menu.values'),
    };
  },
};
</script>
