export default {
  methods: {
    toIsoDate(isoTime) {
      return String(isoTime).split('T')[0];
    },
    toSloDate(isoTime) {
      return this.toIsoDate(isoTime)
        .split('-')
        .reverse()
        .join('. ');
    },
    toMonthYear(isoTime) {
      const [year, month] = this.toIsoDate(isoTime)
        .split('-')
        .map(Number);
      if (year && month) {
        return `${this.$t(`months[${month - 1}]`)} ${year}`;
      }
      return '';
    },
  },
};
