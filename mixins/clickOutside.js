export default {
  directives: {
    clickOutside: {
      bind(el, binding) {
        const handler = e => {
          if (!el.contains(e.target) && el !== e.target) {
            binding.value(e);
          }
        };
        el.vueClickOutside = handler;
        document.addEventListener('click', handler);
      },
      unbind(el) {
        document.removeEventListener('click', el.vueClickOutside);
        el.vueClickOutside = null;
      },
    },
  },
};
