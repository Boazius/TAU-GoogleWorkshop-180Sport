<template>
<section class="row justify-center q-pa-md">
        <login-form
        @loading="loading = $event"
        :loading="loading"
        :errorMessage="errorMessage"
      ></login-form>
</section>

</template>

<script>
// import { mapState, mapActions } from "vuex";
import LoginForm from "components/login/LoginForm.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Login",
  data() {
    return {
      loading: false,
    };
  },
  components: {
    LoginForm,
  },
  computed: {
    errorMessage() {
      const error = {}; // Get error from server'// this.$store.getters['authentication/error'];
      if (error.has) {
        switch (error.message) {
          case "Invalid email":
            error.message = this.$t("authentication.email");
            break;
          default:
            error.message = this.$t("authentication.wrong");
        }
      }
      return error;
    },
  },
  methods: {
    // ...mapActions({
    //   login: 'authentication/login'
    // }),
    async loginHandler({ email, password }) {
      const response = await this.login({
        email,
        password,
      });
      if (response.data !== false) {
        this.$router.push({ path: "/trainers" });
      }
      this.loading = false;
    },
  },
});
</script>

<style lang="scss" scoped></style>
