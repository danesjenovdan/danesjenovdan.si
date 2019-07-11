<template>
  <div class="logo-box">
    <div class="logo-box__content">
      <img src="/img/logo_gong.png" alt="gong logo" />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.logo-box {
  display: block;
  width: 100%;
  height: 0;
  padding-top: 100%;
  position: relative;
  background-color: #fff;

  .logo-box__content {
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    padding: 2rem;

    img {
      width: 100%;
      filter: brightness(0);
    }
  }
}
</style>
