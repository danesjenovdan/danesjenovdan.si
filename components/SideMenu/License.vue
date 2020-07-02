<template>
  <div class="license">
    <div v-if="$i18n.locale === 'sl'" xmlns:dct="http://purl.org/dc/terms/">
      Izdano pod licenco
      <a
        rel="license"
        href="https://creativecommons.org/publicdomain/zero/1.0/deed.sl"
        >CC0</a
      >. Kolikor dopušča zakonodaja, se
      <a rel="dct:publisher" href="https://danesjenovdan.si/">
        <span property="dct:title"
          >Danes je nov dan, Inštitut za druga vprašanja</span
        >
      </a>
      odpoveduje vsem avtorskim in sorodnim pravicam glede
      <span property="dct:title">spletnega mesta danesjenovdan.si</span> z
      izjemo vseh ikon in slik objavljenih na
      <a href="https://agrument.danesjenovdan.si">Agrumentu</a>, ki jih nismo
      ustvarili na inštitutu.
    </div>
    <div v-else xmlns:dct="http://purl.org/dc/terms/">
      Licensed under
      <a
        rel="license"
        href="https://creativecommons.org/publicdomain/zero/1.0/deed.en"
        >CC0</a
      >. As far as the law allows,
      <a rel="dct:publisher" href="https://danesjenovdan.si/">
        <span property="dct:title"
          >Danes je nov dan, Inštitut za druga vprašanja (Today is a new day,
          Institute for other studies)</span
        >
      </a>
      waives all copyright and related or neighboring rights to
      <span property="dct:title">danesjenovdan.si</span>, excluding all icons
      and images on
      <a href="https://agrument.danesjenovdan.si">Agrument</a> that are not
      produced by Danes je nov dan.
    </div>
  </div>
</template>

<style lang="scss" scoped>
.license {
  font-size: 0.75rem;
  line-height: 1.1;
  font-weight: 200;

  a {
    color: inherit;
    font-weight: 400;
  }
}
</style>
