<template>
  <section class="self-center full-width">
    <q-form @submit.prevent="formHandler" autofocus>
      <q-input
        no-error-icon
        v-model="email"
        ref="email"
        name="email"
        clearable
        lazy-rules
        clear-icon="close"
        label-color="text-grey-1"
        @blur="reset('email')"
        :label="$t('authentication.email')"
        :rules="emailRules"
      >
      </q-input>
      <q-input
        no-error-icon
        v-model="password"
        ref="password"
        name="password"
        clearable
        lazy-rules
        clear-icon="close"
        label-color="text-grey-1"
        @blur="reset('password')"
        :label="$t('authentication.password')"
        :rules="passwordRules"
      >
      </q-input>

      <black-button class="q-mt-sm" type="'submit'" :loading="submitting">{{
        $t("authentication.signup")
      }}</black-button>
    </q-form>
    <div class="q-mt-md q-px-md">
      {{ $t("authentication.already") }}
      <span
        class="text-primary text-underline cursor-pointer"
        @click="$emit('signinMode', true)"
      >
        {{ $t("authentication.signin2") }}</span
      >
    </div>
  </section>
</template>

<script>
import BlackButton from "components/basic/BlackButton";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Signup",
  props: ["errorMessage", "loading"],
  components: {
    BlackButton,
  },
  data() {
    return {
      password: "",
      email: "",
      emailRules: [
        (email) => !!email || this.$t("authentication.email1"),
        (email) => /.+@.+\..+/.test(email) || this.$t("authentication.email2"),
      ],
      passwordRules: [(pass) => !!pass || this.$t("authentication.password1")],
    };
  },
  computed: {
    submitting: {
      get() {
        return this.loading;
      },
      set(value) {
        this.$emit("loading", value);
      },
    },
  },
  methods: {
    formHandler() {
      const formData = {
        email: this.email,
        password: this.password,
        locale: this.$i18n.locale,
      };
      this.$emit("signupFormData", formData);
    },
    reset(fieldName) {
      this.$refs[fieldName].resetValidation();
    },
  },
});
</script>

<style lang="scss" scoped></style>
