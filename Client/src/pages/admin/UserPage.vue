<template>
  <q-page padding>
    <div class="row">
      <div>
        <q-btn
          size="sm"
        class="q-mr-md q-mt-sm"
          padding="sm"
          glossy
          ripple="center"
          color="primary"
          icon="arrow_forward"
          to="/trainees"
        />
      </div>
      <q-item-section
        class="table_header wrap q-mb-sm"
        style="font-size: xx-large"
        >{{ $t("user.userPageHeader") }}
      </q-item-section>
      <q-space />
    </div>
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
  methods: {
    handler() {
      window.localStorage.removeItem('userdata');
    },
  },
  components: {
    UserCredentialsList,
  },
};
</script>

<style scoped>
@import "assets/tableStyle.css";
</style>
