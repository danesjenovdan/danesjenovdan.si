<template>
  <news-article :title="title" :date="date">
    <p>
      V okviru sofinanciranja aktivnosti
      <strong
        >PODPRI: razvoj inovativnih modelov podporništva in komuniciranja za
        NVO</strong
      >, ki je subvencionirana s strani Ministrstva za javno upravo RS znotraj
      javnega razpisa razvoj in profesionalizacija NVO in prostovoljstva 2019,
      bomo konzorcijski partnerji naslovili problematiko nižanja demokratičnih
      standardov v Sloveniji in krčenja prostora za delovanje civilno družbenih
      organizacij na področju človekovih pravic, enakosti in svobode medijev.
    </p>
    <p>
      <strong>Namen vzpostavitve konzorcija</strong> je okrepiti obstoječe
      sodelovanje partnerjev na tistih ključnih vsebinskih področjih in
      razvojnih aktivnostih, kjer lahko ustvarimo sinergije s povezovanjem
      kompetenc in virov, kot so raziskovanje in zagovorništvo, preiskovalno
      novinarstvo, podpora novinarski skupnosti, ozaveščanje in izobraževanje,
      aktivizem in participacija skupnosti, da bi tako presegli omejitve na
      ravni posameznega partnerja ter skupno povečali kakovost in doseg
      delovanja za pozitivne spremembe v družbi.
    </p>
    <p>Osrednji strateški cilji konzorcija so:</p>
    <ul>
      <li>
        doseganje
        <strong
          >večje ozaveščenosti, dobre informiranosti, večje občutljivosti,
          podpore in participacije ciljnih javnosti</strong
        >
        pri prizadevanjih partnerjev za utrjevanje demokracije, enakosti in
        transparentnosti, skupaj doseči večjo moč pri odzivanju na družbene
        probleme, kot so sovražni govor, lažne novice in dezinformacije ter na
        kršitve demokratičnih standardov, zlorabe javnih sredstev in funkcij;
      </li>
      <li>
        s podporo javnega razpisa
        <strong
          >hitreje razvijati in preizkusiti inovativne pristope, nova orodja in
          vsebine</strong
        >
        za ciljne javnosti, ki bodo sočasno omogočale pridobivati alternativne
        vire financiranja in s tem zagotoviti boljšo dolgoročno finančno in
        kadrovsko vzdržnost;
      </li>
      <li>
        krepiti prepoznavnost delovanja konzorcijskih partnerjev in se bolj
        učinkovito povezovati z nevladnimi organizacijami, podporniki in
        aktivisti na lokalni in regionalni ravni in tako
        <strong>doseči večji doseg in učinek</strong>;
      </li>
      <li>
        vzajemni <strong>prenos znanj</strong> med partnerji ter sodelovanje na
        projektih skupnega interesa.
      </li>
    </ul>
    <p>
      <strong>Partnerji:</strong>
    </p>
    <ul>
      <li>
        <a
          href="http://www.mirovni-institut.si/"
          target="_blank"
          rel="noopener noreferrer"
          >Mirovni inštitut</a
        >
      </li>
      <li>
        <a href="https://podcrto.si/" target="_blank" rel="noopener noreferrer"
          >Pod črto</a
        >
      </li>
      <li>
        <a href="https://novinar.com/" target="_blank" rel="noopener noreferrer"
          >Društvo novinarjev Slovenije</a
        >
      </li>
    </ul>
    <p><strong>Financer:</strong></p>
    <p>
      <a
        href="https://www.gov.si/drzavni-organi/ministrstva/ministrstvo-za-javno-upravo/o-ministrstvu-za-javno-upravo/"
        target="_blank"
        rel="noopener noreferrer"
      >
        <img
          src="/img/donators/mju.png"
          alt="Ministrstvo za javno upravo"
          class="img-fluid"
          style="max-width: 270px;"
        />
      </a>
    </p>
    <p>
      <small>
        Aktivnosti sofinancira Ministrstvo za javno upravo v okviru javnega
        razpisa za razvoj in profesionalizacijo NVO in prostovoljstva 2019.
      </small>
    </p>
  </news-article>
</template>

<script>
import NewsArticle from '~/components/NewsArticle.vue';

export default {
  pageColor: 'primary',
  nuxtI18n: {
    paths: {
      sl:
        '/novice/podpri-razvoj-inovativnih-modelov-podporni%C5%A1tva-in-komuniciranja-za-nvo',
      en: '/news/mju-press-release',
    },
  },
  components: {
    NewsArticle,
  },
  data() {
    return {
      title:
        'PODPRI: razvoj inovativnih modelov podporništva in komuniciranja za NVO',
      date: '2019-11-01',
    };
  },
  head() {
    return {
      title: this.title,
    };
  },
};
</script>
