<template>
  <div class="container-fluid">
    <div class="djnd-logo">
      <a href="/">
        <img
          src="../../../static/icons/donations/2022/djdn-logo-dark-100.png"
          alt="DJND logo"
        />
      </a>
    </div>
    <div class="row">
      <img
        class="header-image mb-3 mb-lg-5"
        src="../../../static/icons/donations/2022/naslovi/naslov_VSTOPNA.png"
        alt="Zakaj nisi še nikoli doniral_a Danes je nov dan?"
      />
    </div>
    <div class="row justify-content-center my-5">
      <div class="col-lg-10">
        <div class="row">
          <div
            v-for="option in mixedOptions"
            :key="option.title"
            class="col-lg-4 p-2"
          >
            <nuxt-link
              :to="`/novoletna-kampanja-2022/${option.leads_to}`"
              class="option-button"
            >
              <h3>{{ option.title }}</h3>
              <img
                class="button-arrow"
                src="../../../static/icons/donations/2022/noun-arrow.svg"
                alt=""
              />
            </nuxt-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  components: {},
  layout: 'donate-2022',

  pageColor: 'secondary',

  nuxtI18n: {
    paths: {
      sl: '/novoletna-kampanja-2022',
      en: '/new-years-campaign-2022',
    },
  },

  data() {
    return {
      options: [
        {
          title: 'Ker sem pozabil_a denarnico doma',
          leads_to: 'brez-denarnice',
        },
        {
          title: 'Ker nimam niti za najemnino',
          leads_to: 'ni-za-najemnino',
        },
        {
          title: 'Ker ne zaupam spletnim plačilom',
          leads_to: 'ne-zaupam',
        },
        {
          title: 'Ker vas itak plačuje Soroš',
          leads_to: 'soros',
        },
        {
          title: 'Kaj bluzite, saj sem že doniral_a',
          leads_to: 'kaj-bluzite',
        },
        {
          title: 'Ker je preveč zakomplicirano',
          leads_to: 'ne-znam',
        },
        {
          title: 'Ker sem desničar_ka',
          leads_to: 'z-desne',
        },
        {
          title: 'Ker mi že država preveč pobere od plače',
          leads_to: 'davkoplacevalec',
        },
        {
          title: 'Ker sploh ne vem, kaj vi počnete',
          leads_to: 'kaj-pocnemo',
        },
        {
          title: 'Pa saj hočem mesečno donirati',
          leads_to: 'hocem-donirati-mesecno',
        },
        {
          title: 'Pa saj hočem donirati 1 % dohodnine',
          leads_to: 'hocem-donirati-dohodnino',
        },
        {
          title: 'Ker raje dam komu, ki bolj rabi',
          leads_to: 'doniram-drugam',
        },
      ],
    };
  },

  head() {
    return {
      title: 'Zakaj nisi še nikoli doniral_a Danes je nov dan?',
      meta: [
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        {
          hid: 'description',
          name: 'description',
          content:
            'Deli svoj razlog, mi pa ti povemo, kako nam lahko vseeno pomagaš!',
        },
        {
          hid: 'og:title',
          property: 'og:title',
          content: 'Zakaj nisi še nikoli doniral_a Danes je nov dan?',
        },
        {
          hid: 'og:description',
          property: 'og:description',
          content:
            'Deli svoj razlog, mi pa ti povemo, kako nam lahko vseeno pomagaš!',
        },
        {
          hid: 'og:image',
          property: 'og:image',
          content: 'https://danesjenovdan.si/donatorska-2022_OG.png',
        },
        {
          hid: 'twitter:title',
          property: 'twitter:title',
          content: 'Zakaj nisi še nikoli doniral_a Danes je nov dan?',
        },
        {
          hid: 'twitter:description',
          property: 'twitter:description',
          content:
            'Deli svoj razlog, mi pa ti povemo, kako nam lahko vseeno pomagaš!',
        },
        {
          hid: 'twitter:image',
          property: 'twitter:image',
          content: 'https://danesjenovdan.si/donatorska-2022_OG.png',
        },
      ],
    };
  },

  computed: {
    mixedOptions() {
      const optionsTemp = [...this.options];
      for (let i = optionsTemp.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        const temp = optionsTemp[i];
        optionsTemp[i] = optionsTemp[j];
        optionsTemp[j] = temp;
      }
      return optionsTemp;
    },
  },
};
</script>

<style lang="scss" scoped>
.djnd-logo {
  display: flex;
  justify-content: end;

  a {
    margin: 40px;
  }

  img {
    width: 90px;
  }

  @include media-breakpoint-down(sm) {
    a {
      margin: 20px;
    }
  }
}

.header-image {
  max-width: 100%;
  height: auto;

  @include media-breakpoint-down(sm) {
    min-height: 140px;
    object-fit: cover;
  }
}

h1 {
  font-size: 65px;
  font-weight: 600;
  // line-height: 100px;
  font-style: italic;
  letter-spacing: -1px;
  text-align: left;
  width: 100%;

  @include media-breakpoint-down(sm) {
    font-size: 50px;
    line-height: 60px;
    margin-bottom: 0;
    padding-left: 30px;
    padding-right: 30px;
  }
}

h2 {
  font-size: 40px;
  font-style: italic;
  font-weight: 600;
  margin-bottom: 3rem;

  @include media-breakpoint-down(sm) {
    font-size: 32px;
    line-height: 40px;
    margin-bottom: 0;
    padding-left: 30px;
    padding-right: 30px;
  }
}

p {
  font-size: 20px;
  color: #333333;
  font-weight: 200;
  width: 100%;
  max-width: 872px;
  margin-top: 1em;
  margin-bottom: 1em;
  padding-left: 30px;
  padding-right: 30px;

  @include media-breakpoint-up(md) {
    font-size: 30px;
    padding: 0;
  }
}

.option-button {
  border: 1px solid #000000;
  background-image: linear-gradient(to right, #f5d6d3 0%, #fdf7f6 100%);
  padding: 50px 30px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;

  h3 {
    color: #333333;
    font-size: 36px;
    font-weight: 700;
    font-family: $font-family-sans-serif;
    line-height: 40px;
    text-align: left;
    padding-right: 20px;
    margin-bottom: 0;
  }

  .button-arrow {
    width: 50px;
  }

  &:hover {
    text-decoration: none;
    background-image: none;
    background-color: #f5d6d3;
  }

  @include media-breakpoint-down(sm) {
    padding: 30px 15px;

    h3 {
      font-size: 18px;
      line-height: 20px;
    }

    .button-arrow {
      width: 30px;
    }
  }
}

.gradient-section {
  background-image: linear-gradient(to right, #df786c 0%, #f5d6d3 100%);
  position: absolute;
  opacity: 0.2;
  top: 0;
  bottom: 0;
  width: 100vw;
  margin-left: calc(50% - 50vw);
}

.colored-text {
  color: #dc776b;
  font-weight: 900;
}

.limit-like-p {
  width: 100%;
  max-width: 872px;
}
.pad-like-p {
  padding-left: 30px;
  padding-right: 30px;
}
</style>
