const global = {
  computed: {
    isRtl() {
      return this.$store.state.authentication.user.language === 'he'
    },
    isHeb() {
      return this.$i18n.locale === 'he';
    },
    isDesktop() {
      return this.$q.platform.is.desktop;
    },
    isMobile() {
      return this.$q.platform.is.mobile;
    },
  }
};

export default global;
