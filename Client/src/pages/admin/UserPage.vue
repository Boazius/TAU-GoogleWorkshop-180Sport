<template>
  <q-page padding>
    <h3 class="table_header q-ma-sm">{{ $t("user.userPageHeader") }}</h3>
    <user-credentials-list></user-credentials-list>
  </q-page>
</template>

<script>
import UserCredentialsList from "components/list/UserCredentialsList.vue";

export default {
  name: "UserPage",
  data() {
    return {};
  },
  components: {
    UserCredentialsList,
  },
};
</script>

<style scoped>
@import "assets/tableStyle.css";
</style>
