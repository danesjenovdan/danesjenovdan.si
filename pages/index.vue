<template>
  <div>
    <page-title
      :title="$t('hello')"
      :text="$t('landing.description')"
    />
    <div class="row">
      <div class="col-12">
        <section-header :text="$t('menu.agrument')" icon="keyboard"/>
      </div>
    </div>
    <div>
      <div class="wrapping-flex-tiles">
        <div class="flex-tile">
          <preview-tile
            image="https://agrument.danesjenovdan.si/media/by_id/1411.jpg"
            title="O arhitekurnem prekariatu"
            byline="25. 3. 2019"
            text="Študenti ljubljanske Fakultete za arhitekturo so v javnem pismu opozorili, da jih profesorji izkoriščajo. Ti poleg ..."
          />
        </div>
        <div class="flex-tile">
          <preview-tile
            image="https://agrument.danesjenovdan.si/media/by_id/1411.jpg"
            title="O arhitekurnem prekariatu"
            byline="25. 3. 2019"
            text="Študenti ljubljanske Fakultete za arhitekturo so v javnem pismu opozorili, da jih profesorji izkoriščajo. Ti poleg ..."
          />
        </div>
        <div class="flex-tile">
          <preview-tile
            image="https://agrument.danesjenovdan.si/media/by_id/1411.jpg"
            title="O arhitekurnem prekariatu"
            byline="25. 3. 2019"
            text="Študenti ljubljanske Fakultete za arhitekturo so v javnem pismu opozorili, da jih profesorji izkoriščajo. Ti poleg ..."
          />
        </div>
        <div class="flex-tile">
          <preview-tile
            image="https://agrument.danesjenovdan.si/media/by_id/1411.jpg"
            title="O arhitekurnem prekariatu"
            byline="25. 3. 2019"
            text="Študenti ljubljanske Fakultete za arhitekturo so v javnem pismu opozorili, da jih profesorji izkoriščajo. Ti poleg ..."
          />
        </div>
        <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile"/>
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <more-button :to="localePath('agrument')" :text="$t('agrument.more')"/>
    </div>
    <div class="row">
      <div class="col-12">
        <section-header :text="$t('menu.clipping')" icon="keyboard"/>
      </div>
    </div>
    <div>
      <div class="wrapping-flex-tiles">
        <div class="flex-tile">
          <preview-tile
            image="https://www.dnevnik.si/i/as/2019/03/17/1166962.jpg"
            title="Filip Dobranić: Facebook je nevaren in škodljiv"
            byline="Dnevnik, 25. 3. 2019"
          />
        </div>
        <div class="flex-tile">
          <preview-tile
            image="https://www.dnevnik.si/i/as/2019/03/17/1166962.jpg"
            title="Filip Dobranić: Facebook je nevaren in škodljiv"
            byline="Dnevnik, 25. 3. 2019"
          />
        </div>
        <div class="flex-tile">
          <preview-tile
            image="https://www.dnevnik.si/i/as/2019/03/17/1166962.jpg"
            title="Filip Dobranić: Facebook je nevaren in škodljiv"
            byline="Dnevnik, 25. 3. 2019"
          />
        </div>
        <div class="flex-tile">
          <preview-tile
            image="https://www.dnevnik.si/i/as/2019/03/17/1166962.jpg"
            title="Filip Dobranić: Facebook je nevaren in škodljiv"
            byline="Dnevnik, 25. 3. 2019"
          />
        </div>
        <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile"/>
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <more-button :to="localePath('clipping')" :text="$t('clipping.more')"/>
    </div>
    <div class="row">
      <div class="col-12">
        <section-header :text="$t('menu.projects')" color="secondary" icon="keyboard"/>
      </div>
    </div>
    <div>
      <div class="wrapping-flex-tiles">
        <div class="flex-tile">
          <project-tile/>
        </div>
        <div class="flex-tile">
          <project-tile/>
        </div>
        <div class="flex-tile">
          <project-tile/>
        </div>
        <div class="flex-tile">
          <project-tile/>
        </div>
        <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile"/>
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <more-button :to="localePath('projects')" :text="$t('projects.more')" color="secondary"/>
    </div>
    <div class="row">
      <div class="col-12">
        <section-header :text="$t('menu.videos')" color="warning" icon="keyboard"/>
      </div>
    </div>
    <div>
      <div class="wrapping-flex-tiles">
        <div class="flex-tile">
          <preview-tile
            color="warning"
            image="https://i1.ytimg.com/vi/JzpF6KJErpU/hqdefault.jpg"
            title="Evropa potrebuje dobro reformo avtorskega prava"
            byline="25. 3. 2019"
          />
        </div>
        <div class="flex-tile">
          <preview-tile
            color="warning"
            image="https://i1.ytimg.com/vi/JzpF6KJErpU/hqdefault.jpg"
            title="Evropa potrebuje dobro reformo avtorskega prava"
            byline="25. 3. 2019"
          />
        </div>
        <div class="flex-tile">
          <preview-tile
            color="warning"
            image="https://i1.ytimg.com/vi/JzpF6KJErpU/hqdefault.jpg"
            title="Evropa potrebuje dobro reformo avtorskega prava"
            byline="25. 3. 2019"
          />
        </div>
        <div class="flex-tile">
          <preview-tile
            color="warning"
            image="https://i1.ytimg.com/vi/JzpF6KJErpU/hqdefault.jpg"
            title="Evropa potrebuje dobro reformo avtorskega prava"
            byline="25. 3. 2019"
          />
        </div>
        <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile"/>
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <more-button :to="localePath('videos')" :text="$t('videos.more')" color="warning"/>
    </div>
    <div class="row">
      <div class="col-12">
        <section-header :text="$t('menu.tools')" color="warning" icon="keyboard"/>
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <more-button :to="localePath('tools')" :text="$t('tools.more')" color="warning"/>
    </div>
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';
import SectionHeader from '~/components/SectionHeader.vue';
import ProjectTile from '~/components/ProjectTile.vue';
import PreviewTile from '~/components/PreviewTile.vue';
import MoreButton from '~/components/MoreButton.vue';

export default {
  components: {
    PageTitle,
    SectionHeader,
    ProjectTile,
    PreviewTile,
    MoreButton,
  },
};
</script>

<style lang="scss" scoped>
.wrapping-flex-tiles {
  @include wrapping-flex-tiles($width: 320px);
}
</style>
