<template>
  <div>
    <page-title
      :title="$t('menu.about')"
      :text="$t('about.description')"
      color="primary"
    />
    <div class="row">
      <div class="col-xl-7">
        <div class="about-info__image">
          <div class="embed-responsive embed-responsive-1200by630">
            <div class="embed-responsive-item d-flex align-items-center">
              <div
                :style="{ 'background-image': 'url(/img/about-main.jpg)' }"
                class="background-image"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="col-xl-5 about-info__contact-col">
        <div class="about-info__contact">
          <div class="icon">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 100 100"
              fill="currentColor"
            >
              <path
                d="M50 8.011c-15.482 0-28 13.048-28 29 0 5.946 2.344 13.328 5.094 18l21.187 36a2 2 0 0 0 3.438 0l21.187-36c2.75-4.672 5.094-12.054 5.094-18 0-15.952-12.518-29-28-29zm0 4c13.237 0 24 11.13 24 25 0 4.803-2.259 12.108-4.531 15.97L50 86.073 30.531 52.98C28.26 49.12 26 41.814 26 37.011c0-13.87 10.763-25 24-25zm0 9c-8.26 0-15 6.74-15 15 0 8.261 6.74 15 15 15s15-6.739 15-15c0-8.26-6.74-15-15-15zm0 4c6.099 0 11 4.902 11 11 0 6.1-4.901 11-11 11s-11-4.9-11-11c0-6.098 4.901-11 11-11z"
              />
            </svg>
          </div>
          <div class="text">
            <strong>
              Danes je nov dan,
              <br />Inštitut za druga vprašanja
              <br />
            </strong>
            Resljeva cesta 25, 1000 Ljubljana
          </div>
          <div class="icon">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 52 52"
              fill="currentColor"
            >
              <path
                d="M12.513 44.324L2.333 22.69l32.49-15.013L45 29.31 12.513 44.324zM5 23.66l8.477 18.016 28.856-13.337-8.477-18.015L5.001 23.66z"
              />
              <path
                d="M25.135 29.131L3.443 24.15l.448-1.949 20.175 4.633 9.384-18.29 1.78.914z"
              />
              <path
                d="M25.971 25.858l.44-1.951 17.476 3.942-.44 1.951zM12.106 42.54l8.188-15.802 1.776.92-8.188 15.802zM40.667 9h9v2h-9zm-8 30h17v2h-17zm13-16h4v2h-4z"
              />
            </svg>
          </div>
          <div class="text">
            <strong>
              <a
                href="mailto:vsi@danesjenovdan.si"
                target="_blank"
                rel="noopener noreferrer"
                >vsi@danesjenovdan.si</a
              >
            </strong>
          </div>
          <div class="icon">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 100 100"
              fill="currentColor"
            >
              <path
                d="M24.368 5.148c-1.375.618-2.43 1.338-3.002 2.416-8.664 16.54-11.001 32.522-6.91 46.809 4.099 14.315 14.616 26.758 31.051 36.361 1.245.531 2.687.692 3.815.408 1.184-.312 2.329-1 3.033-2.227l2.314-4.016c2.416 1.826 5.348 3.595 8.068 2.949 2.668 2.076 6.443 3.216 9.694 3.45 3.354 4.005 8.231 3.741 13.04 3.672 1.057.015 2.029-.947 2.029-2.008s-.972-2.023-2.03-2.008c-2.687 0-4.222.624-7.505-.502.912-.417 1.416-.996 1.97-1.663 1.132-2.27.564-4.862-.969-6.4-1.533-1.538-4.116-2.076-6.38-.941-1.594 1.306-2.386 3.708-2.25 5.459-1.003-.223-1.932-.51-2.721-.847.73-.348 1.149-.798 1.595-1.35.59-1.185.707-2.507.344-3.639-.906-2.225-2.91-3.528-5.097-3.64-1.576.053-2.612.488-3.69 1.256-1.105 1.614-1.4 3.126-.938 4.8-.984-.377-2.016-1.004-3.065-2.196.75-1.294 1.51-2.598 2.252-3.89.652-1.23.62-2.536.28-3.703-.339-1.166-1.032-2.31-2.25-3.011-3.478-2.022-7.528-6.062-10.82-9.287a2.035 2.035 0 0 0-1.876-.502l-10.132 2.573c-5.135-9.374-6.703-14.947-7.13-25.507l10.07-2.604a2.046 2.046 0 0 0 1.438-1.412c1.197-4.526 2.395-10.697 4.784-14.243.673-1.212.278-2.812-.156-3.859-.423-1.003-1.121-2.08-2.345-2.76-4.444-2.62-8.99-5.24-12.79-7.499-1.27-.693-2.414-.676-3.72-.44zm1.72 3.921c4.274 2.506 8.547 5.035 12.82 7.53.544.44.644.882.814 1.537C37.097 22.41 35.986 27.75 35 31.752l-10.507 2.73c-.872.225-1.529 1.104-1.5 2.008.363 12.67 2.175 19.19 8.442 30.338.435.76 1.407 1.167 2.252.94l10.57-2.697c3.112 3.07 6.838 6.802 10.787 9.098.434.406.371.772.438 1.318l-6.598 11.42c-.452.427-.876.354-1.47.313-15.722-9.212-25.351-20.812-29.112-33.946-3.769-13.16-1.693-28.02 6.66-43.922.379-.401.681-.274 1.126-.283zm39.62 73.54c-.405.34-.911.649-1.564.91-.516-.693-.548-1.226-.438-1.914 1.175-.24 1.675.1 2.001 1.003zm10.444 2.635c.321.322.427.773.281 1.349-.386.269-1.077.446-1.97.565-.318-.818-.274-1.497.281-2.197.613-.248.941 0 1.408.283z"
              />
            </svg>
          </div>
          <div class="text">
            <strong>
              <a
                href="tel:+38664147823"
                target="_blank"
                rel="noopener noreferrer"
                >+386 64 163 663</a
              >
            </strong>
          </div>
        </div>
      </div>
    </div>
    <div class="row my-3 py-xl-3" />
    <div class="row box-links">
      <div class="col-12 col-sm-6 col-md-12 col-lg-6 col-xxl-4">
        <box-link
          :to="localePath('people')"
          :title="$t('menu.people')"
          :text="$t('about.descriptions.people')"
          image="/img/about/people.svg"
        />
      </div>
      <div class="col-12 col-sm-6 col-md-12 col-lg-6 col-xxl-4">
        <box-link
          :to="localePath('values')"
          :title="$t('menu.values')"
          :text="$t('about.descriptions.values')"
          image="/img/about/values.svg"
        />
      </div>
      <div class="col-12 col-sm-6 col-md-12 col-lg-6 col-xxl-4">
        <box-link
          :to="localePath('clipping')"
          :title="$t('menu.clipping')"
          :text="$t('about.descriptions.clipping')"
          image="/img/about/clipping.svg"
        />
      </div>
    </div>
    <div class="row my-3" />
    <div class="row">
      <div class="col-12">
        <section-header :text="$t('about.our-partners')" />
      </div>
    </div>
    <div class="wrapping-flex-tiles logos">
      <div v-for="partner in partners" :key="partner.name" class="flex-tile">
        <logo-box
          :name="partner.name"
          :url="partner.url"
          :image="partner.image"
          :content-class="partner.class"
        />
      </div>
      <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile" />
    </div>
    <div class="row">
      <div class="col-12">
        <section-header :text="$t('about.our-donators')" />
      </div>
    </div>
    <div class="wrapping-flex-tiles logos">
      <div v-for="donator in donators" :key="donator.name" class="flex-tile">
        <logo-box
          :name="donator.name"
          :url="donator.url"
          :image="donator.image"
          :content-class="donator.class"
        />
      </div>
      <div v-for="n in 10" :key="`flex-spacer-${n}`" class="flex-tile" />
    </div>
    <div class="row">
      <div class="col-12">
        <section-header :text="$t('about.formalities')" />
      </div>
    </div>
    <div class="row formalities">
      <div class="col-12 mt-3">
        <p>
          {{ $t('about.mailing-address') }}
          <strong
            >Resljeva cesta 25, 1000 Ljubljana<template
              v-if="$i18n.locale !== 'sl'"
              >, Slovenia</template
            ></strong
          >
        </p>
        <p>
          {{ $t('about.tax-id') }}
          <strong>SI54561710</strong>
          <br />{{ $t('about.registration-number') }}
          <strong>6468594000</strong>
        </p>
        <p>
          {{ $t('about.bank-account') }}
          <strong>SI56 6100 0000 5740 710</strong>
          <br />(Delavska hranilnica d.d., Ljubljana)
        </p>
        <p v-t="'about.ngo'"></p>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <section-header :text="$t('about.transparency')" />
      </div>
    </div>
    <div class="row formalities">
      <div class="col-12 mt-3">
        <more-button
          :text="$t('about.yearly-reports')"
          icon="papers"
          to="https://drive.google.com/drive/folders/105Jb0F_hKvf-HBKXiwK4NRjTIbNepLFP"
        />
      </div>
      <div class="col-12 mt-3">
        <more-button
          :text="$t('about.results')"
          icon="papers"
          to="https://drive.google.com/drive/folders/1mUhlnNyfuJGJZg6ACJvBl4eBOvO-rJ-x"
        />
      </div>
      <div class="col-12 mt-3">
        <p>
          {{ $t('about.pay-ratio') }}
          <span>30. 6. 2021</span>:
          <strong>1 : 1,44</strong>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';
import BoxLink from '~/components/BoxLink.vue';
import SectionHeader from '~/components/SectionHeader.vue';
import LogoBox from '~/components/LogoBox.vue';
import MoreButton from '~/components/MoreButton.vue';
import partnersJson from '~/assets/partners.json';

export default {
  nuxtI18n: {
    paths: {
      sl: '/o-nas',
      en: '/about',
    },
  },
  components: {
    PageTitle,
    BoxLink,
    SectionHeader,
    LogoBox,
    MoreButton,
  },
  data() {
    return {
      partners: partnersJson.partners.sort((a, b) =>
        a.name.localeCompare(b.name),
      ),
      donators: partnersJson.donators.sort((a, b) =>
        a.name.localeCompare(b.name),
      ),
    };
  },
  head() {
    return {
      title: this.$t('menu.about'),
    };
  },
};
</script>

<style lang="scss" scoped>
.about-info__image {
  position: relative;
  z-index: 1;
  margin-right: 1rem;
  margin-left: -0.5rem;

  @include media-breakpoint-up(xl) {
    margin-right: -4rem;
    margin-left: 0rem;
    z-index: 2;
  }

  .background-image {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    z-index: -2;
  }
}

.about-info__contact-col {
  $bg-offset: 1.8rem;
  margin-top: -$bg-offset;
  z-index: -1;

  @include media-breakpoint-up(xl) {
    z-index: 1;
    margin-top: 0;
  }

  .about-info__contact {
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    height: 100%;
    justify-content: center;
    padding: 0 1.2rem 1.5rem 1.2rem;
    padding-top: $bg-offset;
    margin-left: 0.5rem;
    margin-right: -0.5rem;
    background-color: #fff;

    @include media-breakpoint-up(xl) {
      margin-left: 0rem;
      margin-right: 0rem;
      margin-top: 2rem;
      padding-left: 2rem;
    }

    .icon {
      width: 40px;
      height: 40px;
      margin: 1.5rem auto 0.5rem;
      color: $color-green;

      @include media-breakpoint-up(xl) {
        &:first-child {
          margin-top: 0;
        }
      }

      svg {
        width: 100%;
        height: 100%;
      }
    }

    .text {
      font-size: 1.25rem;
      font-weight: 300;
      font-style: italic;
      line-height: 1.25;
      text-align: center;

      strong {
        font-weight: 600;
      }

      a {
        color: inherit;
      }
    }
  }
}

.wrapping-flex-tiles {
  @include wrapping-flex-tiles($width: 150px, $gap: 1rem);
}

.formalities {
  p {
    font-weight: 200;
    font-size: 1.2rem;

    strong {
      font-weight: 500;
    }
  }
}

.box-links {
  .col-12 {
    display: flex;
  }
}
</style>
