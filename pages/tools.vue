<template>
  <div>
    <page-title :title="$t('menu.tools')" :text="$t('tools.description')" color="warning"/>
    <div class="row">
      <div class="col-12">
        <div class="tool-tile bg-white">
          <div class="row">
            <div class="col-md-6 left-col">
              <div class="d-flex flex-column justify-content-center h-100">
                <div class="d-flex align-items-center">
                  <div class="icon">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 160 160"
                      fill="currentColor"
                    >
                      <path
                        d="M104.6 109.1c1.7-2 2.7-4.5 2.7-7.3 0-6.2-5.1-11.3-11.4-11.3s-11.4 5.1-11.4 11.3c0 2.8 1 5.4 2.7 7.3-4.5 0-8.5 2.4-10.8 6-2.3-3.6-6.2-5.9-10.8-6 1.7-2 2.7-4.5 2.7-7.3 0-6.2-5.1-11.3-11.4-11.3s-11.4 5.1-11.4 11.3c0 2.8 1 5.4 2.7 7.3-7 .1-12.8 5.8-12.8 12.8v20.6c0 3.4 2.7 6.1 6.1 6.1.7 0 1.5-.1 2.1-.4v5.8c0 1.1.9 2 2 2s2-.9 2-2v-29.2c0-1.1-.9-2-2-2s-2 .9-2 2v17.7c0 1.2-.9 2.1-2.1 2.1-1.2 0-2.1-.9-2.1-2.1v-20.6c0-4.8 4-8.8 8.9-8.8h17.2c4.9 0 8.9 3.9 8.9 8.8v20.3c0 1.3-1.1 2.3-2.4 2.3-1.3 0-2.4-1.1-2.4-2.3v-17.5c0-1.1-.9-2-2-2s-2 .9-2 2V154c0 1.1.9 2 2 2s2-.9 2-2v-5.9c.7.3 1.5.5 2.4.5 1.7 0 3.2-.6 4.3-1.7 1.1 1 2.6 1.7 4.2 1.7.7 0 1.5-.1 2.1-.4v5.8c0 1.1.9 2 2 2s2-.9 2-2v-29.2c0-1.1-.9-2-2-2s-2 .9-2 2v17.7c0 1.2-1 2.1-2.1 2.1s-2.1-.9-2.1-2.1v-20.6c0-4.8 4-8.8 8.9-8.8h17.2c4.9 0 8.9 3.9 8.9 8.8v20.3c0 1.3-1.1 2.3-2.4 2.3s-2.4-1.1-2.4-2.3v-17.5c0-1.1-.9-2-2-2s-2 .9-2 2V154c0 1.1.9 2 2 2s2-.9 2-2v-5.9c.7.3 1.5.5 2.4.5 3.5 0 6.4-2.8 6.4-6.3V122c0-7.1-5.7-12.8-12.8-12.9zm-47.5 0c-4.1 0-7.4-3.3-7.4-7.3s3.3-7.3 7.4-7.3 7.4 3.3 7.4 7.3-3.3 7.3-7.4 7.3zm38.9 0c-4.1 0-7.4-3.3-7.4-7.3s3.3-7.3 7.4-7.3 7.4 3.3 7.4 7.3-3.4 7.3-7.4 7.3zM110.6 6H42.4C25.8 6 12.3 19.5 12.3 36.1s13.5 30.1 30.1 30.1h6.8l6 16.9c.3.8 1 1.3 1.9 1.3s1.6-.5 1.9-1.3l6-16.9h23.1l6 16.9c.3.8 1 1.3 1.9 1.3s1.6-.5 1.9-1.3l6-16.9h6.8c16.6 0 30.1-13.5 30.1-30.1C140.7 19.5 127.2 6 110.6 6zm0 56.2h-8.2c-.8 0-1.6.5-1.9 1.3L96 76.4l-4.6-12.9c-.3-.8-1-1.3-1.9-1.3h-26c-.8 0-1.6.5-1.9 1.3L57 76.4l-4.6-12.9c-.3-.8-1-1.3-1.9-1.3h-8.2c-14.4 0-26.1-11.7-26.1-26.1C16.3 21.7 28 10 42.4 10h68.2c14.4 0 26.1 11.7 26.1 26.1 0 14.4-11.7 26.1-26.1 26.1z"
                      ></path>
                      <path
                        d="M71.8 30.6c-.7-.4-1.6-.6-2.4-.6h-9.1c.4-2.5.6-5.1.5-7.7v-.2c-.1-1.6-.7-3.1-1.9-4.3-1.1-1.2-2.8-1.7-4.3-1.3-.5.1-1 .3-1.4.6-1.2.7-2 2.1-2 3.5v1.8c0 1.4-.3 2.7-.8 4-.5 1.3-1.3 2.4-2.3 3.4L46.6 31c-.4-.3-.8-.6-1.4-.6h-7.9c-1.1 0-2 .9-2 2v21.4c0 1.1.9 2 2 2h7.9c1.1 0 1.9-.8 2-1.9 1.1.3 2.3.4 3.4.4h13.6c2.1 0 4-.8 5.5-2.3 1-1 1.8-2.3 2.1-3.8 2.8-12.1 2.8-12.8 2.8-13.2 0-1.7-1.1-3.5-2.8-4.4zm-28.6 4.7V52h-3.9V34.5h3.9v.8zm24.7 12.2c-.2.7-.5 1.3-1 1.8-.7.7-1.6 1.1-2.6 1.1H50.7c-1.2 0-2.3-.2-3.4-.5V36.1l3.6-3.6c1.4-1.3 2.4-2.9 3.1-4.7.7-1.8 1.1-3.6 1.1-5.5v-1.8s0-.1.1-.1.1-.1.2-.1c.2 0 .4.1.6.3.4.4.7 1 .7 1.7v.2c.1 2.5-.1 5-.5 7.5l-.3 1.7c-.1.6 0 1.2.4 1.6.4.5.9.7 1.5.7h11.6c.2 0 .4 0 .6.2.4.2.6.6.6 1-.1.4-.8 4-2.7 12.3zM115.6 16.3h-7.9c-1.1 0-1.9.8-2 1.9-1.1-.3-2.3-.4-3.4-.4H88.8c-2.1 0-4 .8-5.5 2.3-1 1-1.8 2.3-2.1 3.8-2.8 12.1-2.8 12.8-2.8 13.2 0 1.9 1 3.7 2.8 4.6.7.4 1.6.6 2.4.6h9.1c-.4 2.5-.6 5.1-.5 7.7v.2c.1 1.6.7 3.1 1.9 4.3.9.9 2.1 1.4 3.4 1.4.3 0 .6 0 1-.1.5-.1 1-.3 1.4-.6 1.2-.7 2-2.1 2-3.5v-1.8c0-1.4.3-2.7.8-4 .5-1.3 1.3-2.4 2.3-3.4l1.4-1.4c.4.3.8.6 1.4.6h7.9c1.1 0 2-.9 2-2V18.3c-.1-1.1-.9-2-2.1-2zm-9.8 19.8l-3.6 3.6c-1.3 1.3-2.4 2.9-3.1 4.7-.7 1.8-1.1 3.6-1.1 5.5v1.8s0 .1-.1.1-.1.1-.2.1c-.2 0-.4-.1-.6-.3-.4-.4-.7-1-.7-1.7v-.2c-.1-2.5.1-5 .5-7.5l.3-1.7c.1-.6 0-1.2-.4-1.6-.4-.5-.9-.7-1.5-.7H83.7c-.2 0-.4 0-.6-.2-.4-.2-.6-.6-.6-1 0-.6.8-4.1 2.7-12.4.2-.7.5-1.3 1-1.8.7-.7 1.6-1.1 2.6-1.1h13.6c1.2 0 2.3.2 3.4.5v13.9zm7.8 1.6h-3.9V20.3h3.9v17.4z"
                      ></path>
                    </svg>
                  </div>
                  <div class="title d-flex flex-column">
                    <h2>Parlameter</h2>
                    <h3>A complete solution for any organization aiming for full transparency and digitalization of sessions.</h3>
                  </div>
                </div>
                <div class="d-flex">
                  <div class="icon"/>
                  <div class="links">
                    <ul>
                      <li>
                        <a href="#" target="_blank">parlameter.si</a>
                      </li>
                      <li>
                        <a href="#" target="_blank">parlameter.si</a>
                      </li>
                      <li>
                        <a href="#" target="_blank">parlameter.si</a>
                      </li>
                      <li>
                        <a href="#" target="_blank">parlameter.si</a>
                      </li>
                      <li>
                        <a href="#" target="_blank">parlameter.si</a>
                      </li>
                      <li>
                        <a href="https://github.com/danesjenovdan" target="_blank">GitHub</a>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-6 right-col">
              <p>Parlameter nudi transparenten vpogled in enostavno dostopnost ter preglednost informacij o delu parlamenta. Zbiramo in analiziramo podatke o glasovanjih, transkripte sej, pa tudi siceršnje aktivnosti poslancev ter poslanskih skupin.</p>
              <p>Podatki so urejeni na strojem in ljudem prijazen način: za prve so tu API klici, za druge pa kartični dizajn oz. inovativna organizacija podatkov. Vsak kos vsebine Parlametra namreč živi v obliki samostojne kartice, ki jo uporabnik lahko deli z drugimi ali vdela v svoje spletno mesto.</p>
              <p>Razvoj Parlametra je podprl Google DNI, njegovo samostojno življenje pa trenutno lajša še štipendija NED.</p>
              <p>Vrednost projekta pripoznavajo strokovna (nagrada Brumen, velika nagrada Diggit), novinarska (vdelan je na STA), pa tudi tuja nevladniška javnost: kmalu Parlameter prihaja tudi na Hrvaško, v Bosno in v Veliko Britanijo.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from '~/components/PageTitle.vue';

export default {
  nuxtI18n: {
    paths: {
      sl: '/orodja',
      en: '/tools',
    },
  },
  components: {
    PageTitle,
  },
  data() {
    return {
      filters: [
        { key: 'okolje', label: 'Okolje', active: false },
        { key: 'pravice', label: 'Človekove pravice', active: true },
        { key: 'demokracija', label: 'Demokracija', active: false },
        { key: 'lulz', label: 'For the lulz', active: false },
      ],
    };
  },
  head() {
    return {
      title: this.$t('menu.tools'),
    };
  },
};
</script>

<style lang="scss" scoped>
.tool-tile {
  padding: 2.5rem 4rem;

  .left-col,
  .right-col {
    padding: 1.5rem 0;
  }

  .left-col {
    border-bottom: 1px solid #686d6e;
    padding-bottom: 2.5rem;

    @include media-breakpoint-up(md) {
      border-bottom: none;
      padding-bottom: 0;
      border-right: 1px solid #686d6e;
      padding-right: 2.5rem;
    }

    .icon {
      flex-basis: 20%;
      flex-shrink: 0;
      color: $color-yellow;
      margin-right: 2rem;
    }

    .title {
      h2 {
        font-size: 4.3rem;
        font-weight: 600;
      }

      h3 {
        font-size: 1.5rem;
        font-weight: 300;
        font-style: italic;
      }
    }

    .links {
      margin-top: 2rem;

      ul {
        list-style: none;
        margin: 0;
        padding: 0;
        display: flex;
        flex-wrap: wrap;

        li {
          flex-basis: 50%;
          margin-bottom: 0.75rem;

          a {
            color: inherit;
            text-decoration: underline;
            font-style: italic;

            &:hover {
              text-decoration: none;
            }

            &::before {
              content: '';
              display: inline-block;
              width: 1.7rem;
              height: 100%;
              background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path d="M89.333 30.938l-20.271-20.27a5.54 5.54 0 0 0-3.892-1.613 5.553 5.553 0 0 0-3.886 1.613L41.958 29.995a5.455 5.455 0 0 0-1.612 3.889 5.458 5.458 0 0 0 1.611 3.89 5.46 5.46 0 0 0 3.889 1.611c1.47 0 2.851-.572 3.888-1.611l15.439-15.439 12.493 12.492-15.438 15.439c-1.039 1.039-1.611 2.42-1.611 3.89s.572 2.851 1.61 3.887a5.462 5.462 0 0 0 3.89 1.614h.003a5.472 5.472 0 0 0 3.886-1.613l19.328-19.326a5.508 5.508 0 0 0-.001-7.78zm-2.121 5.658L67.883 55.923c-.938.942-2.585.95-3.535-.002a2.478 2.478 0 0 1-.731-1.766c0-.668.26-1.296.732-1.769l16.499-16.5a1.5 1.5 0 0 0 0-2.122L66.233 19.152c-.293-.293-.677-.439-1.061-.439s-.768.146-1.061.439l-16.5 16.501c-.942.944-2.588.944-3.534-.002a2.483 2.483 0 0 1-.731-1.768c0-.667.26-1.295.732-1.767l19.327-19.328c.933-.931 2.603-.933 3.535 0l20.271 20.27c.976.975.976 2.562.001 3.538zM54.155 60.615a5.455 5.455 0 0 0-3.889 1.611l-15.439 15.44-12.493-12.492 15.438-15.438a5.457 5.457 0 0 0 1.612-3.889 5.465 5.465 0 0 0-1.61-3.89c-1.038-1.039-2.42-1.611-3.89-1.611s-2.852.572-3.889 1.611L10.667 61.285a5.464 5.464 0 0 0-1.611 3.889c0 1.47.573 2.851 1.612 3.889l20.269 20.269a5.474 5.474 0 0 0 3.888 1.614h.006a5.462 5.462 0 0 0 3.886-1.613l19.327-19.327a5.454 5.454 0 0 0 1.611-3.89c0-1.469-.572-2.85-1.61-3.888a5.46 5.46 0 0 0-3.89-1.613zm1.768 7.268l-19.33 19.33a2.499 2.499 0 0 1-3.535-.002L12.788 66.94c-.465-.465-.732-1.109-.732-1.767s.267-1.302.732-1.768l19.329-19.329c.471-.472 1.099-.731 1.767-.731s1.296.26 1.769.732c.472.473.731 1.101.731 1.769 0 .667-.26 1.295-.732 1.767l-16.499 16.5a1.5 1.5 0 0 0 0 2.122l14.614 14.613a1.5 1.5 0 0 0 2.121 0l16.501-16.501c.941-.942 2.589-.944 3.533.001.473.473.732 1.101.733 1.769 0 .667-.259 1.294-.732 1.766zm-26.979-2.327c0 1.469.571 2.851 1.61 3.89s2.42 1.611 3.89 1.611c1.469 0 2.85-.572 3.889-1.611l31.11-31.112c1.04-1.038 1.612-2.42 1.612-3.89s-.572-2.852-1.61-3.888a5.46 5.46 0 0 0-3.89-1.612 5.462 5.462 0 0 0-3.889 1.611l-31.11 31.112a5.461 5.461 0 0 0-1.612 3.889zm3.733-1.767l31.111-31.113c.473-.473 1.1-.732 1.768-.732s1.296.26 1.769.733c.472.471.731 1.099.731 1.767s-.26 1.296-.732 1.768L36.212 67.324c-.946.946-2.592.944-3.536 0a2.483 2.483 0 0 1-.731-1.769 2.476 2.476 0 0 1 .732-1.766z"/></svg>');
              background-repeat: no-repeat;
              background-size: contain;
              position: relative;
              top: 0.35rem;
            }

            &[href^="https://github.com"]::before {
              background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="1363.2 -4345.45 325.79 317.749"><path d="M1526.08-4345.45c-89.94 0-162.88 72.93-162.88 162.9 0 71.96 46.67 133.02 111.4 154.57 8.15 1.49 11.12-3.54 11.12-7.86 0-3.87-.14-14.11-.22-27.7-45.31 9.84-54.87-21.84-54.87-21.84-7.41-18.82-18.09-23.83-18.09-23.83-14.79-10.1 1.12-9.9 1.12-9.9 16.35 1.15 24.95 16.79 24.95 16.79 14.53 24.89 38.13 17.7 47.41 13.53 1.48-10.52 5.69-17.7 10.34-21.77-36.17-4.12-74.2-18.09-74.2-80.51 0-17.79 6.35-32.32 16.77-43.71-1.68-4.12-7.27-20.68 1.6-43.11 0 0 13.67-4.38 44.79 16.69 12.99-3.61 26.93-5.41 40.78-5.48 13.84.07 27.77 1.87 40.78 5.48 31.1-21.07 44.75-16.69 44.75-16.69 8.89 22.43 3.3 38.99 1.63 43.11 10.44 11.39 16.74 25.92 16.74 43.71 0 62.58-38.09 76.35-74.37 80.38 5.84 5.03 11.05 14.97 11.05 30.17 0 21.77-.2 39.34-.2 44.68 0 4.36 2.94 9.43 11.2 7.84 64.68-21.59 111.31-82.6 111.31-154.55 0-89.97-72.94-162.9-162.91-162.9" fill-rule="evenodd"/></svg>');
              background-size: 80% 80%;
              background-position: left center;
            }
          }
        }
      }
    }
  }

  .right-col {
    padding-left: 2.5rem;

    /deep/ p {
      font-size: 1.1rem;
      font-weight: 300;

      &:last-child {
        margin-bottom: 0;
      }
    }
  }
}
</style>
