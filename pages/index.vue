<template>
  <div>
    <page-title :title="$t('hello')" :text="$t('landing.description')"/>
    <div class="row">
      <div class="col-12">
        <section-header :text="$t('menu.agrument')" icon="keyboard"/>
      </div>
    </div>
    <div class="mt-4">
      <promoted-tile
        image="https://agrument.danesjenovdan.si/media/by_id/1411.jpg"
        title="O arhitekurnem prekariatu"
        byline="25. 3. 2019"
        text="Študenti ljubljanske Fakultete za arhitekturo so v javnem pismu opozorili, da jih profesorji izkoriščajo. Ti poleg ..."
      />
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
    <div class="row mobile-no-gap">
      <div class="col-12 my-5">
        <agrument-subscribe-bar/>
      </div>
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
    <div class="row mobile-no-gap">
      <div class="col-12 my-5">
        <social-media-bar
          color="secondary"
          :text="$t('projects.social-bar.follow-us')"
          :icons="[
            { icon: 'facebook', url: 'https://facebook.com/danesjenovdan' },
            { icon: 'twitter', url: 'https://twitter.com/danesjenovdan' },
          ]"
        />
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <section-header :text="$t('menu.videos')" color="warning" icon="keyboard"/>
      </div>
    </div>
    <div class="mt-4">
      <promoted-tile
        color="warning"
        image="https://i1.ytimg.com/vi/JzpF6KJErpU/hqdefault.jpg"
        title="Evropa potrebuje dobro reformo avtorskega prava"
        byline="25. 3. 2019"
      />
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
    <div class="row mobile-no-gap">
      <div class="col-12 my-5">
        <social-media-bar
          color="warning"
          :text="$t('videos.social-bar.follow-us')"
          :icons="[
            { icon: 'youtube', url: 'https://youtube.com/danesjenovdan' },
            { icon: 'vimeo', url: 'https://vimeo.com/danesjenovdan' },
          ]"
        />
      </div>
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
import PromotedTile from '~/components/PromotedTile.vue';
import PreviewTile from '~/components/PreviewTile.vue';
import MoreButton from '~/components/MoreButton.vue';
import AgrumentSubscribeBar from '~/components/AgrumentSubscribeBar.vue';
import SocialMediaBar from '~/components/SocialMediaBar.vue';

export default {
  components: {
    PageTitle,
    SectionHeader,
    ProjectTile,
    PromotedTile,
    PreviewTile,
    MoreButton,
    AgrumentSubscribeBar,
    SocialMediaBar,
  },
};
</script>

<style lang="scss" scoped>
.wrapping-flex-tiles {
  @include wrapping-flex-tiles($width: 320px);
}
</style>
