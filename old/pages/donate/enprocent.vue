<template>
  <div class="donation-landing-container">
    <donation-logo />
    <div class="row justify-content-center">
      <div class="limit-like-p">
        <h1 class="mt-4">Poženi nov dan z <br />1 % dohodnine</h1>
        <p>
          Podpri Danes je nov dan z 1 % svoje dohodnine, ki bo sicer romala
          neznano kam. Postopek je čisto preprost in te nič ne stane, nam pa
          bodo sredstva prišla še kako prav.
        </p>
        <p>
          <span class="important"
            >Če uporabljaš eDavke,
            <a
              href="https://edavki.durs.si/EdavkiPortal/OpenPortal/CommonPages/Opdynp/PageD.aspx?category=namenitev_dela_dohodnine_fo"
              target="_blank"
              >obišči portal</a
            ></span
          >, vpiši našo davčno številko (54561710) in potrdi izbiro.
        </p>
        <p>
          <span class="important"
            >V nasprotnem primeru pa spodnji obrazec dopolni s svojimi podatki
            in ga pošlji na FURS ali pa CNVOS</span
          >
          – točna navodila se nahajajo spodaj. A pozor, ker bodo upoštevane
          zgolj tiste odločbe, ki bodo na davčni urad prispele do konca leta,
          poskrbi, da to storiš dovolj zgodaj (CNVOS bo obrazce razpošiljal že
          20. decembra).
        </p>
        <p>Hvala, ker nam pomagaš spreminjati svet na bolje!</p>
      </div>
    </div>

    <div class="row justify-content-center my-5">
      <iframe
        id="enprocent_iframe"
        frameborder="0"
        width="800"
        height="600"
        style="max-width: 100%"
        src="https://www.cnvos.si/enprocent/embed/v2/?address=Parmova%20ulica%2020&city=Ljubljana&name=Danes%20je%20nov%20dan%2C%20In%C5%A1titut%20za%20druga%20vpra%C5%A1anja&percent=1.0&postalCode=1000&taxNumber=54561710"
      ></iframe>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/iframe-resizer/4.3.2/iframeResizer.min.js"></script>
      <script>
        iFrameResize({ checkOrigin: false }, '#enprocent_iframe');
      </script>
    </div>
  </div>
</template>

<script>
import DonationLogo from '~/components/DonationLogo.vue';

export default {
  components: {
    DonationLogo,
  },
  layout: 'donate',

  pageColor: 'secondary',

  nuxtI18n: {
    paths: {
      sl: '/doniraj/en-procent',
      en: '/donate/one-percent',
    },
  },
};
</script>

<style lang="scss" scoped>
/deep/ .logo {
  width: 230px;

  @include media-breakpoint-up(sm) {
    width: 300px;
  }
}

.limit-like-p {
  width: 100%;
  max-width: 872px;
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

a {
  text-decoration: underline;
  color: #333333;
  &:hover {
    text-decoration: none;
  }
}

.important {
  font-weight: 600;
  font-style: italic;
}
</style>
