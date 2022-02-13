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
const myUserid = 4;

export default defineComponent({
  name: "TraineeDetails",

  computed: {
    currentUser() {
      return this.$store.getters["authentication/getCurrentUser"];
    },
  },

  created() {
    const user = { id: this.currentUser.id };
    localStorage.setItem("user", JSON.stringify(user));

  },

  data() {
    return {
      userData: undefined,
    };
  },

  components: {
    UserCredentialsList,
  },
});
</script>

<style scoped>
@import "assets/tableStyle.css";
</style>
