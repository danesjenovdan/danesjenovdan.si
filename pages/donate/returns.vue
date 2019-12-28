<template>
  <div class="checkout">
    <h1>Reklamacije in menjave</h1>
    <h2>Pravica do odstopa potrošnika od pogodbe</h2>
    <p>
      Kupec ima v skladu z Zakonom o varstvu potrošnikov pravico, da v 14­ih
      dneh od prevzema blaga podjetju po elektronski pošti
      (info@danesjenovdan.si) sporoči, da odstopa od pogodbe, ne da bi mu bilo
      treba navesti razlog za svojo odločitev. Rok se začne šteti en dan po
      datumu prevzema blaga. Edini strošek, ki bremeni kupca v zvezi z odstopom
      od pogodbe, je strošek vračila blaga (ki se v primeru pošiljanja
      obračunava po ceniku dostavne službe). Blago je potrebno vrniti prodajalcu
      najkasneje v roku 30 dni od oddanega sporočila o odstopu od pogodbe
      (nakupa) na naslov firme: Danes je nov dan, Inštitut za druga vprašanja,
      Parmova ulica 20, 1000 Ljubljana. Kupec nima pravice do odstopa od
      pogodbe, pri pogodbah katerih predmet je blago, ki je bilo izdelano po
      naročilu kupca.
    </p>
    <p>
      Izdelek, ki ga kupec vrača, mora biti nepoškodovan, v originalni embalaži
      in v nespremenjeni količini. Ob vračilu bomo na vaš TRR, ki nam ga morate
      posredovati, nakazali vračilo kupnine. Lahko pa se odločite za zamenjavo
      in izberete drug izdelek.
    </p>
    <p>
      V primeru, da je kupec prejel paket, ki se je poškodoval med transportom
      (embalaža ima vidne poškodbe) ali kaže znake odprtja, ga mora takoj
      reklamirati svojemu pismonoši, paket odnesti na pošto ter izpolniti
      reklamacijski zapisnik. Kupec je dolžan o tem obvestiti tudi prodajalca na
      elektronski naslov: info@danesjenovdan.si.
    </p>
    <h2>Uveljavljanje reklamacije</h2>
    <p>
      Reklamacijo iz naslova stvarne napake potrošnik lahko uveljavlja za vsak
      kupljeni izdelek (kar pomeni, da potrošnik zaradi napake na izdelku, za
      katerega ni bila dana garancija, lahko uveljavlja pravice iz stvarne
      napake, enako pa se lahko odloči tudi v primeru, če ne želi uveljavljati
      garancije za izdelek, za katerega je bila dana garancija).
    </p>
    <p>Napaka je po Zakonu o varstvu potrošnikov stvarna:</p>
    <ul>
      <li>
        če blago nima lastnosti, ki so potrebne za njeno normalno rabo ali za
        promet;
      </li>
      <li>
        če blago nima lastnosti, ki so potrebne za posebno rabo, za katero kupec
        blago kupuje, kipa je bila prodajalcu znana oziroma bi mu morala biti
        znana;
      </li>
      <li>
        če blago nima lastnosti in odlik, ki so bile izrecno ali molče
        dogovorjene oziromapredpisane;
      </li>
      <li>
        če je prodajalec izročil blago, ki se ne ujema z vzorcem ali modelom,
        razen če je bil vzorec ali model prikazan le zaradi obvestila.
      </li>
    </ul>
    <p>
      Kupec mora ponudnika o morebitni stvarni napaki skupaj z natančnim opisom
      le­ te in na lastne stroške obvestiti v zakonskem roku 8 dni od prejema
      blaga. Kupec ponudniku hkrati omogoči pregled artikla. Pravico do
      uveljavljanja stvarnih napak natančneje urejajo določila Zakona o varstvu
      potrošnikov. Reklamacija se upošteva le ob predložitvi dokazila o nakupu.
    </p>
  </div>
</template>

<script>
export default {
  nuxtI18n: {
    paths: {
      sl: '/reklamacije',
      en: '/returns',
    },
  },
  layout: 'checkout',
  pageColor: 'secondary',
  components: {},
  data() {
    return {};
  },
};
</script>

<style lang="scss" scoped>
.checkout {
  .donation-options {
    display: flex;
    flex-direction: column;

    @include media-breakpoint-up(md) {
      flex-wrap: wrap;
      flex-direction: row;
      margin-left: -0.75rem;
      margin-right: -0.75rem;
    }

    .donation-option {
      @include media-breakpoint-up(md) {
        flex: 1 1 250px;
        flex-direction: column;
        align-items: stretch;
        margin-left: 0.75rem;
        margin-right: 0.75rem;
      }
    }

    &.donation-gifts {
      .donation-option /deep/ .donation-option__content-wrapper {
        @include media-breakpoint-up(md) {
          flex-direction: row;
          min-height: auto;

          .donation-option__amount {
            margin-bottom: 0;
          }
        }
      }
    }
  }

  .donation-gifts-title {
    font-size: 1.25rem;
    text-align: left;
    font-weight: 300;
    margin: 1rem 0 2rem 0;
    text-transform: uppercase;

    @include media-breakpoint-up(md) {
      font-size: 1.5rem;
      margin-left: 1rem;
    }
  }

  .confirm-button-container {
    text-align: center;
  }

  .payment-container {
    .payment-loader {
      position: fixed;
      top: -1rem;
      left: -0.5rem;
      bottom: -0.5rem;
      right: -0.5rem;
      z-index: 999999;
      background: rgba(#333, 0.5);
      display: flex;
      justify-content: center;
      align-items: center;
    }
  }

  .payment-container,
  .info-content {
    max-width: 540px;
    margin: 0 auto;
  }

  .custom-checkbox {
    margin-bottom: 1rem;

    .custom-control-label {
      font-size: 1rem;
      line-height: 1.1;
      min-height: 2rem;
      display: flex;
      align-items: center;
    }
  }
}
</style>
