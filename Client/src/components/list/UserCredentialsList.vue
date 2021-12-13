<template>
  <section class="col q-gutter-x-md bg-grey-2 q-pa-md">
    User data:{{ userData }} <br />
    Edited data: {{ editedUser }}
    <q-form @submit.prevent="formHandler" autofocus class="max-width">
      <q-input
        no-error-icon
        v-model="editedUser.name"
        name="name"
        clearable
        lazy-rules
        clear-icon="close"
        :label="$t('table.name')"
        :rules="[
          (val) => (val && val.length > 0) || $t('authentication.field'),
        ]"
        label-color="text-grey-1"
      />
      <q-input
        no-error-icon
        v-model="editedUser.email"
        ref="email"
        name="email"
        type="email"
        lazy-rules
        :label="$t('authentication.email')"
        label-color="text-grey-1"
        :rules="emailRules"
      />
      <q-input
        no-error-icon
        v-model="editedUser.phone"
        name="phone"
        type="tel"
        clearable
        clear-icon="close"
        lazy-rules
        mask="###-#######"
        :label="$t('table.phone')"
        :rules="[
          (val) => (val && val.length > 9) || $t('authentication.field'),
        ]"
        label-color="text-grey-1"
      />
      <q-select
        v-model="editedUser.group"
        :options="groupOptions"
        emit-value
        :label="$t('table.groups')"
        class="q-pb-md"
      />

      <q-input
        no-error-icon
        v-model="editedUser.area"
        name="area"
        clearable
        lazy-rules
        clear-icon="close"
        :label="$t('table.livingArea')"
        :rules="[
          (val) => (val && val.length > 0) || $t('authentication.field'),
        ]"
        label-color="text-grey-1"
      />
      <black-button
        class="q-mt-sm q-mr-md"
        :type="'submit'"
        :loading="loading"
        >{{ $t("table.save") }}</black-button
      >
      <black-button class="q-mt-sm" :outline="true" @click="onGoBack">{{
        $t("table.cancel")
      }}</black-button>
    </q-form>
  </section>
</template>

<script>
import BlackButton from "components/basic/BlackButton";

export default {
  name: "UserCredentialsList",
  data() {
    return {
      loading: false,
      editedUser: {
        id: 0,
        name: "",
        email: "",
        phone: "",
        group: 1,
        area: "",
      },
      emailRules: [
        (email) => !!email || this.$t("authentication.email1"),
        (email) => /.+@.+\..+/.test(email) || this.$t("authentication.email2"),
      ],
      groupOptions: [
        {
          label: "group 1",
          value: "1",
        },
        {
          label: "group 2",
          value: "2",
        },
        {
          label: "group 1",
          value: "3",
        },
      ],
    };
  },
  computed: {
    userData() {
      return this.$store.getters["authentication/getEditedUser"];
    },
  },
  methods: {
    onGoBack() {
      this.$router.go(-1);
    },
    formHandler() {},
  },
  created() {
    if (this.userData !== {}) {
      this.editedUser = JSON.parse(JSON.stringify(this.userData));
    }
  },
  unmounted() {
    this.$store.dispatch("authentication/setEditedUser", {});
  },
  components: {
    BlackButton,
  },
};
</script>

<style scoped lang="scss"></style>
