export default {
  methods: {
    embedUrl(videoUrl) {
      const v = videoUrl;
      if (/[/.]youtube\.com\//.test(v) || /[/.]youtu\.be\//.test(v)) {
        const m = /[?&]v=(.*?)(?:&|$)/.exec(v) || /youtu\.be\/(.*?)(?:\?|$)/.exec(v);
        if (m && m.length > 1) {
          return `https://www.youtube.com/embed/${m[1]}?rel=0&modestbranding=1`;
        }
      }
      if (/[/.]vimeo\.com\//.test(v)) {
        const m = /vimeo\.com\/(\d*?)(?:\?|$)/.exec(v);
        if (m && m.length > 1) {
          return `https://player.vimeo.com/video/${m[1]}`;
        }
      }
      return '';
    },
  },
};
