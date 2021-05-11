<template>
  <div>
    <page-title
      :title="$t('menu.tools')"
      :text="$t('tools.description')"
      color="warning"
    />
    <div class="row">
      <div v-for="tool in tools" :key="tool.id" class="col-12">
        <tool-tile
          :icon="tool.id"
          :alt="tool.alt"
          :title="$t(`tools.tools.${tool.id}.title`)"
          :description="$t(`tools.tools.${tool.id}.description`)"
          :paragraphs="$t(`tools.tools.${tool.id}.paragraphs`)"
          :links="tool.links"
          :email="{
            address: tool.email,
            label: $t(`tools.tools.${tool.id}.contact`),
            subject: $t(`tools.tools.${tool.id}.email-subject`),
          }"
        />
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';
import ToolTile from '~/components/ToolTile.vue';
import toolsJson from '~/assets/tools.json';

export default {
  pageColor: 'warning',
  nuxtI18n: {
    paths: {
      sl: '/orodja',
      en: '/tools',
    },
  },
  components: {
    PageTitle,
    ToolTile,
  },
  data() {
    return {
      tools: toolsJson.tools,
    };
  },
  head() {
    return {
      title: this.$t('menu.tools'),
    };
  },
};
</script>
