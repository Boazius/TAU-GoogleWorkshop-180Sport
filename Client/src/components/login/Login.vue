<template>
  <section class="row justify-center q-pa-md">
    <div class="column items-center">
      <h2 class="heading q-ma-sm text-primary text-weight-bold text-center">
        {{ $t("app.greeting") }}
      </h2>

      <google-button></google-button>
      <span class="text-subtitle2 text-positive q-py-sm">{{
        $t("app.clickToLogin")
      }}</span>
    </div>
    <error-message-popup
      :dialog="error.show"
      :errorMessage="error.message"
      @onClose="error = false"
    />
  </section>
</template>

<script>
import GoogleButton from "components/login/GoogleButton.vue";
import ErrorMessagePopup from "components/basic/popup/ErrorMessagePopup.vue";

import { defineComponent } from "vue";

export default defineComponent({
  name: "Login",
  computed: {
    error: {
      get() {
        return this.$store.getters["authentication/error"];
      },
      set(value) {
        this.$store.dispatch("authentication/setError", {
          show: value,
          message: "",
        });
      },
    },
  },
  components: {
    GoogleButton,
    ErrorMessagePopup,
  },
});
</script>

<style lang="scss" scoped>
.heading {
  font-size: 2em;
  max-width: 70vw;
}
</style>
