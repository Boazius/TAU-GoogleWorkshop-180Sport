<template>
  <q-page padding>
    <div class="row">
      <div>
        <q-btn
          size="sm"
          class="q-mr-md q-mt-sm"
          padding="sm"
          glossy
          :ripple="{ center: true }"
          color="primary"
          icon="arrow_forward"
          @click="onGoBack()"
        />
      </div>
      <q-item-section
        class="table_header wrap q-mb-sm"
        style="font-size: xx-large"
        >{{ $t("user.userPageHeader") }}
      </q-item-section>
      <q-space />
    </div>
    <user-credentials-list :fromAdmin="true"></user-credentials-list>
  </q-page>
</template>

<script>
import UserCredentialsList from "components/list/UserCredentialsList.vue";

export default {
  name: "UserPage",
  methods: {
    onGoBack() {
      this.$router.go(-1);
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
