<template>
  <article class="row agrument-article">
    <div class="col-7">
      <div class="article__image">
        <figure>
          <img
            src="https://agrument.danesjenovdan.si/media/1551649592261-singlizem.png"
            class="img-fluid"
          >
          <figcaption>
            <a href="https://danesjenovdan.si">Danes je nov dan</a>
          </figcaption>
        </figure>
      </div>
    </div>
    <div class="col-5">
      <div class="article__title">
        <h2>Proti singlizmu!</h2>
        <div class="article__date">
          <time datetime="2019-03-06">6. 3. 2019</time>
        </div>
      </div>
    </div>
    <div class="col-8 offset-2">
      <div class="bg-white article__content">
        <div class="article__text">
          <p>
            Na zahodu število samskih ljudi
            <a href="#">narašča</a>. Zdi se, da to drži tudi za Slovenijo, čeprav uradnih podatkov nimamo. Za statistični urad smo namreč vsi, ki nismo bili nikoli poročeni, samski.
          </p>
          <p>Čeprav se naša razmerja spreminjajo, pa singlizem (singlism) - stigmatizacija in diskriminacija samskih - ostaja prisoten v družbi. Ljudje, ki so poročeni in imajo družino, so dojeti kot bolj odgovorni in resni, medtem ko so samski posamezniki velikokrat videni kot nesrečneži, ki še niso našli ljubezni in sreče. Samske pa ne le obsojamo, temveč ima lahko samskost tudi zelo konkretne posledice, saj je družba pač prilagojena življenju v paru: samskim ženskam smo prepovedali umetno oploditev, brez “boljše polovice” pa je izredno težko dobiti kredit.</p>
          <p>Družbeni pritiski in nerazvit sistem oskrbe samskih starejših mnoge tišči v okvire zakona in nuklearne družine. Zaradi vedno večjega števila samskih pa bi se kot družba morali začeti ukvarjati s sistemi kohabitacije, namesto da jih vedno znova - diskriminiramo.</p>
        </div>
        <hr>
        <div class="article__share">
          <form class="form-inline">
            <div class="form-group">
              <label for="share-link">
                <em>Skopiraj povezavo!</em>
              </label>
              <input
                id="share-link"
                class="form-control"
                value="https://djnd.si/baf"
                onfocus="this.select()"
              >
            </div>
          </form>
        </div>
      </div>
    </div>
  </article>
</template>

<style lang="scss" scoped>
article {
  margin-bottom: 6rem;

  .article__image {
    position: relative;
    z-index: 1;

    img {
      width: 100%;
    }

    figcaption {
      margin-top: 0.75rem;
      font-style: italic;
      text-align: right;

      a {
        font-weight: 400;
        text-decoration: underline;
        color: inherit;

        &:hover {
          text-decoration: none;
        }
      }
    }
  }

  .article__title {
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    height: 100%;
    justify-content: center;

    h2 {
      font-size: 4.3rem;
      font-weight: 600;
    }

    .article__date {
      font-style: italic;
      margin-top: 1rem;
    }
  }

  .article__content {
    padding-left: 8rem;
    padding-right: 8rem;
    padding-bottom: 2.5rem;

    $bg-offset: 25rem;
    padding-top: 2.5rem + $bg-offset;
    margin-top: -$bg-offset;

    .article__text {
      font-size: 1.25rem;
      font-weight: 300;

      a {
        font-weight: 600;
        text-decoration: underline;
        color: inherit;

        &:hover {
          text-decoration: none;
        }
      }
    }

    hr {
      border-top-color: #333;
      margin-top: 3rem;
      margin-bottom: 2rem;
    }

    .article__share {
      em {
        margin-right: 2rem;
      }
    }
  }
}
</style>
