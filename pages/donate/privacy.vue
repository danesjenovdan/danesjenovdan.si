<template>
  <div class="checkout">
    <h1>Varovanje podatkov</h1>
    <p>
      Upravitelj spletne trgovine je zavezan k varovanju osebnih podatkov po
      veljavni zakonodaji o varstvu potrošnikov.
    </p>
    <p>
      Ponudnik bo osebne podatke uporabil izključno za potrebe izpolnitve
      naročila: ime in priimek za identifikacijo kupca, elektronski naslov za
      komunikacijo s kupcem ter pošiljanje računa, naslov za pošiljanje blaga
      oz. darila pri donaciji nad 11 eur, podatki plačilne kartice za izvedbo
      plačilo. Ponudnik bo ime, elektronski ter naslov hranil skladno z veljavno
      zakonodajo in ne več kot 1 leto. Ponudnik podatkov plačilne kartice ne
      hrani.
    </p>
    <p>
      Kupec se lahko prijavi, da bo prejemal sporočila od ponudnika. V tem
      primeru ponudnik hrani ime in elektronski naslov kupca do preklica
      prijave.
    </p>
    <p>
      Podatki ne bodo v nobenem primeru posredovani nepooblaščenim osebam. Za
      potrebe dostave bomo vaše podatke zaupali dostavni službi. Za
      zagotavljanje plačila posredujemo podatke o plačilni kartici partnerju, ki
      upravlja s sistemom zagotavljanja plačil: Braintree, PayPal (Europe) S.à
      r.l. et Cie, S.C.A.
    </p>
    <p>V Ljubljani, 18. 12. 2019</p>
  </div>
</template>

<script>
export default {
  nuxtI18n: {
    paths: {
      sl: '/zasebnost',
      en: '/privacy',
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
