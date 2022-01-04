<template>
  <q-page padding>
    <div class="row">
      <q-item-section
        class="table_header wrap q-mb-sm"
        style="font-size: xx-large"
        >{{ $t("user.userPageHeader") }}
      </q-item-section>
      <q-space />
    </div>
    <user-credentials-list :fromAdmin="false"></user-credentials-list>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import UserCredentialsList from "components/list/UserCredentialsList.vue";

export default defineComponent({
  name: "MyDetails",

  data() {
    return {};
  },

  components: {
    UserCredentialsList,
  },
});
</script>

<style scoped>
@import "assets/tableStyle.css";
</style>
