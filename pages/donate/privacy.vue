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
};
</script>
