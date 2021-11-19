<template>
  <q-header>
    <q-toolbar>
      <q-btn flat @click="$emit('menuClicked')" icon="menu" aria-label="Menu" />
      <img src="~/assets/images/logo-white-big.webp" height="25px" />
    </q-toolbar>

    <q-toolbar class="q-pa-none">
      <!-- Burger Menu & Title -->
      <q-btn
        flat
        stretch
        @click="$emit('menuClicked')"
        icon="menu"
        aria-label="Menu"
      />
      <q-toolbar-title class="text-h6 text-black text-no-wrap">
      </q-toolbar-title>
    </q-toolbar>
  </q-header>
</template>

<script>
import { defineComponent } from "vue";
import Global from "src/mixins/Global.js";

export default defineComponent({
  name: "Header",
  mixins: [Global],
  computed: {
    language() {
      return this.$i18n.locale;
    },
    backIcon() {
      return this.language == "he" ? "navigate_next" : "navigate_before";
    },
  },
});
</script>

<style lang="scss" scoped>
.back-icon {
  font-weight: 300;
  margin: 0;
}
.o-absolute {
  position: absolute;
  right: 0;
  &.left {
    right: unset;
  }
}

.main-heading {
  font-size: 21px;
  line-height: 21px;
  color: #000;
}
</style>
