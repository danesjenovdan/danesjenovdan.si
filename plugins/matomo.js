import Vue from 'vue';
import VueMatomo from 'vue-matomo';

export default ({ app }) => {
  Vue.use(VueMatomo, {
    // Configure your matomo server and site by providing
    host: 'https://track.djnd.si',
    siteId: 11,
    router: app.router,
    disableCookies: true,
    enableHeartBeatTimer: true,
  });
};
