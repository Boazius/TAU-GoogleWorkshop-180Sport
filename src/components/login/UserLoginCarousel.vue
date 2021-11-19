<template>
  <q-carousel
    v-model="component"
    transition-prev="slide-right"
    transition-next="slide-left"
    animated
    infinite
    class="q-mx-auto small-width"
  >
    <q-carousel-slide name="Login" class="no-wrap">
      <login
        @switchMode="switchMode({ value: false, component: 'Login' })"
        @loading="loading = $event"
        :loading="loading"
        :errorMessage="errorMessage"
      ></login>
    </q-carousel-slide>
    <q-carousel-slide name="Signup" class="content-center">
      <transition
        appear
        enter-active-class="animated fadeIn"
        leave-active-class="animated fadeOut"
        mode="out-in"
      >
        <signup
          @switchMode="switchMode({ value: true, component: 'Signup' })"
          @signupFormData="signupHandler($event)"
          @loading="loading = $event"
          :loading="loading"
          :errorMessage="errorMessage"
        ></signup>
      </transition>
    </q-carousel-slide>
  </q-carousel>
</template>

<script>
// import { mapState, mapActions } from "vuex";
import Login from "components/login/LoginForm.vue";
import Signup from "components/login/SignupForm.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "UserLoginCarousel",
  data() {
    return {
      signinMode: true,
      component: "Signup",
      loading: false,
    };
  },
  components: {
    Login,
    Signup,
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
    //   signup: 'authentication/signup',
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
    async signupHandler(formData) {
      const response = await this.signup(formData);
      if (response.data !== false) {
        this.component = "Login";
      }
      this.loading = false;
    },
    switchMode({ value, component }) {
      this.signinMode = value;
      this.component = component;
    },
  },
});
</script>

<style lang="scss" scoped>
.small-width {
  width: 355px;
}
</style>
