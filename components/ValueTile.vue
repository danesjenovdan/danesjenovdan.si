<template>
  <div class="value-tile bg-white">
    <div class="row">
      <div class="col-lg-12 col-xxl-6 left-col">
        <div class="d-flex flex-column justify-content-center h-100">
          <div class="d-flex align-items-center flex-column flex-lg-row">
            <div class="icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" fill="currentColor">
                <path
                  d="M104.6 109.1c1.7-2 2.7-4.5 2.7-7.3 0-6.2-5.1-11.3-11.4-11.3s-11.4 5.1-11.4 11.3c0 2.8 1 5.4 2.7 7.3-4.5 0-8.5 2.4-10.8 6-2.3-3.6-6.2-5.9-10.8-6 1.7-2 2.7-4.5 2.7-7.3 0-6.2-5.1-11.3-11.4-11.3s-11.4 5.1-11.4 11.3c0 2.8 1 5.4 2.7 7.3-7 .1-12.8 5.8-12.8 12.8v20.6c0 3.4 2.7 6.1 6.1 6.1.7 0 1.5-.1 2.1-.4v5.8c0 1.1.9 2 2 2s2-.9 2-2v-29.2c0-1.1-.9-2-2-2s-2 .9-2 2v17.7c0 1.2-.9 2.1-2.1 2.1-1.2 0-2.1-.9-2.1-2.1v-20.6c0-4.8 4-8.8 8.9-8.8h17.2c4.9 0 8.9 3.9 8.9 8.8v20.3c0 1.3-1.1 2.3-2.4 2.3-1.3 0-2.4-1.1-2.4-2.3v-17.5c0-1.1-.9-2-2-2s-2 .9-2 2V154c0 1.1.9 2 2 2s2-.9 2-2v-5.9c.7.3 1.5.5 2.4.5 1.7 0 3.2-.6 4.3-1.7 1.1 1 2.6 1.7 4.2 1.7.7 0 1.5-.1 2.1-.4v5.8c0 1.1.9 2 2 2s2-.9 2-2v-29.2c0-1.1-.9-2-2-2s-2 .9-2 2v17.7c0 1.2-1 2.1-2.1 2.1s-2.1-.9-2.1-2.1v-20.6c0-4.8 4-8.8 8.9-8.8h17.2c4.9 0 8.9 3.9 8.9 8.8v20.3c0 1.3-1.1 2.3-2.4 2.3s-2.4-1.1-2.4-2.3v-17.5c0-1.1-.9-2-2-2s-2 .9-2 2V154c0 1.1.9 2 2 2s2-.9 2-2v-5.9c.7.3 1.5.5 2.4.5 3.5 0 6.4-2.8 6.4-6.3V122c0-7.1-5.7-12.8-12.8-12.9zm-47.5 0c-4.1 0-7.4-3.3-7.4-7.3s3.3-7.3 7.4-7.3 7.4 3.3 7.4 7.3-3.3 7.3-7.4 7.3zm38.9 0c-4.1 0-7.4-3.3-7.4-7.3s3.3-7.3 7.4-7.3 7.4 3.3 7.4 7.3-3.4 7.3-7.4 7.3zM110.6 6H42.4C25.8 6 12.3 19.5 12.3 36.1s13.5 30.1 30.1 30.1h6.8l6 16.9c.3.8 1 1.3 1.9 1.3s1.6-.5 1.9-1.3l6-16.9h23.1l6 16.9c.3.8 1 1.3 1.9 1.3s1.6-.5 1.9-1.3l6-16.9h6.8c16.6 0 30.1-13.5 30.1-30.1C140.7 19.5 127.2 6 110.6 6zm0 56.2h-8.2c-.8 0-1.6.5-1.9 1.3L96 76.4l-4.6-12.9c-.3-.8-1-1.3-1.9-1.3h-26c-.8 0-1.6.5-1.9 1.3L57 76.4l-4.6-12.9c-.3-.8-1-1.3-1.9-1.3h-8.2c-14.4 0-26.1-11.7-26.1-26.1C16.3 21.7 28 10 42.4 10h68.2c14.4 0 26.1 11.7 26.1 26.1 0 14.4-11.7 26.1-26.1 26.1z"
                ></path>
                <path
                  d="M71.8 30.6c-.7-.4-1.6-.6-2.4-.6h-9.1c.4-2.5.6-5.1.5-7.7v-.2c-.1-1.6-.7-3.1-1.9-4.3-1.1-1.2-2.8-1.7-4.3-1.3-.5.1-1 .3-1.4.6-1.2.7-2 2.1-2 3.5v1.8c0 1.4-.3 2.7-.8 4-.5 1.3-1.3 2.4-2.3 3.4L46.6 31c-.4-.3-.8-.6-1.4-.6h-7.9c-1.1 0-2 .9-2 2v21.4c0 1.1.9 2 2 2h7.9c1.1 0 1.9-.8 2-1.9 1.1.3 2.3.4 3.4.4h13.6c2.1 0 4-.8 5.5-2.3 1-1 1.8-2.3 2.1-3.8 2.8-12.1 2.8-12.8 2.8-13.2 0-1.7-1.1-3.5-2.8-4.4zm-28.6 4.7V52h-3.9V34.5h3.9v.8zm24.7 12.2c-.2.7-.5 1.3-1 1.8-.7.7-1.6 1.1-2.6 1.1H50.7c-1.2 0-2.3-.2-3.4-.5V36.1l3.6-3.6c1.4-1.3 2.4-2.9 3.1-4.7.7-1.8 1.1-3.6 1.1-5.5v-1.8s0-.1.1-.1.1-.1.2-.1c.2 0 .4.1.6.3.4.4.7 1 .7 1.7v.2c.1 2.5-.1 5-.5 7.5l-.3 1.7c-.1.6 0 1.2.4 1.6.4.5.9.7 1.5.7h11.6c.2 0 .4 0 .6.2.4.2.6.6.6 1-.1.4-.8 4-2.7 12.3zM115.6 16.3h-7.9c-1.1 0-1.9.8-2 1.9-1.1-.3-2.3-.4-3.4-.4H88.8c-2.1 0-4 .8-5.5 2.3-1 1-1.8 2.3-2.1 3.8-2.8 12.1-2.8 12.8-2.8 13.2 0 1.9 1 3.7 2.8 4.6.7.4 1.6.6 2.4.6h9.1c-.4 2.5-.6 5.1-.5 7.7v.2c.1 1.6.7 3.1 1.9 4.3.9.9 2.1 1.4 3.4 1.4.3 0 .6 0 1-.1.5-.1 1-.3 1.4-.6 1.2-.7 2-2.1 2-3.5v-1.8c0-1.4.3-2.7.8-4 .5-1.3 1.3-2.4 2.3-3.4l1.4-1.4c.4.3.8.6 1.4.6h7.9c1.1 0 2-.9 2-2V18.3c-.1-1.1-.9-2-2.1-2zm-9.8 19.8l-3.6 3.6c-1.3 1.3-2.4 2.9-3.1 4.7-.7 1.8-1.1 3.6-1.1 5.5v1.8s0 .1-.1.1-.1.1-.2.1c-.2 0-.4-.1-.6-.3-.4-.4-.7-1-.7-1.7v-.2c-.1-2.5.1-5 .5-7.5l.3-1.7c.1-.6 0-1.2-.4-1.6-.4-.5-.9-.7-1.5-.7H83.7c-.2 0-.4 0-.6-.2-.4-.2-.6-.6-.6-1 0-.6.8-4.1 2.7-12.4.2-.7.5-1.3 1-1.8.7-.7 1.6-1.1 2.6-1.1h13.6c1.2 0 2.3.2 3.4.5v13.9zm7.8 1.6h-3.9V20.3h3.9v17.4z"
                ></path>
              </svg>
            </div>
            <div class="title d-flex flex-column">
              <h2>Pravica do dobrega življenja in solidarne družbe</h2>
            </div>
          </div>
        </div>
      </div>
      <div class="col-lg-12 col-xxl-6 right-col">
        <p>Vsakdo ima pravico do kvalitetnega zdravstva, šolstva, oskrbe in bivališča, pravico do solidarne družbe, ki nas podpira in spodbuja, pravico do prostega časa, srečnega otroštva, kreativne mladosti, preskrbljene odraslosti in varne starosti. Vsakdo ima pravico do prihodnosti. Predolgo je bilo merilo uspešnosti države njen gospodarski razvoj in merilo izpolnjenega posameznika njegov dohodek. Naše merilo je veselje do življenja.</p>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.value-tile {
  padding: 2.5rem 2rem;
  margin-bottom: 2rem;

  @include media-breakpoint-up(lg) {
    padding: 2.5rem 4rem;
  }

  .left-col,
  .right-col {
    padding: 0;

    @include media-breakpoint-up(lg) {
      padding: 1.5rem 0;
    }
  }

  .left-col {
    border-bottom: 1px solid #686d6e;
    padding-bottom: 1.5rem;

    @include media-breakpoint-up(xxl) {
      border-bottom: none;
      border-right: 1px solid #686d6e;
      padding-right: 2.5rem;
    }

    .icon {
      flex-shrink: 0;
      color: $color-yellow;
      margin-bottom: 2rem;
      width: 100px;
      height: 100px;

      @include media-breakpoint-up(lg) {
        margin-right: 2rem;
        margin-bottom: 0;
      }

      @include media-breakpoint-up(xxl) {
        margin-left: 2rem;
      }

      svg {
        width: 100%;
        height: 100%;
      }
    }

    .title {
      h2 {
        padding: 0 1rem;
        font-size: 2rem;
        font-weight: 600;
        text-align: center;

        @include media-breakpoint-up(lg) {
          text-align: left;
          font-size: 2.5rem;
        }
      }
    }
  }

  .right-col {
    padding-top: 1.5rem;

    @include media-breakpoint-up(xxl) {
      padding-left: 2.5rem;
    }

    /deep/ p {
      font-size: 1.1rem;
      font-weight: 300;
      padding: 0 1rem;

      @include media-breakpoint-up(lg) {
        padding: 0;
      }

      &:last-child {
        margin-bottom: 0;
      }
    }
  }
}
</style>
